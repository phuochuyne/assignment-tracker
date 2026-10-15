(function () {
  "use strict";

  const STORAGE_KEY = "assignment-tracker:assignments:v1";

  function todayKey() {
    const now = new Date();
    const local = new Date(now.getTime() - now.getTimezoneOffset() * 60000);
    return local.toISOString().slice(0, 10);
  }

  function isOverdue(assignment, today = todayKey()) {
    return !assignment.completed && assignment.dueDate < today;
  }

  function sortByDeadline(assignments) {
    return [...assignments].sort((left, right) => {
      const dateOrder = left.dueDate.localeCompare(right.dueDate);
      return dateOrder || left.createdAt.localeCompare(right.createdAt);
    });
  }

  function readAssignments(storage) {
    try {
      const value = JSON.parse(storage.getItem(STORAGE_KEY) || "[]");
      return Array.isArray(value) ? value : [];
    } catch (_error) {
      return [];
    }
  }

  function writeAssignments(storage, assignments) {
    storage.setItem(STORAGE_KEY, JSON.stringify(assignments));
  }

  function formatDate(value) {
    return new Intl.DateTimeFormat("en-AU", { day: "numeric", month: "short", year: "numeric" })
      .format(new Date(`${value}T00:00:00`));
  }

  function createAssignment({ title, unitCode, dueDate }) {
    return {
      id: crypto.randomUUID(),
      title: title.trim(),
      unitCode: unitCode.trim().toUpperCase(),
      dueDate,
      completed: false,
      createdAt: new Date().toISOString()
    };
  }

  function startApp(documentObject, storage) {
    const form = documentObject.querySelector("#assignment-form");
    const message = documentObject.querySelector("#form-message");
    const activeList = documentObject.querySelector("#active-list");
    const completedList = documentObject.querySelector("#completed-list");
    const template = documentObject.querySelector("#assignment-template");
    let assignments = readAssignments(storage);

    function save() {
      try {
        writeAssignments(storage, assignments);
        message.textContent = "";
        return true;
      } catch (_error) {
        message.textContent = "This browser could not save your assignment. Check its storage settings and try again.";
        return false;
      }
    }

    function makeCard(assignment) {
      const card = template.content.firstElementChild.cloneNode(true);
      const toggle = card.querySelector(".completion-toggle");
      const status = card.querySelector(".status-badge");
      const overdue = isOverdue(assignment);

      card.dataset.assignmentId = assignment.id;
      card.classList.toggle("is-completed", assignment.completed);
      card.classList.toggle("is-overdue", overdue);
      card.querySelector("h3").textContent = assignment.title;
      card.querySelector(".assignment-meta").textContent = `${assignment.unitCode} · Due ${formatDate(assignment.dueDate)}`;
      toggle.checked = assignment.completed;
      toggle.setAttribute("aria-label", `${assignment.completed ? "Mark active" : "Mark complete"}: ${assignment.title}`);

      if (assignment.completed) {
        status.textContent = "Completed";
        status.className = "status-badge completed";
      } else if (overdue) {
        status.textContent = "Overdue";
        status.className = "status-badge overdue";
      } else {
        status.textContent = "Upcoming";
        status.className = "status-badge upcoming";
      }

      toggle.addEventListener("change", () => {
        const previous = assignment.completed;
        assignment.completed = toggle.checked;
        if (!save()) {
          assignment.completed = previous;
          toggle.checked = previous;
          return;
        }
        render();
      });

      return card;
    }

    function render() {
      const active = sortByDeadline(assignments.filter((assignment) => !assignment.completed));
      const completed = sortByDeadline(assignments.filter((assignment) => assignment.completed));

      activeList.replaceChildren(...active.map(makeCard));
      completedList.replaceChildren(...completed.map(makeCard));
      documentObject.querySelector("#active-empty").hidden = active.length > 0;
      documentObject.querySelector("#completed-empty").hidden = completed.length > 0;
      documentObject.querySelector("#upcoming-count").textContent = String(active.filter((assignment) => !isOverdue(assignment)).length);
      documentObject.querySelector("#overdue-count").textContent = String(active.filter((assignment) => isOverdue(assignment)).length);
      documentObject.querySelector("#completed-count").textContent = String(completed.length);
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const data = new FormData(form);
      const assignment = createAssignment({
        title: String(data.get("title") || ""),
        unitCode: String(data.get("unit_code") || ""),
        dueDate: String(data.get("due_date") || "")
      });

      if (!assignment.title || !assignment.unitCode || !assignment.dueDate) {
        message.textContent = "Enter a title, unit code and due date.";
        return;
      }

      assignments.push(assignment);
      if (!save()) {
        assignments.pop();
        return;
      }
      form.reset();
      message.textContent = "Assignment added.";
      render();
      documentObject.querySelector("#title").focus();
    });

    render();
  }

  const publicApi = { STORAGE_KEY, createAssignment, isOverdue, readAssignments, sortByDeadline, writeAssignments };
  if (typeof module !== "undefined" && module.exports) module.exports = publicApi;
  if (typeof window !== "undefined") {
    window.AssignmentTracker = publicApi;
    window.addEventListener("DOMContentLoaded", () => startApp(document, window.localStorage));
  }
}());

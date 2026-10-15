CREATE TABLE `f_622b64dc__assignments` (
  `id` CHAR(36) NOT NULL,
  `title` VARCHAR(500) NOT NULL,
  `unit_code` VARCHAR(50) NOT NULL,
  `due_date` DATE NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_c1936286__assignments` (
  `id` CHAR(36) NOT NULL,
  `title` VARCHAR(500) NOT NULL,
  `unit_code` VARCHAR(50) NOT NULL,
  `due_date` DATE NOT NULL,
  `completed` BOOLEAN NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- No database tables are required for feature: capability_automatic_deadline_sorting_2088096a


CREATE TABLE `f_8bb5982d__assignments` (
  `id` CHAR(36) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `unit_code` VARCHAR(50) NOT NULL,
  `due_date` DATE NOT NULL,
  `is_completed` BOOLEAN NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_1a7f53a5__assignment_completion` (
  `id` CHAR(36) NOT NULL,
  `assignment_id` CHAR(36) NOT NULL,
  `is_completed` BOOLEAN NOT NULL,
  `completed_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_1b2057db__assignment_display_metadata` (
  `id` CHAR(36) NOT NULL,
  `assignment_reference` CHAR(36) NOT NULL,
  `display_order` INT UNSIGNED NOT NULL,
  `last_rendered_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_19f07be9__assignment_completion` (
  `id` CHAR(36) NOT NULL,
  `assignment_id` CHAR(36) NOT NULL,
  `is_completed` TINYINT(1) NOT NULL,
  `completed_at` TIMESTAMP NULL DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- No database tables are required for feature: capability_overdue_assignment_highlighting_a3b2e567


-- No database tables are required for feature: capability_responsive_design_507cc59c


-- No database tables are required for feature: capability_color_coded_status_labels_b6950121
CREATE TABLE "teams" (
    "team_id" BIGSERIAL PRIMARY KEY,
    "team_lead" VARCHAR(50) NOT NULL,
    "team_lead_email" VARCHAR(50) NOT NULL,
);

CREATE TABLE "users" (
    "user_id" BIGSERIAL,
    "first_name" VARCHAR(20) NOT NULL,
    "last_name" VARCHAR(20) NOT NULL,
    "username" VARCHAR(20) UNIQUE PRIMARY KEY NOT NULL,
    "password" VARCHAR(80) NOT NULL,
    "email" VARCHAR(50) UNIQUE NOT NULL,
    "role" VARCHAR(20) NOT NULL,
    "team_id" INTEGER 
        REFERENCES "teams" ("team_id") 
        FOREIGN KEY ON DELETE SET NULL
);

CREATE TABLE "projects" (
    "project_id" BIGSERIAL PRIMARY KEY,
    "project_name" VARCHAR(50) NOT NULL,
    "project_status" VARCHAR(50) NOT NULL,
    "team_id" INTEGER 
        REFERENCES "teams" ("team_id") 
        FOREIGN KEY ON DELETE SET NULL
);

CREATE TABLE "tasks" (
    "task_id" BIGSERIAL PRIMARY KEY,
    "task_name" VARCHAR(50) UNIQUE NOT NULL,
    "task_description" VARCHAR(1000),
    "status" VARCHAR(50) NOT NULL,
    "project_id" INTEGER 
        REFERENCES "projects" ("project_id") 
        FOREIGN KEY ON DELETE CASCADE,
    "assigned_user" VARCHAR 
        REFERENCES "users" ("username") 
        FOREIGN KEY ON DELETE SET NULL
);
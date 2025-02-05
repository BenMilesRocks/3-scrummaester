CREATE TABLE "teams" (
    "team_id" BIGSERIAL PRIMARY KEY,
    "team_lead" VARCHAR(50) NOT NULL,
    "team_lead_email" VARCHAR(50) NOT NULL,
);

CREATE TABLE "users" (
    "user_id" BIGSERIAL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "username" VARCHAR(50) UNIQUE NOT NULL,
    "email" VARCHAR(50) UNIQUE NOT NULL,
    "role" VARCHAR(50) NOT NULL,
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
    "project_id" INTEGER REFERENCES 
        "users" ("user_id") 
        FOREIGN KEY ON DELETE SET NULL
);
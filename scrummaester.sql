CREATE TABLE IF NOT EXISTS teams
(
    team_id bigint NOT NULL,
    team_lead character varying(30) NOT NULL,
    team_lead_email character varying(30) NOT NULL,
    CONSTRAINT teams_pkey PRIMARY KEY (team_id)
)

CREATE TABLE IF NOT EXISTS users
(
    id bigint NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(100) NOT NULL,
    email character varying(80) NOT NULL,
    team_role character varying(80) NOT NULL,
    team_id bigint NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT users_username_key UNIQUE (username),
    CONSTRAINT users_team_id_fkey FOREIGN KEY (team_id)
        REFERENCES teams (team_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS projects
(
    project_id bigint NOT NULL,
    project_name character varying(30) NOT NULL,
    project_status character varying(30) NOT NULL,
    team_id bigint NOT NULL,
    CONSTRAINT projects_pkey PRIMARY KEY (project_id),
    CONSTRAINT projects_team_id_fkey FOREIGN KEY (team_id)
        REFERENCES teams (team_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS tasks
(
    task_id bigint NOT NULL,
    task_name character varying(50) NOT NULL,
    task_description character varying(3000) NOT NULL,
    task_status character varying(30) NOT NULL,
    project_id bigint NOT NULL,
    assigned_user bigint NOT NULL,
    CONSTRAINT tasks_pkey PRIMARY KEY (task_id),
    CONSTRAINT tasks_assigned_user_fkey FOREIGN KEY (assigned_user)
        REFERENCES users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT tasks_project_id_fkey FOREIGN KEY (project_id)
        REFERENCES projects (project_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

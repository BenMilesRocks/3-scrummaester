CREATE TABLE IF NOT EXISTS public.teams
(
    team_id bigint NOT NULL DEFAULT nextval('teams_team_id_seq'::regclass),
    team_lead character varying(30) COLLATE pg_catalog."default" NOT NULL,
    team_lead_email character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT teams_pkey PRIMARY KEY (team_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.teams
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.users
(
    id bigint NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    first_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    password character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(80) COLLATE pg_catalog."default" NOT NULL,
    team_role character varying(80) COLLATE pg_catalog."default" NOT NULL,
    team_id bigint NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT users_username_key UNIQUE (username),
    CONSTRAINT users_team_id_fkey FOREIGN KEY (team_id)
        REFERENCES public.teams (team_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.projects
(
    project_id bigint NOT NULL DEFAULT nextval('projects_project_id_seq'::regclass),
    project_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    project_status character varying(30) COLLATE pg_catalog."default" NOT NULL,
    team_id bigint NOT NULL,
    CONSTRAINT projects_pkey PRIMARY KEY (project_id),
    CONSTRAINT projects_team_id_fkey FOREIGN KEY (team_id)
        REFERENCES public.teams (team_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.tasks
(
    task_id bigint NOT NULL DEFAULT nextval('tasks_task_id_seq'::regclass),
    task_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    task_description character varying(3000) COLLATE pg_catalog."default" NOT NULL,
    task_status character varying(30) COLLATE pg_catalog."default" NOT NULL,
    project_id bigint NOT NULL,
    assigned_user bigint NOT NULL,
    CONSTRAINT tasks_pkey PRIMARY KEY (task_id),
    CONSTRAINT tasks_assigned_user_fkey FOREIGN KEY (assigned_user)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT tasks_project_id_fkey FOREIGN KEY (project_id)
        REFERENCES public.projects (project_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
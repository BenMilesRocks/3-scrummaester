PGDMP  ,    &                }            scrummaester    17.2    17.2 &    D           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            E           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            F           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            G           1262    16856    scrummaester    DATABASE     �   CREATE DATABASE scrummaester WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United Kingdom.1252';
    DROP DATABASE scrummaester;
                     postgres    false            �            1259    25467    projects    TABLE     �   CREATE TABLE public.projects (
    project_id bigint NOT NULL,
    project_name character varying(30) NOT NULL,
    project_status character varying(30) NOT NULL,
    team_id bigint NOT NULL
);
    DROP TABLE public.projects;
       public         heap r       postgres    false            �            1259    25466    projects_project_id_seq    SEQUENCE     �   CREATE SEQUENCE public.projects_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.projects_project_id_seq;
       public               postgres    false    222            H           0    0    projects_project_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.projects_project_id_seq OWNED BY public.projects.project_id;
          public               postgres    false    221            �            1259    25479    tasks    TABLE       CREATE TABLE public.tasks (
    task_id bigint NOT NULL,
    task_name character varying(50) NOT NULL,
    task_description character varying(3000) NOT NULL,
    task_status character varying(30) NOT NULL,
    project_id bigint NOT NULL,
    assigned_user bigint NOT NULL
);
    DROP TABLE public.tasks;
       public         heap r       postgres    false            �            1259    25478    tasks_task_id_seq    SEQUENCE     z   CREATE SEQUENCE public.tasks_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.tasks_task_id_seq;
       public               postgres    false    224            I           0    0    tasks_task_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.tasks_task_id_seq OWNED BY public.tasks.task_id;
          public               postgres    false    223            �            1259    25444    teams    TABLE     �   CREATE TABLE public.teams (
    team_id bigint NOT NULL,
    team_lead character varying(30) NOT NULL,
    team_lead_email character varying(30) NOT NULL
);
    DROP TABLE public.teams;
       public         heap r       postgres    false            �            1259    25443    teams_team_id_seq    SEQUENCE     z   CREATE SEQUENCE public.teams_team_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.teams_team_id_seq;
       public               postgres    false    218            J           0    0    teams_team_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.teams_team_id_seq OWNED BY public.teams.team_id;
          public               postgres    false    217            �            1259    25451    users    TABLE     c  CREATE TABLE public.users (
    id bigint NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(100) NOT NULL,
    email character varying(80) NOT NULL,
    team_role character varying(80) NOT NULL,
    team_id bigint NOT NULL
);
    DROP TABLE public.users;
       public         heap r       postgres    false            �            1259    25450    users_id_seq    SEQUENCE     u   CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public               postgres    false    220            K           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public               postgres    false    219            �           2604    25470    projects project_id    DEFAULT     z   ALTER TABLE ONLY public.projects ALTER COLUMN project_id SET DEFAULT nextval('public.projects_project_id_seq'::regclass);
 B   ALTER TABLE public.projects ALTER COLUMN project_id DROP DEFAULT;
       public               postgres    false    221    222    222            �           2604    25482    tasks task_id    DEFAULT     n   ALTER TABLE ONLY public.tasks ALTER COLUMN task_id SET DEFAULT nextval('public.tasks_task_id_seq'::regclass);
 <   ALTER TABLE public.tasks ALTER COLUMN task_id DROP DEFAULT;
       public               postgres    false    223    224    224            �           2604    25447    teams team_id    DEFAULT     n   ALTER TABLE ONLY public.teams ALTER COLUMN team_id SET DEFAULT nextval('public.teams_team_id_seq'::regclass);
 <   ALTER TABLE public.teams ALTER COLUMN team_id DROP DEFAULT;
       public               postgres    false    218    217    218            �           2604    25454    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    219    220    220            ?          0    25467    projects 
   TABLE DATA           U   COPY public.projects (project_id, project_name, project_status, team_id) FROM stdin;
    public               postgres    false    222   �+       A          0    25479    tasks 
   TABLE DATA           m   COPY public.tasks (task_id, task_name, task_description, task_status, project_id, assigned_user) FROM stdin;
    public               postgres    false    224   ,       ;          0    25444    teams 
   TABLE DATA           D   COPY public.teams (team_id, team_lead, team_lead_email) FROM stdin;
    public               postgres    false    218   ;-       =          0    25451    users 
   TABLE DATA           i   COPY public.users (id, first_name, last_name, username, password, email, team_role, team_id) FROM stdin;
    public               postgres    false    220   �-       L           0    0    projects_project_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.projects_project_id_seq', 4, true);
          public               postgres    false    221            M           0    0    tasks_task_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.tasks_task_id_seq', 7, true);
          public               postgres    false    223            N           0    0    teams_team_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.teams_team_id_seq', 3, true);
          public               postgres    false    217            O           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 6, true);
          public               postgres    false    219            �           2606    25472    projects projects_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (project_id);
 @   ALTER TABLE ONLY public.projects DROP CONSTRAINT projects_pkey;
       public                 postgres    false    222            �           2606    25486    tasks tasks_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (task_id);
 :   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_pkey;
       public                 postgres    false    224            �           2606    25449    teams teams_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);
 :   ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_pkey;
       public                 postgres    false    218            �           2606    25460    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public                 postgres    false    220            �           2606    25456    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    220            �           2606    25458    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public                 postgres    false    220            �           2606    25473    projects projects_team_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(team_id);
 H   ALTER TABLE ONLY public.projects DROP CONSTRAINT projects_team_id_fkey;
       public               postgres    false    218    222    4762            �           2606    25492    tasks tasks_assigned_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_assigned_user_fkey FOREIGN KEY (assigned_user) REFERENCES public.users(id);
 H   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_assigned_user_fkey;
       public               postgres    false    224    220    4766            �           2606    25487    tasks tasks_project_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.projects(project_id);
 E   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_project_id_fkey;
       public               postgres    false    222    4770    224            �           2606    25461    users users_team_id_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(team_id);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_team_id_fkey;
       public               postgres    false    220    218    4762            ?   >   x�3�t�,*.Q(��JM.�tL.�,K�4�2�NM��KQ(��8��䤖��pq��qqq ;�&      A     x�U�OO�0���x'vA�6*8"B�ġ�!�����.�j�i��0.q�?���%�,��ICP�sZ3$(�
ީ�9a�XiHQ���Ӓ��m;�`�W>ͨ��b� �Ҕ���c��:����nP���0�y~�-�ј3��5WM��>���j�;'�������5<�Rߠ�Z�ث�F�Ӻ�ԣ��'W����l>H׺3����)�g;�6g������0��?�����s�����Ș:�غ��O؊	�A~�Td�y�e�jȋ�      ;   @   x�3���LTpM)�,���L�K�r3s���s��8��2��3s���8����C:\A� �{      =   �  x�U��r�0���)\��&��E�U�bA��"�(	��������93wq�s��&,hF() h��Q�wO�@�~��M����g�>\��|��	ݲ�U_�E�r��mW3�<�٠��9����5��vAC|�	�zЎ�|�Q=�����Ċ��.���.��W��S��V�].���M�`��n��/�[$< ��`\�,v�Dz�0��Z͜��V�T���"R��6���I�162�Q�JEsc8����K��%�ao(�I��p����u0�F���^��vh�_�؛��K<�/�����u�R�K�0I��#�}�򽫗 7��yZ;�c����4�y��&�2'�؝��7&�cZUș�^����d���ed	�$�Ǫ?LL�f,���_�O�%�[�R�~���4�����     
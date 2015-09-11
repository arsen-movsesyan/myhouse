--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: human_sex; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE human_sex AS ENUM (
    'MALE',
    'FEMALE',
    'PREFER_NOT_TO_SAY'
);


ALTER TYPE human_sex OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO postgres;

--
-- Name: mh_1_account_account; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_account_account (
    id integer NOT NULL,
    acct_name character varying NOT NULL,
    create_date date DEFAULT (now())::date NOT NULL,
    created_by integer NOT NULL,
    login_url character varying NOT NULL,
    acct_type_id integer NOT NULL,
    disabled boolean DEFAULT false NOT NULL,
    disabled_date date,
    time_watch boolean DEFAULT false NOT NULL,
    access_login character varying,
    access_password character varying,
    brief character varying,
    description text
);


ALTER TABLE mh_1_account_account OWNER TO postgres;

--
-- Name: mh_1_account_account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_account_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_account_account_id_seq OWNER TO postgres;

--
-- Name: mh_1_account_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_account_account_id_seq OWNED BY mh_1_account_account.id;


--
-- Name: mh_1_account_attribute_value; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_account_attribute_value (
    account_id integer NOT NULL,
    attribute_id integer NOT NULL,
    value character varying,
    id integer NOT NULL
);


ALTER TABLE mh_1_account_attribute_value OWNER TO postgres;

--
-- Name: mh_1_account_attribute_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_account_attribute_value_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_account_attribute_value_id_seq OWNER TO postgres;

--
-- Name: mh_1_account_attribute_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_account_attribute_value_id_seq OWNED BY mh_1_account_attribute_value.id;


--
-- Name: mh_1_account_payment_history; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_account_payment_history (
    id integer NOT NULL,
    account_id integer NOT NULL,
    payment_date date NOT NULL,
    payment_amount money,
    confirmation_code character varying,
    skip boolean
);


ALTER TABLE mh_1_account_payment_history OWNER TO postgres;

--
-- Name: mh_1_account_payment_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_account_payment_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_account_payment_history_id_seq OWNER TO postgres;

--
-- Name: mh_1_account_payment_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_account_payment_history_id_seq OWNED BY mh_1_account_payment_history.id;


--
-- Name: mh_1_account_time_watch; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_account_time_watch (
    account_id integer NOT NULL,
    auto_payment boolean DEFAULT false NOT NULL,
    due_month_day integer,
    initial_payment_date date,
    month_frequency integer DEFAULT 1,
    disabled boolean DEFAULT false NOT NULL
);


ALTER TABLE mh_1_account_time_watch OWNER TO postgres;

--
-- Name: mh_1_account_user_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_account_user_permission (
    account_id integer NOT NULL,
    user_id integer NOT NULL,
    can_view boolean NOT NULL,
    can_manage boolean NOT NULL,
    can_edit boolean NOT NULL,
    id integer NOT NULL
);


ALTER TABLE mh_1_account_user_permission OWNER TO postgres;

--
-- Name: mh_1_account_user_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_account_user_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_account_user_permission_id_seq OWNER TO postgres;

--
-- Name: mh_1_account_user_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_account_user_permission_id_seq OWNED BY mh_1_account_user_permission.id;


--
-- Name: mh_1_address_basic_address; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_address_basic_address (
    id integer NOT NULL,
    str_line_1 character varying NOT NULL,
    city character varying NOT NULL,
    state character varying,
    zip_code character varying NOT NULL,
    country character varying NOT NULL,
    str_line_2 character varying,
    appt_unit character varying
);


ALTER TABLE mh_1_address_basic_address OWNER TO postgres;

--
-- Name: mh_1_common_basic_address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_common_basic_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_common_basic_address_id_seq OWNER TO postgres;

--
-- Name: mh_1_common_basic_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_common_basic_address_id_seq OWNED BY mh_1_address_basic_address.id;


--
-- Name: mh_1_myhouse_household; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_myhouse_household (
    id integer NOT NULL,
    create_date date DEFAULT (now())::date NOT NULL
);


ALTER TABLE mh_1_myhouse_household OWNER TO postgres;

--
-- Name: mh_1_common_main_house_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_common_main_house_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_common_main_house_id_seq OWNER TO postgres;

--
-- Name: mh_1_common_main_house_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_common_main_house_id_seq OWNED BY mh_1_myhouse_household.id;


--
-- Name: mh_1_config_acctattribute; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_acctattribute (
    id integer NOT NULL,
    attribute_name character varying NOT NULL,
    description text
);


ALTER TABLE mh_1_config_acctattribute OWNER TO postgres;

--
-- Name: mh_1_config_acctattribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_acctattribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_acctattribute_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_acctattribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_acctattribute_id_seq OWNED BY mh_1_config_acctattribute.id;


--
-- Name: mh_1_config_accttype; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_accttype (
    id integer NOT NULL,
    type_name character varying NOT NULL,
    brief character varying NOT NULL,
    description text
);


ALTER TABLE mh_1_config_accttype OWNER TO postgres;

--
-- Name: mh_1_config_accttype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_accttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_accttype_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_accttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_accttype_id_seq OWNED BY mh_1_config_accttype.id;


--
-- Name: mh_1_config_document_attribute; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_document_attribute (
    id integer NOT NULL,
    attribute character varying NOT NULL,
    attribute_format character varying,
    time_watch boolean DEFAULT false
);


ALTER TABLE mh_1_config_document_attribute OWNER TO postgres;

--
-- Name: mh_1_config_document_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_document_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_document_attribute_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_document_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_document_attribute_id_seq OWNED BY mh_1_config_document_attribute.id;


--
-- Name: mh_1_config_document_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_document_type (
    id integer NOT NULL,
    document_type character varying NOT NULL,
    description text
);


ALTER TABLE mh_1_config_document_type OWNER TO postgres;

--
-- Name: mh_1_config_document_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_document_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_document_type_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_document_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_document_type_id_seq OWNED BY mh_1_config_document_type.id;


--
-- Name: mh_1_config_map_doc_attribute; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_map_doc_attribute (
    id integer NOT NULL,
    doc_type_id integer NOT NULL,
    attr_id integer NOT NULL,
    attached boolean NOT NULL
);


ALTER TABLE mh_1_config_map_doc_attribute OWNER TO postgres;

--
-- Name: mh_1_config_map_doc_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_map_doc_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_map_doc_attribute_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_map_doc_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_map_doc_attribute_id_seq OWNED BY mh_1_config_map_doc_attribute.id;


--
-- Name: mh_1_config_vehicle_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_config_vehicle_type (
    id integer NOT NULL,
    vehicle_type character varying NOT NULL,
    description text
);


ALTER TABLE mh_1_config_vehicle_type OWNER TO postgres;

--
-- Name: mh_1_config_vehicle_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_config_vehicle_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_config_vehicle_type_id_seq OWNER TO postgres;

--
-- Name: mh_1_config_vehicle_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_config_vehicle_type_id_seq OWNED BY mh_1_config_vehicle_type.id;


--
-- Name: mh_1_map_household_address; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_map_household_address (
    ba_id integer NOT NULL,
    hh_id integer NOT NULL,
    comment character varying
);


ALTER TABLE mh_1_map_household_address OWNER TO postgres;

--
-- Name: mh_1_map_user_household; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_map_user_household (
    user_id integer NOT NULL,
    household_id integer NOT NULL,
    hh_superuser boolean NOT NULL
);


ALTER TABLE mh_1_map_user_household OWNER TO postgres;

--
-- Name: mh_1_people_document; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_people_document (
    id integer NOT NULL,
    user_id integer NOT NULL,
    document_id integer NOT NULL,
    notes character varying
);


ALTER TABLE mh_1_people_document OWNER TO postgres;

--
-- Name: mh_1_people_document_attribute; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_people_document_attribute (
    id integer NOT NULL,
    doc_map_id integer NOT NULL,
    attr_id integer NOT NULL,
    attr_value character varying
);


ALTER TABLE mh_1_people_document_attribute OWNER TO postgres;

--
-- Name: mh_1_people_document_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_people_document_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_people_document_attribute_id_seq OWNER TO postgres;

--
-- Name: mh_1_people_document_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_people_document_attribute_id_seq OWNED BY mh_1_people_document_attribute.id;


--
-- Name: mh_1_people_document_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_people_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_people_document_id_seq OWNER TO postgres;

--
-- Name: mh_1_people_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_people_document_id_seq OWNED BY mh_1_people_document.id;


--
-- Name: mh_1_people_house_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_people_house_user (
    user_id integer NOT NULL,
    dob date,
    ssn_13 character(3) NOT NULL,
    ssn_45 character(2) NOT NULL,
    ssn_69 character(4) NOT NULL,
    sex human_sex NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    email character varying NOT NULL,
    title character varying,
    suffix character varying,
    created_by integer NOT NULL,
    disabled boolean DEFAULT false NOT NULL,
    disabled_at date
);


ALTER TABLE mh_1_people_house_user OWNER TO postgres;

--
-- Name: mh_1_vehicle_car; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_vehicle_car (
    id integer NOT NULL,
    year_produced character varying,
    make character varying,
    model character varying,
    milage_purchased integer,
    vin character varying NOT NULL,
    milage_registered integer,
    owned_by integer NOT NULL,
    non_operational boolean DEFAULT false NOT NULL,
    license_plate character varying
);


ALTER TABLE mh_1_vehicle_car OWNER TO postgres;

--
-- Name: mh_1_vehicle_car_user_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_vehicle_car_user_permission (
    id integer NOT NULL,
    user_id integer NOT NULL,
    car_id integer NOT NULL,
    can_operate boolean DEFAULT true NOT NULL
);


ALTER TABLE mh_1_vehicle_car_user_permission OWNER TO postgres;

--
-- Name: mh_1_vehicle_car_user_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_vehicle_car_user_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_vehicle_car_user_permission_id_seq OWNER TO postgres;

--
-- Name: mh_1_vehicle_car_user_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_vehicle_car_user_permission_id_seq OWNED BY mh_1_vehicle_car_user_permission.id;


--
-- Name: mh_1_vehicle_generic; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_vehicle_generic (
    id integer NOT NULL,
    type_id integer NOT NULL,
    date_purchased date,
    date_registered date DEFAULT (now())::date NOT NULL
);


ALTER TABLE mh_1_vehicle_generic OWNER TO postgres;

--
-- Name: mh_1_vehicle_generic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_vehicle_generic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_vehicle_generic_id_seq OWNER TO postgres;

--
-- Name: mh_1_vehicle_generic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_vehicle_generic_id_seq OWNED BY mh_1_vehicle_generic.id;


--
-- Name: mh_1_vehicle_renewal; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mh_1_vehicle_renewal (
    id integer NOT NULL,
    vehicle_id integer NOT NULL,
    renewal_date date NOT NULL,
    renewal_amount money
);


ALTER TABLE mh_1_vehicle_renewal OWNER TO postgres;

--
-- Name: mh_1_vehicle_renewal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mh_1_vehicle_renewal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mh_1_vehicle_renewal_id_seq OWNER TO postgres;

--
-- Name: mh_1_vehicle_renewal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mh_1_vehicle_renewal_id_seq OWNED BY mh_1_vehicle_renewal.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_account ALTER COLUMN id SET DEFAULT nextval('mh_1_account_account_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_attribute_value ALTER COLUMN id SET DEFAULT nextval('mh_1_account_attribute_value_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_payment_history ALTER COLUMN id SET DEFAULT nextval('mh_1_account_payment_history_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_user_permission ALTER COLUMN id SET DEFAULT nextval('mh_1_account_user_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_address_basic_address ALTER COLUMN id SET DEFAULT nextval('mh_1_common_basic_address_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_acctattribute ALTER COLUMN id SET DEFAULT nextval('mh_1_config_acctattribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_accttype ALTER COLUMN id SET DEFAULT nextval('mh_1_config_accttype_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_document_attribute ALTER COLUMN id SET DEFAULT nextval('mh_1_config_document_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_document_type ALTER COLUMN id SET DEFAULT nextval('mh_1_config_document_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_map_doc_attribute ALTER COLUMN id SET DEFAULT nextval('mh_1_config_map_doc_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_vehicle_type ALTER COLUMN id SET DEFAULT nextval('mh_1_config_vehicle_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_myhouse_household ALTER COLUMN id SET DEFAULT nextval('mh_1_common_main_house_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document ALTER COLUMN id SET DEFAULT nextval('mh_1_people_document_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document_attribute ALTER COLUMN id SET DEFAULT nextval('mh_1_people_document_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_car_user_permission ALTER COLUMN id SET DEFAULT nextval('mh_1_vehicle_car_user_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_generic ALTER COLUMN id SET DEFAULT nextval('mh_1_vehicle_generic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_renewal ALTER COLUMN id SET DEFAULT nextval('mh_1_vehicle_renewal_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
37	Can add account type	13	add_accounttype
38	Can change account type	13	change_accounttype
39	Can delete account type	13	delete_accounttype
40	Can add account	14	add_account
41	Can change account	14	change_account
42	Can delete account	14	delete_account
43	Can add log entry	15	add_logentry
44	Can change log entry	15	change_logentry
45	Can delete log entry	15	delete_logentry
46	Can add house user	16	add_houseuser
47	Can change house user	16	change_houseuser
48	Can delete house user	16	delete_houseuser
49	Can add account attribute	17	add_accountattribute
50	Can change account attribute	17	change_accountattribute
51	Can delete account attribute	17	delete_accountattribute
52	Can add account user permission	18	add_accountuserpermission
53	Can change account user permission	18	change_accountuserpermission
54	Can delete account user permission	18	delete_accountuserpermission
55	Can add account attribute value	19	add_accountattributevalue
56	Can change account attribute value	19	change_accountattributevalue
57	Can delete account attribute value	19	delete_accountattributevalue
58	Can add account time watch	20	add_accounttimewatch
59	Can change account time watch	20	change_accounttimewatch
60	Can delete account time watch	20	delete_accounttimewatch
61	Can add account payment history	21	add_accountpaymenthistory
62	Can change account payment history	21	change_accountpaymenthistory
63	Can delete account payment history	21	delete_accountpaymenthistory
64	Can add household	22	add_household
65	Can change household	22	change_household
66	Can delete household	22	delete_household
67	Can add map user household	23	add_mapuserhousehold
68	Can change map user household	23	change_mapuserhousehold
69	Can delete map user household	23	delete_mapuserhousehold
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 69, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
37	pbkdf2_sha256$20000$u3iJtiQrxUut$v1Qc0QrgO3eDoWP+NiZB6EvTiMILS0nw0FeMA3uqP3w=	2015-09-03 11:27:04.108294-07	f	petros@test.com			petros@test.com	f	t	2015-09-03 11:06:58.898123-07
39	pbkdf2_sha256$20000$TjpBnjT9TIHn$KUuNvMG2JsGCy36XQQWMCjDl4eVjABvjKmTqEN+KVog=	\N	f	right@test.com			right@test.com	f	f	2015-09-04 16:15:10.130961-07
21	pbkdf2_sha256$20000$S2Z4V1zJsMqg$u3oWDghu1FXRZAyp94iH+TiTntxOrMmpiVlk65v0kkw=	2015-09-11 13:26:29.809756-07	t	arsen			arsen.movsesyan@gmail.com	t	t	2015-09-01 11:59:37.014824-07
24	pbkdf2_sha256$20000$b6w0DAO0tH3w$zk+PMhJw8lEhV8tXcKOEDJLUTvh2JeKNb78CtR009uU=	2015-09-11 13:30:03.691334-07	f	arsen@test.com			arsen@test.com	f	t	2015-09-01 12:49:17.237276-07
33	pbkdf2_sha256$20000$jcaREeIuVt4y$e64SzbTPcyVhh6hn3PQB6+e5vmGz7llpGukrp4ThMOs=	2015-09-02 10:12:42.436486-07	f	poghos@test.com			poghos@test.com	f	t	2015-09-01 14:34:07.814296-07
38	pbkdf2_sha256$20000$HCXVepgwte7V$hlVtZqr01OIS9npRvw2obOdl9BS9LtM31HzQoNnC6ak=	\N	f	martiros@test.com			martiros@test.com	f	f	2015-09-03 11:25:56.02487-07
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 40, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2015-09-01 12:00:27.96887-07	13	arsen@test.com	3		3	21
2	2015-09-01 12:00:27.973184-07	20	poghos@petros.com	3		3	21
3	2015-09-01 12:43:14.487197-07	22	arsen@test.com	3		3	21
4	2015-09-01 12:48:14.562554-07	23	arsen@test.com	3		3	21
5	2015-09-11 13:29:03.953747-07	8	DocumentType object	3		25	21
6	2015-09-11 13:29:03.958378-07	7	DocumentType object	3		25	21
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 6, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	auth	user
4	contenttypes	contenttype
5	sessions	session
13	config	accounttype
14	account	account
15	admin	logentry
16	people	houseuser
17	config	accountattribute
18	account	accountuserpermission
19	account	accountattributevalue
20	account	accounttimewatch
21	account	accountpaymenthistory
22	people	household
23	people	mapuserhousehold
24	config	vehicletype
25	config	documenttype
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 25, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2015-08-18 17:39:46.94055-07
2	contenttypes	0002_remove_content_type_name	2015-08-18 17:39:46.956032-07
3	auth	0001_initial	2015-08-18 17:39:47.051247-07
4	auth	0002_alter_permission_name_max_length	2015-08-18 17:39:47.073882-07
5	auth	0003_alter_user_email_max_length	2015-08-18 17:39:47.095258-07
6	auth	0004_alter_user_username_opts	2015-08-18 17:39:47.113825-07
7	auth	0005_alter_user_last_login_null	2015-08-18 17:39:47.134866-07
8	auth	0006_require_contenttypes_0002	2015-08-18 17:39:47.138137-07
9	sessions	0001_initial	2015-08-18 17:39:47.16039-07
10	account	0001_initial	2015-08-19 15:25:13.611464-07
11	account	0002_houseuser_mainaccount	2015-08-19 16:54:57.540219-07
12	account	0003_auto_20150820_1138	2015-08-20 11:38:14.609585-07
13	account	0004_household	2015-08-24 12:00:31.397876-07
14	account	0005_mapuserhousehold	2015-08-24 12:26:33.317717-07
15	config	0001_initial	2015-08-27 13:27:00.553158-07
16	account	0006_account	2015-08-27 15:16:22.331634-07
17	admin	0001_initial	2015-09-01 11:57:53.037921-07
18	config	0002_accountattribute	2015-09-01 11:57:53.050338-07
19	people	0001_initial	2015-09-01 11:57:53.073054-07
20	people	0002_auto_20150901_1242	2015-09-01 12:42:49.710651-07
21	account	0007_accountuserpermission	2015-09-01 15:08:05.557119-07
22	account	0008_accountattributevalue_accountpaymenthistory_accounttimewatch	2015-09-02 18:27:25.866498-07
23	people	0003_household_mapuserhousehold	2015-09-02 18:27:25.902716-07
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 23, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
iom43ne134ez26y6yyh0xyucmaoe9dxo	NTEwMGZiNzJiNzE2ZDg1OGE1ZjFkMjFmOTA3ZDVjOWZiMjVjMTc5Mjp7ImhvdXNlaG9sZCI6NCwiX2F1dGhfdXNlcl9oYXNoIjoiNTc3MzQ1OWM5MDE0NDliN2E3ZjIzMDhkMjU2ODkyNWYwMGQ5NTZjZCIsIl9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2015-09-11 11:15:05.97394-07
rrpe1tab4nom1894wu6kcttykn5ix71s	YzM1ODViZjI4NjhkMWMwNTZjMjk0NDU4ZjJlZGM4MjQwNWE2NzJlODp7InVzZXJfaWQiOjI0LCJfYXV0aF91c2VyX2lkIjoiMjQiLCJob3VzZWhvbGRfaWQiOjYsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmVhMmYxYzIzMzJjNjEzODFkNTdjOWQ1NTU5ZDczYmJmMDRkMjBiYyIsInVzZXJfbmFtZSI6IkFyc2VuIn0=	2015-09-25 13:30:03.700929-07
\.


--
-- Data for Name: mh_1_account_account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_account (id, acct_name, create_date, created_by, login_url, acct_type_id, disabled, disabled_date, time_watch, access_login, access_password, brief, description) FROM stdin;
11	Google	2015-09-02	24	http://www.google.com	4	f	\N	f	aaa	sss		False
12	Yahoo	2015-09-03	24	http://www.yahoo.com	2	f	\N	f	aaa	bbb		False
13	PGE	2015-09-03	24	http://www.pge.com	1	f	\N	t	aaa	bbb	Electrical Utility	
14	Comcast	2015-09-03	24	http://www.comcast.com	1	f	\N	t	aaa	bbb	Telecom	
15	Main Bank	2015-09-03	24	http://www.chase.com	1	f	\N	t	aaa	bbb	Credit	
16	Some Credit	2015-09-03	24	http://www.credit.com	1	f	\N	t	aaa	bbb	Another Credit	
17	Mortgage	2015-09-03	24	http://www.chase.com	1	f	\N	t	aaa	bbb	Mortgage	
18	Another Credit	2015-09-04	24	http://www.capitalone.com	1	f	\N	t	aaa	bbb	Yet another credit	
\.


--
-- Name: mh_1_account_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_account_id_seq', 18, true);


--
-- Data for Name: mh_1_account_attribute_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_attribute_value (account_id, attribute_id, value, id) FROM stdin;
\.


--
-- Name: mh_1_account_attribute_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_attribute_value_id_seq', 3, true);


--
-- Data for Name: mh_1_account_payment_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_payment_history (id, account_id, payment_date, payment_amount, confirmation_code, skip) FROM stdin;
2	14	2015-09-04	$10.00	lalala	\N
3	15	2015-09-04	$45.00	fff	\N
4	16	2015-09-11	$23.00	ABCDE	\N
5	17	2015-09-11	$0.00	Void Acknowledged	t
\.


--
-- Name: mh_1_account_payment_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_payment_history_id_seq', 5, true);


--
-- Data for Name: mh_1_account_time_watch; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_time_watch (account_id, auto_payment, due_month_day, initial_payment_date, month_frequency, disabled) FROM stdin;
14	f	5	\N	1	f
15	f	10	\N	1	f
16	f	15	\N	1	f
17	f	20	\N	1	f
18	t	4	\N	1	f
13	f	1	\N	1	f
\.


--
-- Data for Name: mh_1_account_user_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_user_permission (account_id, user_id, can_view, can_manage, can_edit, id) FROM stdin;
12	33	t	t	f	7
12	37	t	t	f	8
12	38	t	t	f	9
11	33	t	f	t	3
11	37	t	t	t	5
11	38	f	f	t	6
13	33	t	t	f	10
13	37	t	t	f	11
13	38	t	t	f	12
14	33	t	t	f	13
14	37	t	t	f	14
14	38	t	t	f	15
15	33	t	t	f	16
15	37	t	t	f	17
15	38	t	t	f	18
16	33	t	t	f	19
16	37	t	t	f	20
16	38	t	t	f	21
17	33	t	t	f	22
17	37	t	t	f	23
17	38	t	t	f	24
18	33	t	t	f	25
18	37	t	t	f	26
18	38	t	t	f	27
11	39	t	t	f	28
12	39	t	t	f	29
13	39	t	f	f	30
14	39	t	t	f	31
15	39	t	t	t	32
16	39	f	t	f	33
17	39	t	f	f	34
18	39	t	t	t	35
\.


--
-- Name: mh_1_account_user_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_user_permission_id_seq', 43, true);


--
-- Data for Name: mh_1_address_basic_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_address_basic_address (id, str_line_1, city, state, zip_code, country, str_line_2, appt_unit) FROM stdin;
5	5450 Cahalan Ave	San Jose	CA	95123	USA		
\.


--
-- Name: mh_1_common_basic_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_common_basic_address_id_seq', 5, true);


--
-- Name: mh_1_common_main_house_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_common_main_house_id_seq', 6, true);


--
-- Data for Name: mh_1_config_acctattribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_acctattribute (id, attribute_name, description) FROM stdin;
1	Account Number	For basic banking account numbers
2	Routing Number	Banking Routing numbers
3	Confirmation	For general purpose confirmations
4	Serial Number	For Test purposes
\.


--
-- Name: mh_1_config_acctattribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_acctattribute_id_seq', 4, true);


--
-- Data for Name: mh_1_config_accttype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_accttype (id, type_name, brief, description) FROM stdin;
1	Financial	Stores financial info	For all financial account types including banks, online stores and services required credit or debit card
2	Social	For social networks	Accounts like "Facebook", "LinkedIn", etc.
3	Basic	General Purpose accounts	
4	Other	For all unclassified accounts	
\.


--
-- Name: mh_1_config_accttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_accttype_id_seq', 4, true);


--
-- Data for Name: mh_1_config_document_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_document_attribute (id, attribute, attribute_format, time_watch) FROM stdin;
5	Issue Date	DATE	f
7	Serial Number	STRING	f
6	Valid Till	DATE	t
8	Country of Residence	STRING	f
9	Issued State	STRING	f
\.


--
-- Name: mh_1_config_document_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_document_attribute_id_seq', 9, true);


--
-- Data for Name: mh_1_config_document_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_document_type (id, document_type, description) FROM stdin;
9	Passport	Generic Document Type
10	Driver License	US person ID
\.


--
-- Name: mh_1_config_document_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_document_type_id_seq', 10, true);


--
-- Data for Name: mh_1_config_map_doc_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_map_doc_attribute (id, doc_type_id, attr_id, attached) FROM stdin;
10	9	5	t
11	9	7	t
12	9	6	t
13	9	8	t
14	9	9	f
15	10	5	t
16	10	7	t
17	10	6	t
18	10	8	f
19	10	9	t
\.


--
-- Name: mh_1_config_map_doc_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_map_doc_attribute_id_seq', 19, true);


--
-- Data for Name: mh_1_config_vehicle_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_vehicle_type (id, vehicle_type, description) FROM stdin;
1	Car	Generic vehicle type car
\.


--
-- Name: mh_1_config_vehicle_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_vehicle_type_id_seq', 1, true);


--
-- Data for Name: mh_1_map_household_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_map_household_address (ba_id, hh_id, comment) FROM stdin;
\.


--
-- Data for Name: mh_1_map_user_household; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_map_user_household (user_id, household_id, hh_superuser) FROM stdin;
24	6	t
33	6	f
37	6	f
38	6	f
39	6	f
\.


--
-- Data for Name: mh_1_myhouse_household; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_myhouse_household (id, create_date) FROM stdin;
6	2015-09-01
\.


--
-- Data for Name: mh_1_people_document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_document (id, user_id, document_id, notes) FROM stdin;
4	24	9	
5	24	10	
\.


--
-- Data for Name: mh_1_people_document_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_document_attribute (id, doc_map_id, attr_id, attr_value) FROM stdin;
7	4	6	2015-12-31
8	4	5	2000-01-01
9	4	7	ABCDE12345
10	4	8	USA
11	5	6	2016-05-01
12	5	5	2008-05-01
13	5	9	CALIFORNIA
14	5	7	12345ABCDE
\.


--
-- Name: mh_1_people_document_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_people_document_attribute_id_seq', 14, true);


--
-- Name: mh_1_people_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_people_document_id_seq', 5, true);


--
-- Data for Name: mh_1_people_house_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_house_user (user_id, dob, ssn_13, ssn_45, ssn_69, sex, first_name, last_name, email, title, suffix, created_by, disabled, disabled_at) FROM stdin;
24	1970-02-21	123	45	6789	MALE	Arsen	Movsesyan	arsen@test.com	MR		24	f	\N
33	1990-01-01	123	45	6789	MALE	Poghos	Petrosyan	poghos@test.com	MR		24	f	\N
37	1997-01-01	123	45	6789	MALE	Petros	Poghosyan	petros@test.com	MR		24	f	\N
38	1970-04-04	123	45	6789	MALE	Martiros	Martirosyan	martiros@test.com	MR		24	f	\N
39	1990-04-04	123	45	6789	FEMALE	Always	Right	right@test.com	MRS		24	f	\N
\.


--
-- Data for Name: mh_1_vehicle_car; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_car (id, year_produced, make, model, milage_purchased, vin, milage_registered, owned_by, non_operational, license_plate) FROM stdin;
5	2008	Nissan	Altima	830	9876543ABCDEFG	64000	24	f	6FMM197
4	2004	Volkswagen	Passat	99000	12345678ABCDEFGH	156000	24	f	6FAE962
\.


--
-- Data for Name: mh_1_vehicle_car_user_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_car_user_permission (id, user_id, car_id, can_operate) FROM stdin;
5	33	5	t
6	37	5	t
7	38	5	t
8	39	5	t
1	33	4	t
2	37	4	f
3	38	4	f
4	39	4	t
\.


--
-- Name: mh_1_vehicle_car_user_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_car_user_permission_id_seq', 8, true);


--
-- Data for Name: mh_1_vehicle_generic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_generic (id, type_id, date_purchased, date_registered) FROM stdin;
4	1	2009-01-01	2015-09-05
5	1	2008-06-25	2015-09-05
\.


--
-- Name: mh_1_vehicle_generic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_generic_id_seq', 5, true);


--
-- Data for Name: mh_1_vehicle_renewal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_renewal (id, vehicle_id, renewal_date, renewal_amount) FROM stdin;
1	5	2015-09-05	$108.00
2	4	2015-01-01	$132.00
\.


--
-- Name: mh_1_vehicle_renewal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_renewal_id_seq', 2, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: mh_1_account_account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_account_account
    ADD CONSTRAINT mh_1_account_account_pkey PRIMARY KEY (id);


--
-- Name: mh_1_account_attribute_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_account_attribute_value
    ADD CONSTRAINT mh_1_account_attribute_value_pkey PRIMARY KEY (id);


--
-- Name: mh_1_account_map_user_household_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_map_user_household
    ADD CONSTRAINT mh_1_account_map_user_household_pkey PRIMARY KEY (user_id);


--
-- Name: mh_1_account_payment_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_account_payment_history
    ADD CONSTRAINT mh_1_account_payment_history_pkey PRIMARY KEY (id);


--
-- Name: mh_1_account_time_watch_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_account_time_watch
    ADD CONSTRAINT mh_1_account_time_watch_pkey PRIMARY KEY (account_id);


--
-- Name: mh_1_account_user_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_account_user_permission
    ADD CONSTRAINT mh_1_account_user_permission_pkey PRIMARY KEY (id);


--
-- Name: mh_1_acct_house_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_people_house_user
    ADD CONSTRAINT mh_1_acct_house_user_pkey PRIMARY KEY (user_id);


--
-- Name: mh_1_common_basic_address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_address_basic_address
    ADD CONSTRAINT mh_1_common_basic_address_pkey PRIMARY KEY (id);


--
-- Name: mh_1_common_main_house_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_myhouse_household
    ADD CONSTRAINT mh_1_common_main_house_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_acctattribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_acctattribute
    ADD CONSTRAINT mh_1_config_acctattribute_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_accttype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_accttype
    ADD CONSTRAINT mh_1_config_accttype_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_document_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_document_attribute
    ADD CONSTRAINT mh_1_config_document_attribute_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_document_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_document_type
    ADD CONSTRAINT mh_1_config_document_type_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_map_doc_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_map_doc_attribute
    ADD CONSTRAINT mh_1_config_map_doc_attribute_pkey PRIMARY KEY (id);


--
-- Name: mh_1_config_vehicle_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_config_vehicle_type
    ADD CONSTRAINT mh_1_config_vehicle_type_pkey PRIMARY KEY (id);


--
-- Name: mh_1_map_household_address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_map_household_address
    ADD CONSTRAINT mh_1_map_household_address_pkey PRIMARY KEY (ba_id);


--
-- Name: mh_1_people_document_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_people_document_attribute
    ADD CONSTRAINT mh_1_people_document_attribute_pkey PRIMARY KEY (id);


--
-- Name: mh_1_people_document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_people_document
    ADD CONSTRAINT mh_1_people_document_pkey PRIMARY KEY (id);


--
-- Name: mh_1_vehicle_car_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_vehicle_car
    ADD CONSTRAINT mh_1_vehicle_car_pkey PRIMARY KEY (id);


--
-- Name: mh_1_vehicle_car_user_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_vehicle_car_user_permission
    ADD CONSTRAINT mh_1_vehicle_car_user_permission_pkey PRIMARY KEY (id);


--
-- Name: mh_1_vehicle_generic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_vehicle_generic
    ADD CONSTRAINT mh_1_vehicle_generic_pkey PRIMARY KEY (id);


--
-- Name: mh_1_vehicle_renewal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mh_1_vehicle_renewal
    ADD CONSTRAINT mh_1_vehicle_renewal_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mh_1_account_account_acct_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_account
    ADD CONSTRAINT mh_1_account_account_acct_type_id_fkey FOREIGN KEY (acct_type_id) REFERENCES mh_1_config_accttype(id);


--
-- Name: mh_1_account_account_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_account
    ADD CONSTRAINT mh_1_account_account_created_by_fkey FOREIGN KEY (created_by) REFERENCES mh_1_people_house_user(user_id) ON DELETE CASCADE;


--
-- Name: mh_1_account_attribute_value_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_attribute_value
    ADD CONSTRAINT mh_1_account_attribute_value_account_id_fkey FOREIGN KEY (account_id) REFERENCES mh_1_account_account(id);


--
-- Name: mh_1_account_attribute_value_attribute_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_attribute_value
    ADD CONSTRAINT mh_1_account_attribute_value_attribute_id_fkey FOREIGN KEY (attribute_id) REFERENCES mh_1_config_acctattribute(id);


--
-- Name: mh_1_account_map_user_household_household_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_map_user_household
    ADD CONSTRAINT mh_1_account_map_user_household_household_id_fkey FOREIGN KEY (household_id) REFERENCES mh_1_myhouse_household(id) ON DELETE CASCADE;


--
-- Name: mh_1_account_map_user_household_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_map_user_household
    ADD CONSTRAINT mh_1_account_map_user_household_user_id_fkey FOREIGN KEY (user_id) REFERENCES mh_1_people_house_user(user_id) ON DELETE CASCADE;


--
-- Name: mh_1_account_payment_history_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_payment_history
    ADD CONSTRAINT mh_1_account_payment_history_account_id_fkey FOREIGN KEY (account_id) REFERENCES mh_1_account_time_watch(account_id);


--
-- Name: mh_1_account_time_watch_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_time_watch
    ADD CONSTRAINT mh_1_account_time_watch_account_id_fkey FOREIGN KEY (account_id) REFERENCES mh_1_account_account(id);


--
-- Name: mh_1_account_user_permission_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_user_permission
    ADD CONSTRAINT mh_1_account_user_permission_account_id_fkey FOREIGN KEY (account_id) REFERENCES mh_1_account_account(id);


--
-- Name: mh_1_account_user_permission_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_account_user_permission
    ADD CONSTRAINT mh_1_account_user_permission_user_id_fkey FOREIGN KEY (user_id) REFERENCES mh_1_people_house_user(user_id);


--
-- Name: mh_1_acct_house_user_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_house_user
    ADD CONSTRAINT mh_1_acct_house_user_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: mh_1_config_map_doc_attribute_attr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_map_doc_attribute
    ADD CONSTRAINT mh_1_config_map_doc_attribute_attr_id_fkey FOREIGN KEY (attr_id) REFERENCES mh_1_config_document_attribute(id);


--
-- Name: mh_1_config_map_doc_attribute_doc_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_config_map_doc_attribute
    ADD CONSTRAINT mh_1_config_map_doc_attribute_doc_type_id_fkey FOREIGN KEY (doc_type_id) REFERENCES mh_1_config_document_type(id);


--
-- Name: mh_1_map_household_address_ba_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_map_household_address
    ADD CONSTRAINT mh_1_map_household_address_ba_id_fkey FOREIGN KEY (ba_id) REFERENCES mh_1_address_basic_address(id);


--
-- Name: mh_1_map_household_address_hh_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_map_household_address
    ADD CONSTRAINT mh_1_map_household_address_hh_id_fkey FOREIGN KEY (hh_id) REFERENCES mh_1_myhouse_household(id);


--
-- Name: mh_1_people_document_attribute_attr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document_attribute
    ADD CONSTRAINT mh_1_people_document_attribute_attr_id_fkey FOREIGN KEY (attr_id) REFERENCES mh_1_config_document_attribute(id);


--
-- Name: mh_1_people_document_attribute_doc_map_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document_attribute
    ADD CONSTRAINT mh_1_people_document_attribute_doc_map_id_fkey FOREIGN KEY (doc_map_id) REFERENCES mh_1_people_document(id);


--
-- Name: mh_1_people_document_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document
    ADD CONSTRAINT mh_1_people_document_document_id_fkey FOREIGN KEY (document_id) REFERENCES mh_1_config_document_type(id);


--
-- Name: mh_1_people_document_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_people_document
    ADD CONSTRAINT mh_1_people_document_user_id_fkey FOREIGN KEY (user_id) REFERENCES mh_1_people_house_user(user_id);


--
-- Name: mh_1_vehicle_car_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_car
    ADD CONSTRAINT mh_1_vehicle_car_id_fkey FOREIGN KEY (id) REFERENCES mh_1_vehicle_generic(id);


--
-- Name: mh_1_vehicle_car_ovned_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_car
    ADD CONSTRAINT mh_1_vehicle_car_ovned_by_fkey FOREIGN KEY (owned_by) REFERENCES mh_1_people_house_user(user_id);


--
-- Name: mh_1_vehicle_car_user_permission_car_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_car_user_permission
    ADD CONSTRAINT mh_1_vehicle_car_user_permission_car_id_fkey FOREIGN KEY (car_id) REFERENCES mh_1_vehicle_car(id);


--
-- Name: mh_1_vehicle_car_user_permission_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_car_user_permission
    ADD CONSTRAINT mh_1_vehicle_car_user_permission_user_id_fkey FOREIGN KEY (user_id) REFERENCES mh_1_people_house_user(user_id);


--
-- Name: mh_1_vehicle_generic_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_generic
    ADD CONSTRAINT mh_1_vehicle_generic_type_id_fkey FOREIGN KEY (type_id) REFERENCES mh_1_config_vehicle_type(id);


--
-- Name: mh_1_vehicle_renewal_vehicle_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mh_1_vehicle_renewal
    ADD CONSTRAINT mh_1_vehicle_renewal_vehicle_id_fkey FOREIGN KEY (vehicle_id) REFERENCES mh_1_vehicle_generic(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


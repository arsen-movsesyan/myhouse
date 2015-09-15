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
-- Data for Name: mh_1_account_account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_account (id, acct_name, create_date, created_by, login_url, acct_type_id, disabled, disabled_date, time_watch, access_login, access_password, brief, description) FROM stdin;
\.


--
-- Name: mh_1_account_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_account_id_seq', 1, false);


--
-- Data for Name: mh_1_account_attribute_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_attribute_value (account_id, attribute_id, value, id) FROM stdin;
\.


--
-- Name: mh_1_account_attribute_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_attribute_value_id_seq', 1, false);


--
-- Data for Name: mh_1_account_payment_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_payment_history (id, account_id, payment_date, payment_amount, confirmation_code, skip) FROM stdin;
\.


--
-- Name: mh_1_account_payment_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_payment_history_id_seq', 1, false);


--
-- Data for Name: mh_1_account_time_watch; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_time_watch (account_id, auto_payment, due_month_day, initial_payment_date, month_frequency, disabled) FROM stdin;
\.


--
-- Data for Name: mh_1_account_user_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_account_user_permission (account_id, user_id, can_view, can_manage, can_edit, id) FROM stdin;
\.


--
-- Name: mh_1_account_user_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_account_user_permission_id_seq', 1, false);


--
-- Data for Name: mh_1_address_basic_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_address_basic_address (id, str_line_1, city, state, zip_code, country, str_line_2, appt_unit) FROM stdin;
\.


--
-- Name: mh_1_common_basic_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_common_basic_address_id_seq', 1, false);


--
-- Name: mh_1_common_main_house_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_common_main_house_id_seq', 1, false);


--
-- Data for Name: mh_1_config_acctattribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_acctattribute (id, attribute_name, description) FROM stdin;
\.


--
-- Name: mh_1_config_acctattribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_acctattribute_id_seq', 1, false);


--
-- Data for Name: mh_1_config_accttype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_accttype (id, type_name, brief, description) FROM stdin;
\.


--
-- Name: mh_1_config_accttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_accttype_id_seq', 1, false);


--
-- Data for Name: mh_1_config_document_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_document_attribute (id, attribute, attribute_format, time_watch) FROM stdin;
\.


--
-- Name: mh_1_config_document_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_document_attribute_id_seq', 1, false);


--
-- Data for Name: mh_1_config_document_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_document_type (id, document_type, description) FROM stdin;
\.


--
-- Name: mh_1_config_document_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_document_type_id_seq', 1, false);


--
-- Data for Name: mh_1_config_map_doc_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_map_doc_attribute (id, doc_type_id, attr_id, attached) FROM stdin;
\.


--
-- Name: mh_1_config_map_doc_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_map_doc_attribute_id_seq', 1, false);


--
-- Data for Name: mh_1_config_vehicle_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_config_vehicle_type (id, vehicle_type, description) FROM stdin;
\.


--
-- Name: mh_1_config_vehicle_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_config_vehicle_type_id_seq', 1, false);


--
-- Data for Name: mh_1_map_household_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_map_household_address (ba_id, hh_id, comment) FROM stdin;
\.


--
-- Data for Name: mh_1_map_user_household; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_map_user_household (user_id, household_id, hh_superuser) FROM stdin;
\.


--
-- Data for Name: mh_1_myhouse_household; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_myhouse_household (id, create_date) FROM stdin;
\.


--
-- Data for Name: mh_1_people_document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_document (id, user_id, document_id, notes) FROM stdin;
\.


--
-- Data for Name: mh_1_people_document_attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_document_attribute (id, doc_map_id, attr_id, attr_value) FROM stdin;
\.


--
-- Name: mh_1_people_document_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_people_document_attribute_id_seq', 1, false);


--
-- Name: mh_1_people_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_people_document_id_seq', 1, false);


--
-- Data for Name: mh_1_people_house_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_people_house_user (user_id, dob, ssn_13, ssn_45, ssn_69, sex, first_name, last_name, email, title, suffix, created_by, disabled, disabled_at) FROM stdin;
\.


--
-- Data for Name: mh_1_vehicle_car; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_car (id, year_produced, make, model, milage_purchased, vin, milage_registered, owned_by, non_operational, license_plate) FROM stdin;
\.


--
-- Data for Name: mh_1_vehicle_car_user_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_car_user_permission (id, user_id, car_id, can_operate) FROM stdin;
\.


--
-- Name: mh_1_vehicle_car_user_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_car_user_permission_id_seq', 1, false);


--
-- Data for Name: mh_1_vehicle_generic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_generic (id, type_id, date_purchased, date_registered) FROM stdin;
\.


--
-- Name: mh_1_vehicle_generic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_generic_id_seq', 1, false);


--
-- Data for Name: mh_1_vehicle_renewal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mh_1_vehicle_renewal (id, vehicle_id, renewal_date, renewal_amount) FROM stdin;
\.


--
-- Name: mh_1_vehicle_renewal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mh_1_vehicle_renewal_id_seq', 1, false);


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


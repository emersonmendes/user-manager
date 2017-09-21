-- Author: Emerson Mendes

CREATE TABLE usergroup
(
  id bigint NOT NULL,
  name varchar NOT NULL,
  CONSTRAINT pk_usergroup PRIMARY KEY (id)
);

CREATE TABLE "user"
(
  id bigint NOT NULL,
  name varchar NOT NULL,
  username varchar NOT NULL,
  password varchar NOT NULL,
  fk_usergroup integer,
  CONSTRAINT pk_user PRIMARY KEY (id),
  CONSTRAINT fk_usergroup FOREIGN KEY (fk_usergroup) REFERENCES usergroup (id)
);

CREATE SEQUENCE usergroup_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE user_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE SCHEMA swiss_tournament;

CREATE TABLE swiss_tournament.participants(
             id serial PRIMARY KEY NOT NULL,
             full_name text NOT NULL,
             wins int default 0,
             matches int default 0
             );


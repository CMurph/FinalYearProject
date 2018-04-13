-- Table: public.location_names

-- DROP TABLE public.location_names;

CREATE TABLE public.location_names
(
  name character varying NOT NULL,
  CONSTRAINT location_names_pkey PRIMARY KEY (name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.location_names
  OWNER TO ciaran;



-- Table: public.locations

-- DROP TABLE public.locations;

CREATE TABLE public.locations
(
  location_id integer NOT NULL,
  geom geometry(Geometry,4326),
  name character varying,
  id character varying,
  alt_name character varying,
  bicycle character varying,
  highway character varying,
  surface character varying,
  lit character varying,
  access character varying,
  maxspeed character varying,
  maxheight character varying,
  oneway character varying,
  width character varying,
  maxweight character varying,
  maxwidth character varying,
  CONSTRAINT roads_stuff_pkey PRIMARY KEY (location_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.locations
  OWNER TO ciaran;



-- Table: public.collisions

-- DROP TABLE public.collisions;

CREATE TABLE public.collisions
(
  collision_id integer NOT NULL DEFAULT nextval('collisions_collision_id_seq'::regclass),
  "timestamp" timestamp without time zone,
  location_name character varying(100),
  CONSTRAINT collisions_pkey PRIMARY KEY (collision_id),
  CONSTRAINT collisions_location_name_fkey FOREIGN KEY (location_name)
      REFERENCES public.location_names (name) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.collisions
  OWNER TO ciaran;

-- Trigger: trigger_collision_locations on public.collisions

-- DROP TRIGGER trigger_collision_locations ON public.collisions;

CREATE TRIGGER trigger_collision_locations
  AFTER INSERT
  ON public.collisions
  FOR EACH ROW
  EXECUTE PROCEDURE public.safe_road_data();


-- Table: public.tweets

-- DROP TABLE public.tweets;

CREATE TABLE public.tweets
(
  tweet_id bigint NOT NULL DEFAULT nextval('tweets_tweet_id_seq'::regclass),
  collision_id integer,
  user_id bigint,
  text character varying(281),
  CONSTRAINT tweets_pkey PRIMARY KEY (tweet_id),
  CONSTRAINT tweets_collision_id_fkey FOREIGN KEY (collision_id)
      REFERENCES public.collisions (collision_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.tweets
  OWNER TO ciaran;

-- Trigger: trigger_tweet_collisions on public.tweets

-- DROP TRIGGER trigger_tweet_collisions ON public.tweets;

CREATE TRIGGER trigger_tweet_collisions
  AFTER INSERT
  ON public.tweets
  FOR EACH ROW
  EXECUTE PROCEDURE public.tweet_data();


-- Table: public.map_data

-- DROP TABLE public.map_data;

CREATE TABLE public.map_data
(
  location_id integer NOT NULL,
  geom geometry(Geometry,4326),
  name character varying,
  id character varying,
  alt_name character varying,
  bicycle character varying,
  highway character varying,
  surface character varying,
  lit character varying,
  access character varying,
  maxspeed character varying,
  maxheight character varying,
  oneway character varying,
  width character varying,
  maxweight character varying,
  maxwidth character varying,
  collisions integer DEFAULT 0,
  tweets integer DEFAULT 0,
  CONSTRAINT map_data_pkey PRIMARY KEY (location_id),
  CONSTRAINT map_data_location_id_fkey FOREIGN KEY (location_id)
      REFERENCES public.locations (location_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.map_data
  OWNER TO ciaran;







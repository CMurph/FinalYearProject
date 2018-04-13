
CREATE OR REPLACE FUNCTION SAFE_ROAD_DATA() RETURNS trigger as $SAFE_ROAD_DATA$
 DECLARE collision_quantity INTEGER; location_check INTEGER;
 BEGIN

    SELECT count(*)
    INTO collision_quantity
    FROM collisions where lower(location_name) = lower(new.location_name);

    SELECT count(*)
    INTO location_check
    FROM map_data
    WHERE lower(map_data.name) = lower(new.location_name);

    IF (location_check = 0) THEN
	INSERT INTO map_data (location_id, geom, name, id, alt_name, bicycle, highway, surface,
                        lit, access, maxspeed, maxheight, oneway, width, maxweight, maxwidth)
    select * from locations where lower(locations.name) = lower(new.location_name);
	end IF;
   RAISE NOTICE 'locationcheck is currently %', location_check;
   RAISE NOTICE 'collision is currently %', collision_quantity;
   RAISE NOTICE 'New.loc is %', new.location_name;


	UPDATE map_data
	SET
	collisions = collision_quantity
    where(
          lower(name) = new.location_name
         );

   RETURN NULL;
  END;
$SAFE_ROAD_DATA$ LANGUAGE plpgsql;



CREATE TRIGGER TRIGGER_COLLISION_LOCATIONS after
  INSERT ON collisions FOR EACH row EXECUTE PROCEDURE SAFE_ROAD_DATA();
    --get quantity of tweets and collisions for a location



/* END OF COLLISION TRIGGER






 */



    --get quantity of tweets and collisions for a location
CREATE OR REPLACE FUNCTION TWEET_DATA() RETURNS trigger as $TWEET_DATA$
 DECLARE tweet_quantity INTEGER; location VARCHAR(100);
 BEGIN

    SELECT count(*)
    INTO tweet_quantity
    FROM tweets join collisions using (collision_id)
    where collisions.collision_id = new.collision_id;


   SELECT location_name
     INTO location
   FROM tweets join collisions using (collision_id)
   where collisions.collision_id = new.collision_id;


	UPDATE map_data
	SET tweets = tweet_quantity
	where (lower(name) = lower(location));
    RAISE NOTICE 'location is currently %', location;
    RAISE NOTICE 'Tweet Quantity is currently %', tweet_quantity;
    RAISE NOTICE 'collision is currently %', new.collision_id;
   RETURN NULL;
  END;
$TWEET_DATA$ LANGUAGE plpgsql;

CREATE TRIGGER TRIGGER_TWEET_COLLISIONS after
  INSERT ON tweets FOR EACH row EXECUTE PROCEDURE TWEET_DATA();
    --get quantity of tweets and collisions for a location

insert into tweets(collision_id) values (1);

DROP TABLE IF EXISTS batting;
CREATE EXTERNAL TABLE IF NOT EXISTS batting(id STRING, year INT, team STRING, league STRING, games INT, ab INT, runs INT, hits INT, doubles INT, triples INT, homeruns INT, rbi INT, sb INT, cs INT, walks INT, strikeouts INT, ibb INT, hbp INT, sh INT, sf INT, gidp INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/batting';
DROP TABLE IF EXISTS master;
CREATE EXTERNAL TABLE IF NOT EXISTS master(id STRING, byear INT, bmonth INT, bday INT, bcountry STRING, bstate STRING, bcity STRING, dyear INT, dmonth INT, dday INT, dcountry STRING, dstate STRING, dcity STRING, fname STRING, lname STRING, name STRING, weight INT, height INT, bats STRING, throws STRING, debut STRING, finalgame STRING, retro STRING, bbref STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/master'; 
DROP VIEW IF EXISTS mostdbltrpl;
CREATE VIEW mostdbltrpl AS SELECT b.id as id ,(b.doubles + b.triples) AS dblstrpls, n.bcity as bcity, n.bstate as bstate FROM batting b JOIN master n ON (b.id=n.id);
DROP VIEW IF EXISTS shrunk1;
CREATE VIEW shrunk1 AS SELECT bcity, bstate, SUM(dblstrpls) as dblstrpls  FROM mostdbltrpl GROUP BY bcity, bstate;
SELECT subquery.bcity, subquery.bstate FROM (SELECT bcity, bstate, DENSE_RANK() OVER (ORDER BY dblstrpls DESC) AS rank FROM shrunk1) subquery WHERE rank <=5;

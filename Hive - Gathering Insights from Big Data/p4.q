DROP TABLE IF EXISTS fielding;
CREATE EXTERNAL TABLE IF NOT EXISTS fielding(id STRING, year INT, team STRING, league STRING, position INT, games INT, gamesstarted INT, InnOut INT, po INT, assists INT, errors INT, doubleplay INT, passedball INT, wildpitch INT, stolenbase INT, cs INT, zr INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/fielding';
DROP VIEW IF EXISTS filtered;
CREATE VIEW filtered AS SELECT team, sum(errors) AS errors FROM fielding WHERE year = 2001 GROUP BY team;
SELECT subquery.team FROM (SELECT team, RANK() OVER (ORDER BY errors DESC) AS rank FROM filtered) subquery WHERE rank = 1;

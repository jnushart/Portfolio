DROP TABLE IF EXISTS batting;
CREATE EXTERNAL TABLE IF NOT EXISTS batting(id STRING, year INT, team STRING, league STRING, games INT, ab INT, runs INT, hits INT, doubles INT, triples INT, homeruns INT, rbi INT, sb INT, cs INT, walks INT, strikeouts INT, ibb INT, hbp INT, sh INT, sf INT, gidp INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/batting';
DROP VIEW IF EXISTS filtered_batting;
CREATE VIEW filtered_batting AS SELECT id, year, ab, hits FROM batting WHERE year <= 2009 AND year >= 2005;
DROP VIEW IF EXISTS grouped_batting;
CREATE VIEW grouped_batting AS SELECT id, SUM(ab) as ab, SUM(hits) as hits FROM filtered_batting GROUP BY id;
DROP TABLE IF EXISTS fielding;
CREATE EXTERNAL TABLE IF NOT EXISTS fielding(id STRING, year INT, team STRING, league STRING, position INT, games INT, gamesstarted INT, InnOut INT, po INT, assists INT, errors INT, doubleplay INT, passedball INT, wildpitch INT, stolenbase INT, cs INT, zr INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/fielding';
DROP VIEW IF EXISTS filtered_fielding;
CREATE VIEW filtered_fielding AS SELECT id, year, games, errors FROM fielding WHERE year <= 2009 AND year >= 2005 OR gamesstarted is not null OR InnOut is not null OR po is not null OR assists is not null OR errors is not null OR doubleplay is not null OR passedball is not null OR wildpitch is not null OR stolenbase is not null OR cs is not null OR zr is not null;
DROP VIEW IF EXISTS filtered_fielding2;
CREATE VIEW filtered_fielding2 AS SELECT id, SUM(games) AS games, SUM(errors) as errors FROM filtered_fielding GROUP BY id;
DROP VIEW IF EXISTS joined;
CREATE VIEW joined AS SELECT b.id, b.ab, b.hits, n.errors, n.games FROM grouped_batting b JOIN filtered_fielding2 n ON (b.id=n.id);
DROP VIEW IF EXISTS filtered;
CREATE VIEW filtered AS SELECT id, ab, hits, errors, games FROM joined WHERE ab >= 40 and games >= 20;
DROP VIEW IF EXISTS badcalc;
CREATE VIEW badcalc AS SELECT filtered.id, ((filtered.hits/filtered.ab)-(filtered.errors/filtered.games)) AS calc FROM filtered;
SELECT subquery.id FROM (SELECT id, DENSE_RANK() OVER (ORDER BY calc DESC) AS rank FROM badcalc) subquery WHERE rank <=3;
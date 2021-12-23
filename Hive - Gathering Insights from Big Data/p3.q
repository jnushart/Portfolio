DROP TABLE IF EXISTS master;
CREATE EXTERNAL TABLE IF NOT EXISTS master(id STRING, byear INT, bmonth INT, bday INT, bcountry STRING, bstate STRING, bcity STRING, dyear INT, dmonth INT, dday INT, dcountry STRING, dstate STRING, dcity STRING, fname STRING, lname STRING, name STRING, weight INT, height INT, bats STRING, throws STRING, debut STRING, finalgame STRING, retro STRING, bbref STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/maria_dev/hivetest/master'; 
DROP VIEW IF EXISTS weight;
CREATE VIEW weight AS SELECT weight, count(*) AS playercount FROM master WHERE length(weight) > 0 GROUP BY weight;
SELECT subquery.weight AS weight FROM (SELECT weight.weight, weight.playercount, DENSE_RANK() OVER (ORDER BY playercount DESC) AS rank FROM weight) subquery WHERE subquery.rank =2;

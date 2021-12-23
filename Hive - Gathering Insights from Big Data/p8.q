DROP VIEW IF EXISTS joined;
CREATE VIEW joined AS SELECT b.id, b.ab, b.hits, n.bmonth, n.bstate FROM batting b JOIN master n ON (b.id=n.id) WHERE n.bmonth != '' OR n.bstate != '';
DROP VIEW IF EXISTS grouped;
CREATE VIEW grouped AS SELECT joined.bmonth AS bmonth, joined.bstate AS bstate, SUM(joined.ab) AS ab, SUM(joined.hits) AS hits, COUNT(*) AS countplayers FROM joined GROUP BY bmonth, bstate;
DROP VIEW IF EXISTS filtered;
CREATE VIEW filtered AS SELECT bmonth, bstate, ab, hits, countplayers FROM grouped WHERE countplayers >= 10 AND ab >= 1500;
SELECT subquery.bmonth AS bmonth, subquery.bstate AS bstate FROM (SELECT bmonth, bstate, (hits/ab) AS batavg, RANK() over (ORDER BY (hits/ab) ASC) AS rank FROM filtered) subquery WHERE rank = 1;
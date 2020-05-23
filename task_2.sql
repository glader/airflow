CREATE TABLE services
(
    who character varying(100) COLLATE pg_catalog."default",
    "where" character varying(100) COLLATE pg_catalog."default",
    "when" date,
    service character varying(100) COLLATE pg_catalog."default"
)

SELECT service, count(1) as amount FROM services GROUP BY service ORDER BY amount DESC LIMIT 10

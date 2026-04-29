CREATE TABLE agencies (
    agency_id SERIAL PRIMARY KEY,
    agency_name TEXT NOT NULL UNIQUE,
    country TEXT,
    founded_year INTEGER
);

CREATE INDEX idx_agencies_name ON agencies(agency_name);
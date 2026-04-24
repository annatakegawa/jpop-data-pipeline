CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    agency_id INT REFERENCES agencies(agency_id),
    group_name TEXT NOT NULL UNIQUE,
    debut_date DATE,
    dsiband_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_groups_agency_id ON groups(agency_id);
CREATE INDEX idx_groups_name ON groups(group_name);
CREATE INDEX idx_groups_active ON groups(is_active);

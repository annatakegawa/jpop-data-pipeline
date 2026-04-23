CREATE TABLE memberships (
    membership_id SERIAL PRIMARY KEY,
    idol_id INTEGER REFERENCES idols(idol_id),
    group_id INTEGER REFERENCES groups(group_id),
    start_date DATE,
    end_date DATE,
    role TEXT,
    is_current BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_memberships_idol_id ON memberships(idol_id);
CREATE INDEX idx_memberships_group_id ON memberships(group_id);
CREATE INDEX idx_memberships_dates ON memberships(start_date, end_date);
CREATE INDEX idx_memberships_is_current ON memberships(is_current);
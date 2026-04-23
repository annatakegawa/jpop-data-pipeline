CREATE TABLE idols (
    idol_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    stage_name TEXT,
    birth_date DATE,
    home_town TEXT,
    gender TEXT,
    active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_idols_name ON idols(full_name);
CREATE INDEX idx_idols_stage_name ON idols(stage_name);
CREATE INDEX idx_idols_active ON idols(active);
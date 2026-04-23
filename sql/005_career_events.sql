CREATE TABLE career_events (
    event_id SERIAL PRIMARY KEY,
    idol_id INT REFERENCES idols(idol_id),
    event_type VARCHAR(50) NOT NULL,
    event_date DATE NOT NULL,
    description TEXT
);

CREATE INDEX idx_events_idol_id ON career_events(idol_id);
CREATE INDEX idx_events_type ON career_events(event_type);
CREATE INDEX idx_events_event_date ON career_events(event_date);
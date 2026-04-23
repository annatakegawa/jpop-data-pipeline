CREATE TABLE idol_works (
    idol_id INT REFERENCES idols(idol_id),
    work_id INT REFERENCES works(work_id),
    role VARCHAR(255), -- e.g. 'lead singer', 'supporting actor'
    PRIMARY KEY (idol_id, work_id)
);

CREATE INDEX idx_idol_works_idol_id ON idol_works(idol_id);
CREATE INDEX idx_idol_works_work_id ON idol_works(work_id);
--- For discography/appearances
CREATE TABLE works (
    work_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    work_type VARCHAR(50) NOT NULL, -- e.g. 'song', 'album', 'drama', 'movie'
    release_date DATE,
    description TEXT
);

CREATE INDEX idx_works_type ON works(work_type);
CREATE INDEX idx_works_release_date ON works(release_date);
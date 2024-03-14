-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT tv_shows.title
    FROM tv_show_genres 
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title;
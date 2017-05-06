import media
import fresh_tomatoes

st_first_contact = media.Movie("Star Trek: First Contact",
    120,
    "In this film, the crew of USS Enterprise-E travel back in time to the mid 21st-century in order to stop the cybernetic Borg from conquering Earth by changing the past.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Star_Trek_08-poster.png/220px-Star_Trek_08-poster.png",
    "https://www.youtube.com/watch?v=MWcbmkdsFYs")

red_october = media.Movie("The Hunt for Red October",
    120,
    "The Soviet Union's best submarine captain in their newest sub violates orders and defects to the USA.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/36/The_Hunt_for_Red_October_movie_poster.png/220px-The_Hunt_for_Red_October_movie_poster.png",
    "https://www.youtube.com/watch?v=kxL8uBmdulY")

earth_still = media.Movie("The Day the Earth Stood Still",
    120,
    "In The Day the Earth Stood Still, a humanoid alien visitor named Klaatu comes to Earth, accompanied by a powerful eight-foot tall robot, Gort, to deliver an important message that will affect the entire human race.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Day_the_Earth_Stood_Still_1951.jpg/220px-Day_the_Earth_Stood_Still_1951.jpg",
    "https://www.youtube.com/watch?v=OfpSXI8_UpY")

armageddon = media.Movie("Armageddon",
    120,
    "The film follows a group of blue-collar deep-core drillers sent by NASA to stop a gigantic asteroid on a collision course with Earth.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Armageddon-poster06.jpg/220px-Armageddon-poster06.jpg",
    "https://www.youtube.com/watch?v=iq6q2BrTino")

django = media.Movie("Django",
    120,
    "The film follows a Union soldier-turned-drifter and his companion, a mixed-race prostitute, who become embroiled in a bitter, destructive feud between a Ku Klux Klan-esque gang of Confederate racists and a band of Mexican revolutionaries.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Djangofilm.jpg/220px-Djangofilm.jpg",
    "https://www.youtube.com/watch?v=w8Ge2hmSTbo")

sw_rogue_one = media.Movie("Rogue One: Star Wars",
    120,
    "Rogue One follows a group of rebels on a mission to steal the plans for the Death Star, the Galactic Empire's superweapon.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png",
    "https://www.youtube.com/watch?v=frdj1zb9sMY")

'''print red_october.movie_title + ": " +  red_october.movie_storyline
red_october.show_trailer()'''

#Add movies into a list
movies = [st_first_contact,
    red_october,
    earth_still,
    armageddon,
    django,
    sw_rogue_one]

fresh_tomatoes.open_movies_page(movies)
print media.Movie.__doc__
print media.Movie.__name__ + " found in " + media.Movie.__module__
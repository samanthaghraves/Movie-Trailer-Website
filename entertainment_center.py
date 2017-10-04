import media
import fresh_tomatoes

big_money_hustlas = media.Movie("Big Money Hustlas",
                                "Jugalos murder each other and other people",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyOTM5MjU0Nl5BMl5BanBnXkFtZTcwOTE3MDAzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                "https://www.youtube.com/watch?v=LIy6GQaMmWE")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = media.Movie("School of Rock",
                             "Dude steals kids and makes an awesome band",
                             "https://images-na.ssl-images-amazon.com/images/I/51v8TQDTF-L._SY300_.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

battle_royale = media.Movie("Battle Royale",
                            "The original Hunger Games",
                            "https://i1.wp.com/thefoxisblack.com/blogimages//Keorattana-Luangrathrajasombat-Battle-Royale-Poster.jpg?resize=800%2C1200",
                            "https://www.youtube.com/watch?v=N0p1t-dC7Ko")

bojack_horseman = media.Movie("Bojack Horseman",
                              "A horseman who is awful has terrible things happen to him",
                              "http://i.imgur.com/uQD2aN6.jpg",
                              "https://www.youtube.com/watch?v=Bf12qwPWDVI")

matilda = media.Movie("Matilda",
                      "Autistic girl has magical powers and is awesome",
                      "http://img.moviepostershop.com/matilda-movie-poster-1996-1010484797.jpg",
                      "https://www.youtube.com/watch?v=MdC_YMvYZyI")


#movies = [big_money_hustlas, toy_story, school_of_rock, battle_royale, bojack_horseman, matilda]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

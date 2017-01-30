import fresh_tomatoes
import media


titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "http://www.titanicandco.com/titanicfilm5.jpg",
                      "https://www.youtube.com/watch?v=ZQ6klONCq4s")

the_last_samurai = media.Movie("The Last Samurai",
                               "An American military advisor embraces the Samurai culture he was hired to destroy after he is captured in battle.",
                               "http://r1.ykimg.com/050E000052774F92675839640006D83E",
                               "https://www.youtube.com/watch?v=T50_qHEOahQ")

pride_and_prejudice = media.Movie("Pride and Prejudice",
                                  "Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But Mr. Darcy reluctantly finds himself falling in love with a woman beneath his class.",
                                  "http://static.rogerebert.com/uploads/movie/movie_poster/pride-and-prejudice-2005/large_lAb9l4kgc6QWnHamBzTnskt71A7.jpg",
                                  "https://www.youtube.com/watch?v=1dYv5u6v55Y")

jaws = media.Movie("Jaws",
                   "A part-time sheriff teams up with a marine biologist and an old seafarer to hunt the white shark down",
                   "https://lh5.googleusercontent.com/-dii6NxzJCYE/Ui_6qyNid7I/AAAAAAAAB-k/EABBbVesReA/s497/Best%252070s%2520Movies%25209.JPG",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")

django_unchained = media.Movie("Django Unchained",
                               "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
                               "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")

les_miserables = media.Movie("Les Miserables",
                             "Jean Valjean, who for decades has been hunted by the ruthless policeman Javert after breaking parole, agrees to care for a factory worker's daughter.",
                             "http://www.impawards.com/2012/posters/les_miserables_ver11.jpg",
                             "https://www.youtube.com/watch?v=IuEFm84s4oI")



movies = [titanic, the_last_samurai, pride_and_prejudice, jaws, django_unchained, les_miserables]
fresh_tomatoes.open_movies_page(movies)

                           
                                

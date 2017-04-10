# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "a story of a boy and his toys that come to life",
                        'http://www.impawards.com/1995/posters/toy_story_ver1.jpg',
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                     "A marine on an Alien Planet.",
                     'https://www.movieposter.com/posters/archive/main/98/MPW-49433',
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


guardians = media.Movie("Guardians of the Galaxy",
                        "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                        'http://www.mtv.com/crop-images/2014/02/20/Guardians-of-the-Galaxy-Poster.jpg',
                        "https://www.youtube.com/watch?v=maIEaTm5gBE")

colossal = media.Movie ("Colossal",
                        "Anne Hathaway plays a burned-out party girl navigating life back in her hometown…just as a giant monster appears in South Korea mimicking her movements thousands of miles away.",
                        'http://cdn2-www.comingsoon.net/assets/uploads/gallery/colossal/colossal-poster2.jpg',
                        "https://www.youtube.com/watch?v=Fmk3cTuGQZI")

rogue = media.Movie ("Rogue One",
                      "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                      'http://t0.gstatic.com/images?q=tbn:ANd9GcQ0S5JQhVplHbw7O6nt7Q0r23Bssl9UNzC-z3zy1r45_eLUB43l',
                      "https://www.youtube.com/watch?v=sC9abcLLQpI")

kong = media.Movie ("Kong Skull Island",
                    "A team of scientists explore an uncharted island in the Pacific, venturing into the domain of the mighty Kong, and must fight to escape a primal Eden.",
                    'http://t3.gstatic.com/images?q=tbn:ANd9GcS3OOr06uE3lEZwum5WxKkkdsC37ObLwjKZgSSx-V96yrt6DhKE',
                    "https://www.youtube.com/watch?v=AP0-9FBs2Rs")
                    

movies = [toy_story, avatar, guardians, colossal, rogue, kong]
fresh_tomatoes.open_movies_page(movies)




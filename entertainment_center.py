import media
import fresh_tomatoes
my_movies_list=[]
toy_story=media.Movie("Toy Story","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=Bj4gS1JQzjk","In a world where toys pretendto be lifeless in the presence of humans, Woody, a pullstring cowboy toy, is the leader of a group of toys owned by a boy named Andy Davis. With his family moving away one week before his birthday, Andy is given a week-early party to spend with his friends, while the toys stage a reconnaissance mission to discover Andy's new presents. Andy receives a spaceman action figure named Buzz Lightyear, whose impressive features see him replacing Woody as Andy's favorite toy. Woody becomes resentful, especially as Buzz also gets attention from the other toys. However, Buzz believes himself to be a real space ranger on a mission to return to his home planet while Woody tries to convince him that he is only a toy")
san_anderas=media.Movie("San Andreas","http://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg","https://www.youtube.com/watch?v=23VflsU3kZE","San Andreas is a 2015 American 3D disaster film directed by Brad Peyton. The screenplay was written by Carlton Cuse, with Andre Fabrizio and Jeremy Passmore receiving a story credit. The film stars Dwayne Johnson, Carla Gugino, Alexandra Daddario, Hugo Johnstone-Burt, Art Parkinson, Ioan Gruffudd, Archie Panjabi and Paul Giamatti.")
my_movies_list.append(toy_story)
my_movies_list.append(san_anderas)
fresh_tomatoes.open_movies_page(my_movies_list)
#toy_story.show_trailer()
def movie_title():
    title =input("Enter the movie title: ")
    return title
def movie_release():
    release = int(input("Enter the year of release:"))
    return release
def movie_director():
    director= input("Enter the name of the director:")
    return director

user=' '
movies=[ ]
while user != False:
    user_action= input("Store / Search / List / Quit : ")
    if user_action.title() == 'Store':
        title=movie_title()
        release=movie_release()
        director=movie_director()
        movies.append( {
            'Title': title.title(),
            'Release': release,
            'Director': director.title()
        } )
    elif user_action.title() == 'Search':
        #search=input("Enter the title of the movie you want: ")
        #name=list(name for name in movies if search.title() in name['Title'])
        #print(name)
        search=input("Title / Release / Director :")
        if search.title() == "Title":
            tit_inp= input("Enter the title of the movie: ")
            mov_title = list(tit for tit in movies if tit_inp.title() in tit['Title'])
            print(mov_title)
        elif search.title() == "Release":
            rel_input = int(input("Enter the year of release: "))
            mov_release = list(rel for rel in movies if rel_input == rel['Release'])
            print(mov_release)
        elif search.title() == "Director":
            dir_input = input("Enter the name of the Director: ")
            mov_director = list(direct for direct in movies if dir_input.title() in direct["Director"])
            print(mov_director)
        else:
            print("Sorry try again :(")
    elif user_action.title() == "List":
        print(movies)
    elif user_action.title() == 'Quit':
        break
    else:
        print("Sorry kindly enter the action you want.")

movies
print(movies)

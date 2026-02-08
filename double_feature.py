from datetime import datetime, timedelta

movie_string = "Wicked: For Good 2 HR 17 MIN PG AMC Fiesta Square 12 RealD 3D : VISUALIZING THE FUTURE AMC Signature Recliners Reserved Seating Closed Caption Audio Description 2:45pmUP TO 15% OFF UP TO 15% OFF 6:00pm 9:00pm Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 3:15pm20% OFF 20% OFF 6:30pm 9:45pm Now You See Me: Now You Don't 1 HR 53 MIN PG13 AMC Fiesta Square 12 Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 3:15pm20% OFF 20% OFF 6:15pm 9:00pm Rental Family 1 HR 50 MIN PG13 AMC Fiesta Square 12 AMC Artisan Films AMC Signature Recliners Reserved Seating Closed Caption Audio Description 6:15pm Eternity 1 HR 52 MIN PG13 AMC Fiesta Square 12 AMC Artisan Films AMC Signature Recliners Reserved Seating Closed Caption 7:15pm 10:30pm Zootopia 2 1 HR 47 MIN PG AMC Fiesta Square 12 RealD 3D : VISUALIZING THE FUTURE AMC Signature Recliners Reserved Seating Closed Caption Audio Description 3:30pmUP TO 15% OFF UP TO 15% OFF 8:15pm 9:30pm Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 2:45pm20% OFF 20% OFF 4:45pm 5:30pm 7:30pm 10:15pm Sentimental Value 2 HR 13 MIN R AMC Fiesta Square 12 Norwegian Spoken with English Subtitles AMC Signature Recliners Reserved Seating AMC Artisan Films Closed Caption 9:15pm Five Nights at Freddy's 2 1 HR 44 MIN PG13 AMC Fiesta Square 12 Thrills & Chills AMC Signature Recliners Reserved Seating Closed Caption Audio Description 2:00pm20% OFF 20% OFF 4:00pm 4:40pm 7:30pmAlmost Full Almost Full 9:45pm 10:15pm Fackham Hall 1 HR 37 MIN R AMC Fiesta Square 12 Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 4:00pm 6:30pm 100 Nights of Hero 1 HR 38 MIN PG13 AMC Fiesta Square 12 Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 4:00pm JUJUTSU KAISEN: Execution 1 HR 28 MIN R AMC Fiesta Square 12 Japanese Spoken with English Subtitles AMC Signature Recliners Reserved Seating 4:15pm 6:45pm 9:15pm Five Nights at Freddy’s 2 Opening Night Event 1 HR 44 MIN PG13 AMC Fiesta Square 12 Digital AMC Signature Recliners Reserved Seating Closed Caption Audio Description 7:00pmAlmost Full Almost Full Five Nights at Freddy’s 2 Opening Night Event Trailers and Info"
#working on being able to paste into terminal but string is too long to input
#movie_string = input("Enter the movie string: ")
value_to_remove = "20% OFF"
while value_to_remove in movie_string:
    movie_string = movie_string.replace(value_to_remove, "")

#adding a word to the end to be able to get the final pm showtime
movie_string = movie_string + " done"

copy_string = movie_string
length = len(movie_string)

stopper = 1

movie_names = []
hr_positions = []
pm_positions = []
showtimes = []
start = 0

#hr counter starts at 1 because i add the first movie separately becuase
#theres no pm time before itis t
pm_counter = 0

hr_counter = 1

#getting first movie name becuase its the only one that doesnt have
#a pm time before it
hr_index = movie_string.find("HR")
movie_names.append(movie_string[start:hr_index-3])
start = hr_index + 3
copy_string = movie_string[start:length]

hr_positions.append(hr_index)
pm_index = 0


#getting the HR positions
while True:
    start = hr_index + 3
    hr_index = copy_string.find("HR ", start)

    if hr_index == -1:
        break


    #putting the original index of HR position since it is currently
    #cutting the copy string so its not the original index
    hr_positions.append(hr_index + len(movie_string) - len(copy_string))






#find PM positions
while True:
    start = pm_index + 3
    pm_index = movie_string.find("pm ", start)

    if pm_index == -1:
        break
    pm_positions.append(pm_index)
    start = pm_index + 2



while True:
    if pm_positions[pm_counter] < hr_positions[hr_counter]:
       pm_counter += 1
       if pm_counter == len(pm_positions):
            break
    else:
        movie_names.append(movie_string[(pm_positions[pm_counter -1 ] + 3):hr_positions[hr_counter] - 3])
        hr_counter += 1
        if hr_counter == len(hr_positions):
            break
        if pm_counter == len(pm_positions):
            break



#now that we have all the movie names, we need a list of the movie name
#the length, the start time, and end time
counter = 0



while counter < len(movie_names):
    #setting the range to look in for showtimes of each movie
    start = hr_positions[counter]
    duration = movie_string[hr_positions[counter] - 3:hr_positions[counter]+5].strip()

    if counter == len(movie_names) - 1:
        end = len(movie_string) + 5
    else:
       end = hr_positions[counter + 1]


    #getting movie start time
    for pm in pm_positions:
        if start < pm <= end:
            movie_time = movie_string[pm-5:pm].strip()
            #showtimes.append((movie_names[counter], movie_time))
            #getting movie end time

            duration_parts = duration.split()
            duration_hours = int(duration_parts[0])
            duration_minutes = int(duration_parts[2])


            movie_duration = timedelta(hours=(duration_hours), minutes = (duration_minutes))
    

            time_parts = movie_time.split(":")
            time_hours = int(time_parts[0])
            time_minutes = int(time_parts[1])

            movie_start = timedelta(hours=(time_hours), minutes = (time_minutes))

            end_time = movie_duration + movie_start
            if end_time > timedelta(hours=12):
                end_time = end_time - timedelta(hours=12)

            showtimes.append({"name":movie_names[counter], 
                              "duration":duration, 
                              "start_time":movie_time, 
                              "end_time":str(end_time)})
        
            #for the final showtime of the last movie
            
    



    counter += 1

    
#print("")
#for i in range(len(showtimes)):
#    print(showtimes[i]) 





    #now starting to schedule multiple movies back to back with delays


#current max delay acceptable is 60 min


#removing movies i have already seen or don't want to see
for i in range(len(movie_names)):
    print(f"{i}: {movie_names[i]}")
remove_movies_list = []
#remove_movies = int(input("Enter the movie number you don't want to see (in format: 1, 2, 3) or press enter to continue: "))
remove_movies = input("Enter movie numbers you don't want to see in format 1, 3, 4, or press enter: ")
remove_movies = remove_movies.replace(",", " ").split()


for char in remove_movies:
    if char.isdigit():
        remove_movies_list.append(int(char))


movies_to_remove = [movie_names[i] for i in remove_movies_list]

#remaking the showtimes list while excluding movies in the movies_to_remove list
showtimes = [s for s in showtimes if s["name"] not in movies_to_remove]
 
count = 0
next_count = 0
max_delay = timedelta(minutes=30)
while count < len(showtimes):
    next_count = 0
    

    while next_count < len(showtimes):
        if showtimes[count]["name"] == showtimes[next_count]["name"]:
            next_count += 1
            continue


        format_time_string = "%H:%M:%S"

        end_time = datetime.strptime(showtimes[count]["end_time"], format_time_string)

        start_time = datetime.strptime(showtimes[next_count]["start_time"], "%H:%M")

        delay = start_time - end_time

        #making sure time isn't negative 
        if timedelta(0) <= delay <= max_delay:
            combinations = showtimes[count]["name"] + " starts at: " + showtimes[count]["start_time"] + "\n"
            combinations += "delay: " + str(delay) + "\n"
            combinations += showtimes[next_count]["name"] + " starts at: " + showtimes[next_count]["start_time"] + "\n"
            print(combinations)
            #3rd combo
            #second_end = datetime.strptime(showtimes[next_count]["end_time"], "%H:%M:%S")
            #third_idx = 0
            #while third_idx < len(showtimes):
                #if showtimes[third_idx]["name"] in (showtimes[count]["name"], showtimes[next_count]["name"]):
                    #third_idx += 1
                    #continue

                #third_start = datetime.strptime(showtimes[third_idx]["start_time"], "%H:%M")
                #third_delay = third_start - second_end

                #if timedelta(0) <= third_delay <= max_delay:
                    #combo_chain = combinations  # copy the chain so far
                    #ombo_chain += "delay: " + str(third_delay) + "\n"
                    #combo_chain += showtimes[third_idx]["name"] + " starts at: " + showtimes[third_idx]["start_time"] + "\n"
                    
                    #print(combo_chain)

                #third_idx += 1
        

        next_count += 1

    count += 1

    

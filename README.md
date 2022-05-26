# rplace
learn to work with a ton of data



2022-04-01 12:44:10.315 UTC debut
2022-04-05 00:14:00.207 UTC fin
2022-04-04 22:47:40.185 UTC dernier pixel coloré



python3 ./drawall.py  -->  draw all pixel

#drawPixelInHour
    Part of project to draw pixel was changed between 2 hours.
    python3 ./setfinal.py  -->  Set a file with X pixel between 2 hours
    python3 ./draw.py  -->  draw the file and save the picture
    
#heatmap
    Part of project to set and draw a classic heatmap
    python3 ./setheatdata.py  -->  Set an array with each pixel to draw
    python3 ./drawheat.py  -->  Draw a heatmap with this array
    
#colors
    Part of project to draw pourcentage of each colors were draw
    python3 ./gettotalcolors.py -->  set a dict with all colors
    python3 ./drawcolors.py  -->  draw a pie with dict of colors

#users
    Part of project to draw a bar graph with how many people change pixels and how much
    python3 ./getallusers.py -->  set an array of dict with all users.
                                  An array is necessary to separate the files into 4 groups because work with just 1 dict is too big.
    python3 ./userstat.py -->  many function to check different stat about the users array, and draw a bar graph.                          

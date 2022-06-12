# Rplace
First personnal project to learn how to work with data and display basic stats.

Rplace site : https://www.reddit.com/r/place/comments/txvk2d/rplace_datasets_april_fools_2022/


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Features

- Display the complete rplace picture
- Draw pixels only between 2 hours
- Display a pie chart with pourcentage of colors used during rplace
- Display a bar chart with the number of times a person has changed a pixel
- Display a pixels's heatmap



## Tech

This project is a complete python project with the next lib to display data:

| Library | site |
| ------ | ------ |
| matplotlib | https://matplotlib.org/stable/index.html |
| seaborn | https://seaborn.pydata.org/index.html |
| Pillow | https://pillow.readthedocs.io/en/stable/ |
| numpy | https://numpy.org/ |

## Installation

for this project, I used Python 3.6.9

https://www.python.org/downloads/

And the rplace Dataset

https://placedata.reddit.com/data/canvas-history/index.html

Create a folder rplace in `src` folder and push all file in to get the following path :

**/home/{user}/rplace/src/rplace/header_1.txt**

You can install the dependencies manually or just execute the following command in main folder:

```sh
pip install -r requirements/requirements.txt
```


## Utilization

All commande must be execute in the folder `src`

The four part use 2 commands:

- Sort all rplace files and create a file with informations will be used by the second command
- draw picture or graph with previous file

### Create the complete rplace
```sh
python3 ./drawall.py
```

### Draw pixel between 2 hours

```sh
python3 ./drawPixelInHours/setfinal.py
python3 ./drawPixelInHours/draw.py
```
You can choose the hours in setfinal file in line 20:

`if "2022-04-04 12:00:00.000" < x[0] < "2022-04-04 12:10:00.000":`

The 3 most intresting date are :
- start of rplace :2022-04-01 12:44:10.315 UTC 

- end : 2022-04-05 00:14:00.207 UTC

- last colored pixel : 2022-04-04 22:47:40.185 UTC 

### Draw heatmap
> do not forget the logarithm function to draw a heatmap without saturated part
> 
> `heat_map = sb.heatmap(data, robust=True, norm=LogNorm())`


```sh
python3 ./heatmap/setheatdata.py
python3 ./heatmap/drawheat.py
```
 ![users graph](/picture/heatmap/heatmap.png)


### Draw colors pie
```sh
python3 ./colors/gettotalcolors.py
python3 ./colors/drawcolors.py
```
 ![users graph](/picture/colors/colorPie_15.png)


### Draw users bar chart
This part is inaccurate.

I can't work with all users in one dict to show pixels changed in 5*1 bar because we have too many unique user_id.

I separated the folder into 4 x 20 files and worked with them but as a result, a user can appear in all five categories.
```sh
python3 ./users/getallusers.py
python3 ./users/statuser.py
python3 ./users/drawusers.py
```
 ![users graph](/picture/users/users_change_pixels.png)


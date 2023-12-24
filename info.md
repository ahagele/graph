# Notes For Graphing Pico calibration data
# Another heading


[Extract Values between two strings in a text file using python](https://stackoverflow.com/questions/18865058/extract-values-between-two-strings-in-a-text-file-using-python)

[Filter a 2D numpy array](https://stackoverflow.com/questions/47885848/filter-a-2d-numpy-array)

[Read CSV file to numpy array, first row as strings, rest as float](https://stackoverflow.com/questions/12336234/read-csv-file-to-numpy-array-first-row-as-strings-rest-as-float)

[gridlines](https://www.w3schools.com/python/matplotlib_grid.asp) 

[numpy read files](https://python-course.eu/numerical-programming/reading-and-writing-data-files-ndarrays.php)

[multiple axis graph](https://matplotlib.org/3.4.3/gallery/ticks_and_spines/multiple_yaxis_with_spines.html)

[interate class](https://www.w3schools.com/python/python_iterators.asp#:~:text=To%20create%20an%20object%2Fclass,the%20object%20is%20being%20created.)

---
## watch out for
- pulse data is in reverse chronological order (newest first) 
  Use **list.reverse()** (speed?)
  <mark>Hello</mark>
  
---  
## ToDo
1. select txt file
2. read file
3. filter pulse list
4. keep column names
5. filter calibration pulses 
   (detect multiple cals)
6. extract relevant cols by name
   (save result as csv)
7. generate graph(s)
8. save graph

options:
- view source data (table or export as csv)

# Log
4/12/23 refactor
- classes for: data collect, csv, graph

lvm data class:
input: file name, block delimiter, column numbers, column names
output list of cal lists 

csv output class (1 set of data):
input: list of data points, file name
output: csv file




   
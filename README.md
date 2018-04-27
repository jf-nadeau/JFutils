# JFutils

### requirements: python3 

### How to use the modules:
##### Option 1: 
Have the script in your working directory and import JFutils
##### Option 2:
Add the script to your pythonpath
PYTHONPATH="${PYTHONPATH}:<path/to>/JFutils/"
export PYTHONPATH

Note: add this to your bashrc to have it permanantly

### Modules:
##### progress_bar:
This is a loop based progress bar. It prints a dynamic progress of the execution on the screen.
Usage:
1)Save the time with time.time() outside of the loop. (initial_time)
2)Get the number of loops your script will do (total_count)
3)Make sure you have a counter in your loop (current_count)
4)Call the module with the 3 arguments above: progress_bar(initial_time, total_count, current_count)

Note: The dynamic display will fail if the terminal size is smaller than the lenght of the progress bar line

##### read_config:
This module reads config files.
example of a config file:
#This is a config file
param1=value1
paeam2=value2

The module returns a dictionary {param1: value1, param2: value2}
Usage: read_config(filename)

##### read_tsv and read_csv:
Those modules reads tab separated and coma separated files.
They return a list of lines. Each lines is a list of columns.
Usage: read_tsv(filename)
example:
file:
a b c
d e f
g h i
read_tsv(file) will return [['a', 'b', 'c']['d', 'e', 'f']['g', 'h', 'i']]

##### write_tsv and write_csv:
Those modules writes the informations of a list in a tab separated or coma separated format.
The input must be a list of lists.
Usage: write_csv(l)
example:
l=[['a', 'b', 'c']['d', 'e', 'f']['g', 'h', 'i']]
write_csv(l) will produce a file containg this information:
a,b,c
d,e,f
g,h,i

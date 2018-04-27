# JFutils

### requirements: python3 

### How to use the modules:
##### Option 1: 
Have the script in your working directory and import JFutils
##### Option 2:
Add the script to your pythonpath<br />
PYTHONPATH="${PYTHONPATH}:<path/to>/JFutils/"<br />
export PYTHONPATH<br />

Note: add this to your bashrc to have it permanantly

### Modules:
##### progress_bar:
This is a loop based progress bar. It prints a dynamic progress of the execution on the screen.<br />
Usage:<br />
1)Save the time with time.time() outside of the loop. (initial_time)<br />
2)Get the number of loops your script will do (total_count)<br />
3)Make sure you have a counter in your loop (current_count)<br />
4)Call the module with the 3 arguments above: progress_bar(initial_time, total_count, current_count)<br />

Note: The dynamic display will fail if the terminal size is smaller than the lenght of the progress bar line

##### read_config:
This module reads config files.<br />
example of a config file:<br />
#This is a config file<br />
param1=value1<br />
paeam2=value2<br />

The module returns a dictionary {param1: value1, param2: value2}<br />
Usage: read_config(filename)<br />

##### read_tsv and read_csv:<br />
Those modules reads tab separated and coma separated files.<br />
They return a list of lines. Each lines is a list of columns.<br />
Usage: read_tsv(filename)<br />
example:<br />
file:<br />
a b c<br />
d e f<br />
g h i<br />
read_tsv(file) will return [['a', 'b', 'c']['d', 'e', 'f']['g', 'h', 'i']]<br />

##### write_tsv and write_csv:
Those modules writes the informations of a list in a tab separated or coma separated format.<br />
The input must be a list of lists.<br />
Usage: write_csv(l)<br />
example:<br />
l=[['a', 'b', 'c']['d', 'e', 'f']['g', 'h', 'i']]<br />
write_csv(l) will produce a file containg this information:<br />
a,b,c<br />
d,e,f<br />
g,h,i<br />

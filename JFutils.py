######################## PROGRESS BAR #############################
def progress_bar(initial_time, current_count, total_count, bar_size=25):
    """ This function print a dynamic progress bar on the terminal.
        USAGE:  1) before your loop, save the time (time.time()) and the total number of elements/loops (ex: The size of the list you're looping on) 
                2) Make sure you have a counter in your loop
                3) Inside your loop, call this function with the 3 mandatory arguments
                opt) You can change the size of the progress bar [==>      ] with the 4th argument. By default, it's 25 characters long
                *warning: The display will not work properly if the bar is larger than your terminal window size """

    if(bar_size<3 or bar_size>100):
        print("ERROR: PROGRESS BAR DISPLAY FAILURE: bar_size must be between 3 and 100 inclusively", end='\r')
        return
    m=int((time.time() - initial_time)/60)
    s=int((time.time() - initial_time)%60)
    percent=int((current_count/total_count*100))
    progress="Progress: {}/{} ({}%) | Time elapsed: {}:{ss:02d}".format(current_count,total_count,percent,m,ss=s)
    print("...[{}>{}] {}".format("="*int(percent/int(100/bar_size))," "*(bar_size-int(percent/int(100/bar_size))),progress), end='\r')
###################################################################
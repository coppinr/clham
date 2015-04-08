CLHAM

Command-line (Canadian) HAM amateur radio

by Rhiannon Coppin, North Vancouver, B.C.
April 7, 2015

This command-line python utility reads in and presents various forms of the question bank, which is made available as a dual-language delimited text file from Industry Canada's web site.
The URL of this file (zipped) at this time (April 2015) is: http://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip
Locator URL on Industry Canada site: http://www.ic.gc.ca/eic/site/025.nsf/eng/h_00004.html
Note: If the format of the file changes substantially, this program may need modification to function.
The current schema of the text question bank is, as Industry Canada states:

Each record has the following data, separated by ";"

Question ID
English Question
Correct English Answer
Incorrect English Answer 1
Incorrect English Answer 2
Incorrect English Answer 3
French Question
Correct French Answer
Incorrect French Answer 1
Incorrect French Answer 2
Incorrect French Answer 3

----- The questions are divided into eight sections, which have their own subsections.
Some others have labelled them as follows:

1 - Regulations and Policies (25 subsections)
2 - Operating and Procedures (9 subsections)
3 - Station Assembly, Practices and Safety (21 subsections)
4 - Circuit Components (6 subsections)
5 - Basic Electronics and Theory (13 subsections)
6 - Antennas and Feedlines (13 subsections)
7 - Propagation (8 subsections)
8 - Interference and Suppression (5 subsections)

Note: The actualy exam has 100 questions. There are also 100 subsections in total.
It appears that the practice tests are generated (see http://apc-cap.ic.gc.ca/pls/apc_anon/apeg_print.basic_exam)
by taking one question from each of the subsections, so that is what I do here.


I give the option of running the test in french (-f at command line).
I also give you the option of saving a file of the questions you got wrong, so you can re-load them all again to re-test just them.
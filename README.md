#CLHAM

**C**ommand-**L**ine (Canadian) **HAM**:<br>
*Test generator for the Industry Canada amateur radio question banks*


*by Rhiannon Coppin, North Vancouver, B.C.*

*Updated: Oct. 10, 2015*

###Quick Start:

Usage: **clham.py -i &lt;input textfile&gt;**

OPTIONAL arguments:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**-a** (use for advanced question set [DEFAULT is basic])
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**-m** (mode: "**exam**" for exam silumator [DEFAULT is "all" questions])
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**-f** (use to select Francais [DEFAULT landuage is English])

Enter "**q**" anytime to quit.

**Notes:**

1. The input text file can be the Industry Canada delimited question bank, or the output of "wrong answers" obtained from a previous run of this program.

2. The exam mode ("**-m exam**") runs through one pseudo-randomly chosen question from each section (though you can restrict which sections to pull from), resulting in a generated test of 50 questions for the Advanced set, and of 100 questions for the Basic set.

3. You are given the option after finishing the test, or even after entering "q" to quit, to save the questions you got wrong to a text file. You can then rerun that text file as input, and run a test from only your 'problem' questions.

4. The French translation of the intro and section labels is poor; the labelling of the section in English may also be questionable.

###Sample Usage:
To run one or more entire sections from the Advanced Question Bank:
> python clham.py -a -i amat_adv_quest/amat_adv_quest_delim.txt

To run a simulated Advanced exam:
> python clham.py -a -i amat_adv_quest/amat_adv_quest_delim.txt -m exam

To run one or more entire sections from the Basic Question Bank:
> python clham.py -i amat_basic_quest/amat_basic_quest_delim.txt

To run a simulated Basic exam:
> python clham.py -i amat_basic_quest/amat_basic_quest_delim.txt -m exam

To run the set of questions you got wrong and save to a textfile (say, name "wrong_answers.txt") from a previous run this program:
> python clham.py -i wrong_answers.txt

**To run the Industry Canada question banks in French instead, add the switch "-f" to any of the commands above**

###Details:

This command-line python utility reads in and presents various forms of the basic and advanbced question banks, which are made available as dual-language delimited text files from Industry Canada's website.

The URLs of these file (zipped) at this time (Oct. 2015) are: 
* [http://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip](http://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip)
* [http://apc-cap.ic.gc.ca/datafiles/amat_adv_quest.zip](http://apc-cap.ic.gc.ca/datafiles/amat_adv_quest.zip)

Locator URL on Industry Canada site: [http://www.ic.gc.ca/eic/site/025.nsf/eng/h_00004.html](http://www.ic.gc.ca/eic/site/025.nsf/eng/h_00004.html)

Note: If the format of the file changes substantially, this program may need modification to function.

The current schema of the text question bank is, as Industry Canada states:

Each record has the following data, separated by ";"

* Question ID
* English Question
* Correct English Answer
* Incorrect English Answer 1
* Incorrect English Answer 2
* Incorrect English Answer 3
* French Question
* Correct French Answer
* Incorrect French Answer 1
* Incorrect French Answer 2
* Incorrect French Answer 3

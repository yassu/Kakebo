# Kakebo

---

* [Licence](#licence)
* [Input file format](#format)
* [How to use this program](#how_to_use)

---

This is simple program for account books.
By using program, you can solve regression line and average for used money and plot regression line per one day.

For this program, need python3, matplotlib and numpy.

##<a name="licence"> Licence

This program is very free.
You can use for any purpose without my consent.

##<a name="format"> Input file format

First, we learn how to write account book for this program.
But this is very simple.

First line or separation for day is `======`.
We can continue after `======`.But this is ignored by this program.

We write `contents:income:rest` for signing income or outcome.

We write `--` in head of line for comment.
Note that this is only ** Head of line ** without way of line.

Blank line is ignored by this program.

For Example, following example is llegal(example.dat):

    ====== 2014/02/14(Fri)
    eat lunch              : -100 : 1000

    -- comment
    eat dinner             : -100 : 900

    ====== 2014/02/15(Wed)

    eat lunch              : -300 : 600
    eat dinner             : -600 : 0

    ====== 2014/02/16(Thu)

    go Bank : +10000 : 10000
    eat lunch: -210: 9790


##<a name="how_to_use"> How to use this program

How to use this program is very simple.

    ./kakebo.py [-g|--graphical] filename

Without `-g` or `--graphical` optional, print average or regression corfficient for linear expression of using money:

    average moneys   : 436.67
    regression coeff : 5.00

With `-g` or `--graphical` optional, print statics infomation and plot data and the regression line.

![Plotting Data](example.png)

Finally, if you is favorite of this program, I recommand to alias for this program:

    alias kakebo=PATH/kakebo.py

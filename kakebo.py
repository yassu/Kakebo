#!/usr/bin/env python3 

def trim_both(text):
    while len(text)>0 and text[0] in (' ', '\t'):
        text = text[1:]
    
    while len(text)>0 and text[-1] in (' ', '\t'):
        text = text[:-1]

    return text

def trim(text):
    def rm(c):
        if c in (' ', '\t'):
            return ''
        else:
            return c
    return ''.join(map(rm, text))

def parse_money(filename):
    """ get list of used mony in file """
    a_money = []
    with open(filename) as f:
        text = f.read()
        for daily in text.split('======'):
            a_money.append(0)
            for line in daily.split('\n'): 
                if trim(line) == '':
                    continue
                if line.startswith('--'):   # comment line
                    continue

                content, income, rest = line.split(':')
                income = trim_both(income)
                if income[0] == '-':
                    a_money[-1] += int(income[1:])
    return a_money

def get_average(datas):
    """ return average of datas """
    return sum(datas)/ len(datas)

def obtain_regress(data):
    n = len(data)
    xm = 0.0
    ym = 0.0
    for x, y in data:
        xm += x
        ym += y
    xm /= n
    ym /= n
    sx2 = 0.0
    sxy = 0.0
    for x, y in data:
        sx2 += (x - xm) ** 2
        sxy += (x - xm) * (y - ym)
    a = sxy / sx2
    return a, ym - a * xm

def print_result_analysis(moneys):
    """ print result """

def write_into_plt(datas, plt_filename):
    """ write result of analyse into plt_filename """

def plot_plt_filename(plt_filename):
    """ plot plt_filename by using gnuplot """

def main(filename):
    """
    print result of analysis
    if graphic mode, plot this by using gnuplot
    """
    moneys = parse_money(filename)
    average = get_average(moneys)

    data = list(zip(list(range(len(moneys))), moneys))
    regression_coef = obtain_regress(data)[0]

    print('average moneys   : {}' .format(average))
    print('regression coeff : {}' .format(regression_coef))

def trim_test():
    s = ' fjp rjqp  rjqr  '
    print(trim_both(s))

def parse_test():
    filename = 'kakebo.txt'
    print(parse_money(filename))

def obtain_regression_test():
    data = [
                (1.2,2.2), (2.1,3.8), (3.3,5.6), (4.1,7.1), (5,8.8)
          ]
    print(obtain_regress(data))

main('kakebo.txt')

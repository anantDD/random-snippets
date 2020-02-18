from collections import namedtuple
from random import randrange
from datetime import datetime, timedelta


def loop_through_days(loc, questions_left, sizes, total_chapters):
    printable = []
    for day in range(14):
        today_list = []
        for q in range(7):
            if questions_left == 0:
                # f.write('\n')
                # f.write(str(today_list))
                printable.append(today_list)
                return printable
            else:
                index = randrange(0, total_chapters)
                while(sizes[index] == 0):
                    index = randrange(0, total_chapters)
                name, ind, size = loc[index]
                sizes[index] -= 1
                questions_left -= 1
                today_list.append(f'{name} {ind}.{size-sizes[index]}')

        printable.append(today_list)
        # f.write('\n')
        # f.write(str(today_list))
    return printable


def main():
    chapter = namedtuple('chap', 'name index size')

    # list of chapters
    loc = [
        chapter('arr', 1, 9),
        chapter('linked', 2, 8),
        chapter('stacks', 3, 6),
        chapter('trees', 4, 12),
        chapter('puzzle', 6, 10),
        chapter('OOP', 7, 12),
        chapter('recursion', 8, 14),
        chapter('system-design', 9, 8),
        chapter('sorting', 10, 11),
        chapter('databases', 14, 7),
    ]
    filename = 'schedule.txt'

    sizes = []
    questions_left = 0
    for chap in loc:
        sizes.append(chap.size)
        questions_left += chap.size
    total_chapters = len(loc)

    to_print = loop_through_days(loc, questions_left, sizes, total_chapters)

    with open(filename, 'w') as f:
        delta = 0
        today = datetime.today()
        for questions_today in to_print:
            on_date = today + timedelta(days=delta)
            f.write(on_date.strftime('%d %b') + ' --- ')
            f.write(str(questions_today))
            f.write('\n')
            delta += 1


if __name__ == '__main__':
    main()

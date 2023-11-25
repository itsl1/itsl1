while True:
    print('The Nitro Type Points Machine (or NTPM)')
    wpm = int(input('What is the WPM? '))
    acc = input('What is the ACC? ')
    acc = acc.replace('%', '')
    acc = float(acc)
    wpm = float(wpm)
    if acc < 101:
        answer_points = (100 + (wpm / 2)) * (acc / 100)
        answer_points = int(answer_points)
        print(f'On that race, you earned {answer_points} points!')
    else:
        print('Higher than 100 acc. ERROR !!!')
    print()

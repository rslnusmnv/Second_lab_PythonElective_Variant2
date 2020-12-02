import pandas as pd
import pylab

# TASK 1
print('\nЗадание 1\n')
path = input('Введите путь к файлу: ')
try:
    data = pd.read_csv(path, sep=',')
    print(data.head(5))

    # TASK 2
    print('\nЗадание 2\n')
    numberColumns = data.shape[1]
    namesColumns = data.columns.tolist()
    print('Количество столбцов:', numberColumns)
    print('Названия столбцов:', namesColumns)
    for columns in data.columns:
        print('Тип данных столбца', columns, ':', data[columns].dtype)
    data.rename(columns={namesColumns[0]: 'Region', namesColumns[1]: 'Sick', namesColumns[2]: 'Recovered',
                         namesColumns[3]: 'Dead'}, inplace=True)
    numberStrings = data.shape[0]
    print('Количество строк:', numberStrings)
    print(data[['Region']])
    print(data['Region'])
    # TASK 3
    print('\nЗадание 3\n')
    request1 = input('Введите любой регион чтобы узнать статистику о нем: ')
    print(data.loc[data['Region'] == request1])

    # TASK 4
    print('\nЗадание 4\n')
    while True:
        request2 = input('Введите порог заболеваемости: ')
        if request2.isdigit():
            request2 = int(request2)
            break

    print(data['Region'].loc[data['Sick'] > request2])

    # TASK 5
    print('\nЗадание 5\n')
    top5MaxSick = pd.DataFrame((data.nlargest(5, 'Sick')), columns=['Region', 'Sick'])
    top5MaxRecovered = pd.DataFrame((data.nlargest(5, 'Recovered')), columns=['Region', 'Recovered'])
    top5MaxDead = pd.DataFrame((data.nlargest(5, 'Dead')), columns=['Region', 'Dead'])
    top5MinSick = pd.DataFrame((data.nsmallest(5, 'Sick')), columns=['Region', 'Sick'])
    top5MinRecovered = pd.DataFrame((data.nsmallest(5, 'Recovered')), columns=['Region', 'Recovered'])
    top5MinDead = pd.DataFrame((data.nsmallest(5, 'Dead')), columns=['Region', 'Dead'])
    print('Top5 c максимальным числом заболевших\n', top5MaxSick)
    print('\nTop5 с максимальным числом выздоровевших\n', top5MaxRecovered)
    print('\nTop5 с максимальным числом смертей\n', top5MaxDead)
    print('\nTop5 c минимальным числом заболевших\n', top5MinSick)
    print('\nTop5 с минимальным числом выздоровевших\n', top5MinRecovered)
    print('\nTop5 с минимальным числом смертей\n', top5MinDead)

    # TASK 6
    pylab.subplot(2, 3, 1)
    pylab.title('Top5 c максимальным числом заболевших')
    pylab.bar(top5MaxSick['Region'], top5MaxSick['Sick'])
    pylab.subplot(2, 3, 2)
    pylab.title('Top5 с максимальным числом выздоровевших')
    pylab.bar(top5MaxRecovered['Region'], top5MaxRecovered['Recovered'])
    pylab.subplot(2, 3, 3)
    pylab.title('Top5 с максимальным числом смертей')
    pylab.bar(top5MaxDead['Region'], top5MaxDead['Dead'])
    pylab.subplot(2, 3, 4)
    pylab.title('Top5 c минимальным числом заболевших')
    pylab.bar(top5MinSick['Region'], top5MinSick['Sick'])
    pylab.subplot(2, 3, 5)
    pylab.title('Top5 с минимальным числом выздоровевших')
    pylab.bar(top5MinRecovered['Region'], top5MinRecovered['Recovered'])
    pylab.subplot(2, 3, 6)
    pylab.title('Top5 с минимальным числом смертей')
    pylab.bar(top5MinDead['Region'], top5MinDead['Dead'])
    pylab.show()

except FileNotFoundError:
    print('Файл не существует!')

import pandas as pd
import pylab
import matplotlib.pyplot as plt

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

    pylab.subplot(6, 1, 1)
    pylab.title('Top-5 c максимальным числом заболевших', fontsize=8)
    pylab.barh(top5MaxSick['Region'], top5MaxSick['Sick'], color='red')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.subplot(6, 1, 2)
    pylab.title('Top-5 с максимальным числом выздоровевших', fontsize=8)
    pylab.barh(top5MaxRecovered['Region'], top5MaxRecovered['Recovered'], color='blue')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.subplot(6, 1, 3)
    pylab.title('Top-5 с максимальным числом смертей', fontsize=8)
    pylab.barh(top5MaxDead['Region'], top5MaxDead['Dead'], color='green')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.subplot(6, 1, 4)
    pylab.title('Top-5 c минимальным числом заболевших', fontsize=8)
    pylab.barh(top5MinSick['Region'], top5MinSick['Sick'], color='yellow')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.subplot(6, 1, 5)
    pylab.title('Top-5 с минимальным числом выздоровевших', fontsize=8)
    pylab.barh(top5MinRecovered['Region'], top5MinRecovered['Recovered'], color='black')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.subplot(6, 1, 6)
    pylab.title('Top-5 с минимальным числом смертей', fontsize=8)
    pylab.barh(top5MinDead['Region'], top5MinDead['Dead'], color='orange')
    plt.tick_params(axis='both', which='major', labelsize=5)
    pylab.show()

except FileNotFoundError:
    print('Файл не существует!')

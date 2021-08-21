# -*- coding: utf-8 -*-
"""0_project_1-миллионером.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SvPMy7hL6u-WCJtezn6YlSN3Ce2kG3ei
"""

import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime, time
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations

data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)

data.describe()

"""# Предобработка"""

answers = {} # создадим словарь для ответов
display(answers)

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...

"""# 1. У какого фильма из списка самый большой бюджет?

Использовать варианты ответов в коде решения запрещено.    
Вы думаете и в жизни у вас будут варианты ответов?)
"""

# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
#answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '5. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
display(answers)
# если ответили верно, можете добавить комментарий со значком "+"
# "+"

# тут пишем ваш код для решения данного вопроса:
display(data.budget.max())
data[data.budget == data.budget.max()].original_title.describe()

"""ВАРИАНТ 2"""

# можно добавлять разные варианты решения
data[data.budget == data.budget.max()].original_title.unique()

"""# 2. Какой из фильмов самый длительный (в минутах)?"""

answers['2'] = 'Gods and Generals (tt0279111)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

data[data.runtime == data.runtime.max()].original_title.unique()

"""ВАРИАНТ 2"""

data[data.runtime == data.runtime.max()].original_title.describe()

"""# 3. Какой из фильмов самый короткий (в минутах)?




"""

answers['3'] = 'Winnie the Pooh (tt1449283)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

data[data.runtime == data.runtime.min()].original_title.unique()

"""# 4. Какова средняя длительность фильмов?

"""

answers['4'] = '110'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

display(round(data.runtime.mean(),ndigits=False))
display(data.runtime.mean())

"""# 5. Каково медианное значение длительности фильмов? """

answers['5'] = '107'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

data.runtime.median()

"""# 6. Какой самый прибыльный фильм?
#### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 
"""

answers['6'] = 'Avatar (tt0499549)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

# лучше код получения столбца profit вынести в Предобработку что в начале
data['profit'] = data.revenue-data.budget
display(data.profit.max())

data[data.profit == data.profit.max()].original_title.unique()

"""# 7. Какой фильм самый убыточный? """

answers['7'] = 'The Lone Ranger (tt1210819)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

data['profit'] = data.revenue-data.budget
display(data.profit.min())

data[data.profit == data.profit.min()].original_title.unique()

"""# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?"""

answers['8'] = '1478'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

display(data[data.revenue > data.budget].original_title.count())

film_similar=data[data.revenue > data.budget]
display(film_similar.original_title)

"""# 9. Какой фильм оказался самым кассовым в 2008 году?"""

answers['9'] = 'The Dark Knight (tt0468569)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df_2008=data[(data['release_year'] == 2008)]
display(df_2008.revenue.max())
df1_2008=df_2008[(df_2008['revenue']==df_2008.revenue.max())]
display(df1_2008)

"""# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?

"""

answers['10'] = 'The Lone Ranger (tt1210819)'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.loc[(data.release_year>= 2012)&(data.release_year <=2014)].sort_values(by='profit',ascending=True)
display(df[df.profit==df.profit.min()].original_title)

"""# 11. Какого жанра фильмов больше всего?"""

answers['11'] = 'Drama'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале

# split разделяет фильмы по жанрам
df2=data['genres'].str.split('|').explode().value_counts()
display(df2)

# split не разделяет фильмы по жанрам, поэтому данных выдаётся меньше
#df=data['genres'].value_counts()
#display(df)

"""ВАРИАНТ 2"""

df = data
new_df=df['genres'].apply(lambda x: x.split('|'))

new_df.explode('genres').value_counts()

data.genres.str.split('|').explode().value_counts()

"""# 12. Фильмы какого жанра чаще всего становятся прибыльными? """

answers['12'] = 'Drama'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df1= data.copy()
df1['genres'] = df1.genres.str.split('|')
df1 = df1.explode('genres')
#display(df1)

df1.genres[df1['profit']>0].value_counts().head(1)

"""# 13. У какого режиссера самые большие суммарные кассовые сборы?"""

answers['13'] = 'Peter Jackson'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy()
df['director'] = df.director.str.split('|') 
#display(df)
df = df.explode('director').groupby(['director']).sum().sort_values(by = 'revenue', ascending=False) 
df

"""ВАРИАНТ 2"""



"""# 14. Какой режисер снял больше всего фильмов в стиле Action?"""

answers['14'] = 'Robert Rodriguez'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy()
df['genres'] = df.genres.str.split('|') 
df['director'] = df.director.str.split('|') 
df=df.explode('genres')
#display(df)

df.sort_values(by='genres')
df = df[df.genres.str.contains('Action',na=False)]
df1 = df.explode('director').groupby(['director'])['imdb_id'].count().sort_values(ascending=False) 
df1

"""# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? """

answers['15'] = 'Chris Hemsworth'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy() #создаём копию Датасета
df['cast'] = df.cast.str.split('|') #разделяет актеров и переносим их в отдельные строки
df=df.explode('cast')
#display(df)

df1=df[df.release_year==2012] #отбираем только фильмы 2012 года
#display(df1)
df1.sort_values(by='revenue', ascending=False) #сортируем по кассовому сбору: самый высокий в первой строчке

#определяем суммарный кассовый сбор для каждого фильма и ставим на первую строку искомый фильм
df2 = df1.groupby(['cast']).revenue.sum().sort_values(ascending=False).head(1) 
df2

"""# 16. Какой актер снялся в большем количестве высокобюджетных фильмов?"""

answers['16'] = 'Matt Damon'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy() #создаём копию Датасета
df=df[df.budget > df.budget.mean()] #отбираем записи с бюджетом выше среднего

df1=pd.Series(df.cast.str.split('|').sum()).value_counts().index[0]
df1

"""# 17. В фильмах какого жанра больше всего снимался Nicolas Cage? """

answers['17'] = 'Action'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy()
df['genres'] = df.genres.str.split('|') 
df['cast'] = df.cast.str.split('|') 
df=df.explode('cast')
#display(df)
#display(df1)

df1=df[df.cast=='Nicolas Cage'] #отбираем только фильмы с Nicolas Cage
df1=df1.genres.explode().value_counts().head(1)
df1

"""# 18. Самый убыточный фильм от Paramount Pictures"""

answers['18'] = 'K-19: The Widowmaker'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df = data.copy()
df['production_companies'] = df.production_companies.str.split('|') #помещаем название компании в отдельную строку
df=df.explode('production_companies')
#display(df)

df1=df[df.production_companies=='Paramount Pictures'] #отбираем самый убыточный фильм
df1

df2 = df1.groupby(['original_title']).sum().sort_values(by='profit',ascending=True).head(1)
df2

"""# 19. Какой год стал самым успешным по суммарным кассовым сборам?"""

answers['19'] = '2015'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

display(df.groupby(by='release_year')['revenue'].sum()) #группировка кассовых сборов по годам; при группировке выполняется суммирование
display(df.groupby(by='release_year')['revenue'].sum().sort_values(ascending=True).tail(1)) #тоже, но выводится последняя строка с максимальными кассовыми сборами

"""# 20. Какой самый прибыльный год для студии Warner Bros?"""

answers['20'] = '2014'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['production_companies'] = df.production_companies.str.split('|') #помещаем название компании в отдельную строку
df=df.explode('production_companies')
#display(df)

df1=df[df.production_companies.str.contains('Warner Bros')] #отбираем записи в датасет, относящиеся к компании Warner Bros
df1

display(df1.groupby(by='release_year')['revenue'].sum()) #группировка кассовых сборов по годам; при группировке выполняется суммирование
display(df1.groupby(by='release_year')['revenue'].sum().sort_values(ascending=True).tail(1)) #тоже, но выводится последняя строка с максимальными кассовыми сборами

"""# 21. В каком месяце за все годы суммарно вышло больше всего фильмов?"""

answers['21'] = 'сентябрь'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['month'] =pd.to_datetime(df.release_date)
#display(df.month)

df['month'] =df["month"].dt.month #сформировали колонку в датасете и ввели в неё месяц из даты релиза
#display(df)

display(df.groupby(by='month')['original_title'].count().sort_values(ascending=False).head(1)) 
#группировка по месяцам за все годы; выдается только месяц и наибольшее количество фильмов

"""# 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)"""

answers['22'] = '450'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['month'] =pd.to_datetime(df.release_date)
#display(df.month)

df['month'] =df["month"].dt.month #сформировали колонку в датасете и ввели в неё месяц из даты релиза
#display(df)

df.groupby(by='month')['original_title'].count().sort_values(ascending=True)

df1=df.loc[(df.month>=6)&(df.month <=8)].sort_values(by='month',ascending=True) #отбор данных по лету
df1=df1.month.count() #вывод суммарного количества фильмов
display(df1)

"""# 23. Для какого режиссера зима – самое продуктивное время года? """

answers['23'] = 'Peter Jackson'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['month'] =pd.to_datetime(df.release_date)
#display(df.month)

df['month'] =df["month"].dt.month #сформировали колонку в датасете и ввели в неё месяц из даты релиза
#display(df)

df.groupby(by='month')['original_title'].count().sort_values(ascending=True)
#display(df.month.count())

df['director'] = df.director.str.split('|') #помещаем ФИО режиссеров в отдельную строку
df=df.explode('director')
#display(df)

df.groupby(by='director')['month'].sum().sort_values(ascending=False) 
#сортировка по режиссерам (первые топ - Clint Eastwood, Steven Soderbergh, Ridley Scott, Peter Jackson, Christopher Nolan)

df1=df.loc[(df.month <=2) ].sort_values(by='month',ascending=True) #формируем два датасета df1 и df2 с данными по зиме
df2=df.loc[(df.month >=12) ].sort_values(by='month',ascending=True)
#display(df1)
#display(df2)

total_df = pd.concat([df1, df2]) #объединяем два датасета df1 и df2 с одинаковым количеством столбцов (одинаковых по наименованию и типу) в один
#display(total_df)

total_df.groupby(by='director')['month'].sum().sort_values(ascending=False).head(5) #выводим рейтинг режисссеров (лидеров; первых пятерых)

"""# 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?"""

answers['24'] = 'Four By Two Productions'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['production_companies'] = df.production_companies.str.split('|') #помещаем название студии в отдельную строку
df=df.explode('production_companies')
#display(df)

df['title_len'] =df['original_title'].str.len() #формируем новый столбец под значение средней длины названия фильма

df.groupby(by='production_companies')['title_len'].mean().sort_values(ascending=False).head(5) 
#находим студию, фильм которой с самым длинным наименованием; выводим пять лидеров

"""# 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?"""

answers['25'] = 'Midnight Picture Show'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['production_companies'] = df.production_companies.str.split('|') #помещаем название студии в отдельную строку
df=df.explode('production_companies')
#display(df)

df['overview_len'] = df.overview.apply(lambda x: len(str(x).split(' '))) #формируем новый столбец под значение кол-ва слов в описании фильма
df.overview_len.describe()

df.groupby(by='production_companies')['overview_len'].max().sort_values(ascending=False)
#находим студию, у которой описание фильма самое длинное по кол-ву слов; выводим пять лидеров

"""# 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
по vote_average
"""

answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df.vote_average.describe(percentiles=[0.01]) #проверка датасета, а есть ли такие фильмы

vote_99 = np.percentile(df.vote_average, 99) #определяем абсолютное значение, соответствующее 1%
#display(vote_99)

df1 = df[df.vote_average >= vote_99].sort_values(by='vote_average', ascending=False) #формируем выборку с фильмами, попадающих в 1%
#display(df1)

df1.groupby(by='original_title')['vote_average'].max().sort_values(ascending=False).head(12)
#формируем рейтинг, в котором находим фильм, входящий в 1 процент лучших по рейтингу
#по рейтингу выбираем фильмы

"""# 27. Какие актеры чаще всего снимаются в одном фильме вместе?

"""

answers['27'] = 'Daniel Radcliffe & Rupert Grint'
# если ответили верно, можете добавить комментарий со значком "+"
# "+"
display(answers)

df=data.copy() #копия датасета

df['cast'] = df.cast.str.split('|') #помещаем название студии в отдельную строку
df.cast=df.cast.apply(lambda x: list(combinations(sorted(x), 2)))
df=df.explode('cast').cast.mode()
display(df)

"""ВАРИАНТ 2

# Submission
"""

# в конце можно посмотреть свои ответы к каждому вопросу
answers

# и убедиться что ни чего не пропустил)
len(answers)




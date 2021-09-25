# -*- coding: utf-8 -*-
"""Юнит-2_Проект_EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qO3hYV_WQn8R43GbMVwEPNV1Hjvnm8qC

**2.8. Итоговое задание**

**Вас пригласили поучаствовать в одном из проектов UNICEF — международного подразделения ООН, чья миссия состоит в повышении уровня благополучия детей по всему миру. **

**Суть проекта — отследить влияние условий жизни учащихся в возрасте от 15 до 22 лет на их успеваемость по математике, чтобы на ранней стадии выявлять студентов, находящихся в группе риска.**

**И сделать это можно с помощью модели, которая предсказывала бы результаты госэкзамена по математике для каждого ученика школы (вот она, сила ML!). Чтобы определиться с параметрами будущей модели, проведите разведывательный анализ данных и составьте отчёт по его результатам. **
"""

!pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
!jupyter contrib nbextension install --user

"""Описание датасета: переменные, которые содержит датасет:

1 school — аббревиатура школы, в которой учится ученик

2 sex — пол ученика ('F' - женский, 'M' - мужской)

3 age — возраст ученика (от 15 до 22)

4 address — тип адреса ученика ('U' - городской, 'R' - за городом)

5 famsize — размер семьи('LE3' <= 3, 'GT3' >3)

6 Pstatus — статус совместного жилья родителей ('T' - живут вместе 'A' - раздельно)

7 Medu — образование матери (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)

8 Fedu — образование отца (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)

9 Mjob — работа матери ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)

10 Fjob — работа отца ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)

11 reason — причина выбора школы ('home' - близость к дому, 'reputation' - репутация школы, 'course' - образовательная программа, 'other' - другое)

12 guardian — опекун ('mother' - мать, 'father' - отец, 'other' - другое)

13 traveltime — время в пути до школы (1 - <15 мин., 2 - 15-30 мин., 3 - 30-60 мин., 4 - >60 мин.)

14 studytime — время на учёбу помимо школы в неделю (1 - <2 часов, 2 - 2-5 часов, 3 - 5-10 часов, 4 - >10 часов)

15 failures — количество внеучебных неудач (n, если 1<=n<=3, иначе 0)

16 schoolsup — дополнительная образовательная поддержка (yes или no)

17 famsup — семейная образовательная поддержка (yes или no)

18 paid — дополнительные платные занятия по математике (yes или no)

19 activities — дополнительные внеучебные занятия (yes или no)

20 nursery — посещал детский сад (yes или no)

21 higher — хочет получить высшее образование (yes или no)

22 internet — наличие интернета дома (yes или no)

23 romantic — в романтических отношениях (yes или no)

24 famrel — семейные отношения (от 1 - очень плохо до 5 - очень хорошо)

25 freetime — свободное время после школы (от 1 - очень мало до 5 - очень мого)

26 goout — проведение времени с друзьями (от 1 - очень мало до 5 - очень много)

27 health — текущее состояние здоровья (от 1 - очень плохо до 5 - очень хорошо)

28 absences — количество пропущенных занятий

29 score — баллы по госэкзамену по математике

**Порядок выполнения проекта:**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind

#загрузка датасета для обработки и анализа

pd.set_option('display.max_rows', 50) # показывать больше строк
pd.set_option('display.max_columns', 50) # показывать больше колонок

stud = pd.read_csv('stud_math.csv')
#print(stud)
display(stud.head(5))
stud.info()

stud.loc[:, ['studytime, granular']].describe()

"""**1. Проведите первичную обработку данных. Так как данных много, стоит написать функции, которые можно применять к столбцам определённого типа.**"""

#переименование столбцов

stud.columns=['school','sex','age','address','famsize',
'Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime',
'studytime','failures','schoolsup','famsup','paid','activities','nursery',
'granular','higher','internet','romantic','famrel','freetime','goout',
'health','absences','score']

display(stud.head(5))

"""Проверяем каждый столбец датасета"""

#проверка каждого столбца
print(stud.school.nunique())
#plt.plot(stud.school) #выбросов, пропусков нет; всего два типа школ - GP и MS
pd.DataFrame(stud.school.value_counts())

#проверка каждого столбца
#sex
print(stud.sex.nunique())
pd.DataFrame(stud.sex.value_counts())

#age
print(stud.age.nunique())
pd.DataFrame(stud.age.value_counts())
#stud.age.describe() #выбросов, пропусков нет, вместо 395 - 395 столбцов
#plt.plot(stud.age)

#address
print(stud.address.nunique())
#выбросов, пропуски есть, вместо 395 - 378 столбцов
pd.DataFrame(stud.address.value_counts())
#stud.address.describe()

#famsize
print(stud.famsize.nunique())
#выбросов, пропуски есть, вместо 395 - 368 столбцов
pd.DataFrame(stud.famsize.value_counts())
stud.famsize.describe()

#Pstatus
print(stud.Pstatus.nunique())
#выбросов, пропуски есть, вместо 395 - 350 столбцов
pd.DataFrame(stud.Pstatus.value_counts())
stud.Pstatus.describe()

#Medu
print(stud.Medu.nunique())
#выбросов, пропуски есть, вместо 395 - 392 столбцов
pd.DataFrame(stud.Medu.value_counts())
stud.Medu.describe()

#Fedu
print(stud.Fedu.nunique())
#выбросов, пропуски есть, вместо 395 - 371 столбцов
pd.DataFrame(stud.Fedu.value_counts())
stud.Fedu.describe()

#Mjob
print(stud.Mjob.nunique())
#выбросов, пропуски есть, вместо 395 - 376 столбцов
pd.DataFrame(stud.Mjob.value_counts())
stud.Mjob.describe()

#Fjob
print(stud.Fjob.nunique())
#выбросов, пропуски есть, вместо 395 - 359 столбцов
pd.DataFrame(stud.Fjob.value_counts())
stud.Fjob.describe()

#reason
print(stud.reason.nunique())
#выбросов, пропуски есть, вместо 395 - 378 столбцов
pd.DataFrame(stud.reason.value_counts())
stud.reason.describe()

#guardian
print(stud.guardian.nunique())
#выбросов, пропуски есть, вместо 395 - 364 столбцов
pd.DataFrame(stud.guardian.value_counts())
stud.guardian.describe()

#traveltime
print(stud.traveltime.nunique())
#выбросов, пропуски есть, вместо 395 - 367 столбцов
pd.DataFrame(stud.traveltime.value_counts())
stud.traveltime.describe()

#studytime
print(stud.studytime.nunique())
#выбросов, пропуски есть, вместо 395 - 388 столбцов
pd.DataFrame(stud.studytime.value_counts())
stud.studytime.describe()

#failures
print(stud.failures.nunique())
#выбросов, пропуски есть, вместо 395 - 373 столбцов
pd.DataFrame(stud.failures.value_counts())
stud.failures.describe()

#schoolsup
print(stud.schoolsup.nunique())
#выбросов, пропуски есть, вместо 395 - 386 столбцов
pd.DataFrame(stud.schoolsup.value_counts())
stud.schoolsup.describe()

#famsup
print(stud.famsup.nunique())
#выбросов, пропуски есть, вместо 395 - 356 столбцов
pd.DataFrame(stud.famsup.value_counts())
stud.famsup.describe()

#paid
print(stud.paid.nunique())
#выбросов, пропуски есть, вместо 395 - 355 столбцов
pd.DataFrame(stud.paid.value_counts())
stud.paid.describe()

#activities
print(stud.activities.nunique())
#выбросов, пропуски есть, вместо 395 - 381 столбцов
pd.DataFrame(stud.activities.value_counts())
stud.activities.describe()

#nursery
print(stud.nursery.nunique())
#выбросов, пропуски есть, вместо 395 - 379 столбцов
pd.DataFrame(stud.nursery.value_counts())
stud.nursery.describe()

#granular
print(stud.granular.nunique())
#выбросов, пропуски есть, вместо 395 - 388 столбцов
pd.DataFrame(stud.granular.value_counts())
stud.granular.describe()

#higher
print(stud.higher.nunique())
#выбросов, пропуски есть, вместо 395 - 375 столбцов
pd.DataFrame(stud.higher.value_counts())
stud.higher.describe()

#internet
print(stud.internet.nunique())
#выбросов, пропуски есть, вместо 395 - 361 столбцов
pd.DataFrame(stud.internet.value_counts())
stud.internet.describe()

#romantic
print(stud.romantic.nunique())
#выбросов, пропуски есть, вместо 395 - 364 столбцов
pd.DataFrame(stud.romantic.value_counts())
stud.romantic.describe()

#famrel
print(stud.famrel.nunique())
#выбросов, пропуски есть, вместо 395 - 368 столбцов
pd.DataFrame(stud.famrel.value_counts())
stud.famrel.describe()

#freetime
print(stud.freetime.nunique())
#выбросов, пропуски есть, вместо 395 - 384 столбцов
pd.DataFrame(stud.freetime.value_counts())
stud.freetime.describe()

#goout
print(stud.goout.nunique())
#выбросов, пропуски есть, вместо 395 - 387 столбцов
pd.DataFrame(stud.goout.value_counts())
stud.goout.describe()

#health
print(stud.health.nunique())
#выбросов, пропуски есть, вместо 395 - 380 столбцов
pd.DataFrame(stud.health.value_counts())
stud.health.describe()

#absences
print(stud.absences.nunique())
#выбросов, пропуски есть, вместо 395 - 383 столбцов
pd.DataFrame(stud.absences.value_counts())
stud.absences.describe()

#score
print(stud.score.nunique())
#выбросов, пропуски есть, вместо 395 - 389 столбцов
pd.DataFrame(stud.score.value_counts())
stud.score.describe()

"""Фильтрация, заполнение и удаление датасета"""

# сохраняем резервную копию датасета в stud_restore

stud_restore=stud
#display(stud_restore.head(5))
stud_restore.describe()
stud_restore.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1=stud
stud_1.address = stud_1.address.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.address == 'None'].index)

display(pd.DataFrame(stud_1.address.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.address.value_counts()>1).sum())

stud_1.loc[:, ['address']].info() 
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.famsize = stud_1.famsize.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.famsize == 'None'].index)

display(pd.DataFrame(stud_1.famsize.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.famsize.value_counts()>1).sum())

stud_1.loc[:, ['famsize']].info() 
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.Pstatus = stud_1.Pstatus.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.Pstatus == 'None'].index)

display(pd.DataFrame(stud_1.Pstatus.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.Pstatus.value_counts()>1).sum())

stud_1.loc[:, ['Pstatus']].info() 
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.Medu = stud_1.Medu.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.Medu == 'None'].index)

stud_1.Medu = stud_1.Medu.astype(float)

display(pd.DataFrame(stud_1.Medu.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.Medu.value_counts()>1).sum())

stud_1.loc[:, ['Medu']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.Fedu = stud_1.Fedu.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1.loc[stud_1.Fedu.astype(str)=='40.0', 'Fedu'] = 4.0 #исправляем опечатку: вместо '40.0' подставляем '4.0'

stud_1 = stud_1.drop(stud_1[stud_1.Fedu == 'None'].index)

stud_1.Fedu = stud_1.Fedu.astype(float)

display(pd.DataFrame(stud_1.Fedu.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.Fedu.value_counts()>1).sum())

stud_1.loc[:, ['Fedu']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.Mjob = stud_1.Mjob.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.Mjob == 'None'].index)

display(pd.DataFrame(stud_1.Mjob.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.Mjob.value_counts()>1).sum())

stud_1.loc[:, ['Mjob']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.Fjob = stud_1.Fjob.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.Fjob == 'None'].index)

display(pd.DataFrame(stud_1.Fjob.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.Fjob.value_counts()>1).sum())

stud_1.loc[:, ['Fjob']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.reason = stud_1.reason.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.reason == 'None'].index)

display(pd.DataFrame(stud_1.reason.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.reason.value_counts()>1).sum())

stud_1.loc[:, ['reason']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.guardian = stud_1.guardian.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.guardian == 'None'].index)

display(pd.DataFrame(stud_1.guardian.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.guardian.value_counts()>1).sum())

stud_1.loc[:, ['guardian']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.traveltime = stud_1.traveltime.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.traveltime == 'None'].index)

stud_1.traveltime = stud_1.traveltime.astype(float)

display(pd.DataFrame(stud_1.traveltime.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.traveltime.value_counts()>1).sum())

stud_1.loc[:, ['traveltime']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.studytime = stud_1.studytime.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.studytime == 'None'].index)

stud_1.studytime = stud_1.studytime.astype(float)

display(pd.DataFrame(stud_1.studytime.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud.studytime.value_counts()>1).sum())

stud_1.loc[:, ['studytime']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.failures = stud_1.failures.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.failures == 'None'].index)

stud_1.failures = stud_1.failures.astype(float)

display(pd.DataFrame(stud_1.failures.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.failures.value_counts()>1).sum())

stud_1.loc[:, ['failures']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.schoolsup = stud_1.schoolsup.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.schoolsup == 'None'].index)

display(pd.DataFrame(stud_1.schoolsup.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.schoolsup.value_counts()>1).sum())

stud_1.loc[:, ['schoolsup']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.famsup = stud_1.famsup.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.famsup == 'None'].index)

display(pd.DataFrame(stud_1.famsup.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.famsup.value_counts()>1).sum())

stud_1.loc[:, ['famsup']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.paid = stud_1.paid.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.paid == 'None'].index)

display(pd.DataFrame(stud_1.paid.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.paid.value_counts()>1).sum())

stud_1.loc[:, ['paid']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.activities = stud_1.activities.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.activities == 'None'].index)

display(pd.DataFrame(stud_1.activities.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.activities.value_counts()>1).sum())

stud_1.loc[:, ['activities']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.nursery = stud_1.nursery.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.nursery == 'None'].index)

display(pd.DataFrame(stud_1.nursery.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.nursery.value_counts()>1).sum())

stud_1.loc[:, ['nursery']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.granular = stud_1.granular.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.granular == 'None'].index)

stud_1.granular = stud_1.granular.astype(float)

display(pd.DataFrame(stud_1.granular.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.granular.value_counts()>1).sum())

stud_1.loc[:, ['granular']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.higher = stud_1.higher.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.higher == 'None'].index)

display(pd.DataFrame(stud_1.higher.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.higher.value_counts()>1).sum())

stud_1.loc[:, ['higher']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.internet = stud_1.internet.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.internet == 'None'].index)

display(pd.DataFrame(stud_1.internet.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.internet.value_counts()>1).sum())

stud_1.loc[:, ['internet']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.romantic = stud_1.romantic.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.romantic == 'None'].index)

display(pd.DataFrame(stud_1.romantic.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.romantic.value_counts()>1).sum())

stud_1.loc[:, ['romantic']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.famrel = stud_1.famrel.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1.loc[stud_1.famrel.astype(str)=='-1.0', 'famrel'] = 1.0 #исправляем опечатку: вместо '-1.0' подставляем '1.0'

stud_1 = stud_1.drop(stud_1[stud_1.famrel == 'None'].index)

stud_1.famrel = stud_1.famrel.astype(float)

display(pd.DataFrame(stud_1.famrel.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.famrel.value_counts()>1).sum())

stud_1.loc[:, ['famrel']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.freetime = stud_1.freetime.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.freetime == 'None'].index)

stud_1.freetime = stud_1.freetime.astype(float)

display(pd.DataFrame(stud_1.freetime.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.freetime.value_counts()>1).sum())

stud_1.loc[:, ['freetime']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.goout = stud_1.goout.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.goout == 'None'].index)

stud_1.goout = stud_1.goout.astype(float)

display(pd.DataFrame(stud_1.goout.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.goout.value_counts()>1).sum())

stud_1.loc[:, ['goout']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.health = stud_1.health.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.health == 'None'].index)

stud_1.health = stud_1.health.astype(float)

display(pd.DataFrame(stud_1.health.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.health.value_counts()>1).sum())

stud_1.loc[:, ['health']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.absences = stud_1.absences.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.absences == 'None'].index)

stud_1.absences = stud_1.absences.astype(float)

display(pd.DataFrame(stud_1.absences.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.absences.value_counts()>1).sum())

stud_1.loc[:, ['absences']].info()
stud_1.info()

#отфильтруем пропуски; оставим только заполненные данные
stud_1.score = stud_1.score.astype(str).apply(lambda x: None if pd.isnull(x) else None if x == 'nan' 
                      else x if '(' not in x else x[:x.find('(')].strip())

stud_1 = stud_1.drop(stud_1[stud_1.score == 'None'].index)

stud_1.score = stud_1.score.astype(float)

display(pd.DataFrame(stud_1.score.value_counts()))
print("Значений, встретившихся в столбце более 1 раз:"#Число 1 взято для ориентира, можно брать другое
      , (stud_1.score.value_counts()>1).sum())

stud_1.loc[:, ['score']].info()
stud_1.info()

"""Сохранение резервной копии очищенного датасета"""

# сохраняем резервную копию датасета в stud_update

stud_update=stud_1
#display(stud_update.head(5))
stud_update.describe()
stud_update.info()

"""Проверка датасета на заполнение полей и сохранение измененного датасета в stud_update"""

#проверка датасета на заполненность и сохранение в stud_update
stud_2=stud_update

display(stud_2.head(5))
stud_2.info()


#удаление из датасета stud_update_1 строк с значением None

#def drop_none(x):
#  if 'None' in x:
#    x=x.drop(x.index)
#  return x

#stud_2.score = stud_2.score.apply(drop_none)
#stud_2.score =[list(filter(lambda x: x is None, inner_list)) for inner_list in stud_update_1['score']]

#проверка типа данных в столбцах
#type(stud_2.score)
#stud_2['score'].value_counts()

"""**2. Посмотрите на распределение признака для числовых переменных, устраните выбросы.**"""

stud_2=stud_update

IQR = stud_2.score.quantile(0.75) - stud_2.score.quantile(0.25)
perc25 = stud_2.score.quantile(0.25)
perc75 = stud_2.score.quantile(0.75)
 
print(
'25-й перцентиль: {},'.format(perc25),
'75-й перцентиль: {},'.format(perc75),
"IQR: {}, ".format(IQR),
"Границы выбросов: [{f}, {l}].".format(f=perc25 - 1.5*IQR, l=perc75 + 1.5*IQR))
 
stud_2.score.loc[stud_2.score.between(
perc25 - 1.5*IQR,
perc75 + 1.5*IQR)].hist(bins = 16, range = (20, 100), label = 'IQR')
 
stud_2.score.loc[stud_2.score <= 100].hist(
alpha = 0.5, bins = 16, range = (0, 100), label = 'Здравый смысл')
 
plt.legend();

stud_3 = stud_2.loc[stud_2.score <= 100]
stud_3

"""**3. Оцените количество уникальных значений для номинативных переменных.**"""

stud_2=stud_update

stud_2.score.hist()
stud_2.score.describe()
stud_2.score.value_counts()

stud_2.absences.hist()
stud_2.absences.describe()
stud_2.absences.value_counts()

stud_2.school.hist()
stud_2.school.describe()
stud_2.school.value_counts()

stud_2.sex.hist()
stud_2.sex.describe()
stud_2.sex.value_counts()

stud_2.age.hist()
stud_2.age.describe()
stud_2.age.value_counts()

stud_2.address.hist()
stud_2.address.describe()
stud_2.address.value_counts()

stud_2.famsize.hist()
stud_2.famsize.describe()
stud_2.famsize.value_counts()

stud_2.Pstatus.hist()
stud_2.Pstatus.describe()
stud_2.Pstatus.value_counts()

stud_2.Medu.hist()
stud_2.Medu.describe()
stud_2.Medu.value_counts()

stud_2.Fedu.hist()
stud_2.Fedu.describe()
stud_2.Fedu.value_counts()

stud_2.famsize.hist()
stud_2.famsize.describe()
stud_2.famsize.value_counts()

stud_2.Mjob.hist()
stud_2.Mjob.describe()
stud_2.Mjob.value_counts()

stud_2.Fjob.hist()
stud_2.Fjob.describe()
stud_2.Fjob.value_counts()

stud_2.reason.hist()
stud_2.reason.describe()
stud_2.reason.value_counts()

stud_2.guardian.hist()
stud_2.guardian.describe()
stud_2.guardian.value_counts()

stud_2.traveltime.hist()
stud_2.traveltime.describe()
stud_2.traveltime.value_counts()

stud_2.studytime.hist()
stud_2.studytime.describe()
stud_2.studytime.value_counts()

stud_2.failures.hist()
stud_2.failures.describe()
stud_2.failures.value_counts()

stud_2.schoolsup.hist()
stud_2.schoolsup.describe()
stud_2.schoolsup.value_counts()

stud_2.famsup.hist()
stud_2.famsup.describe()
stud_2.famsup.value_counts()

stud_2.paid.hist()
stud_2.paid.describe()
stud_2.paid.value_counts()

stud_2.activities.hist()
stud_2.activities.describe()
stud_2.activities.value_counts()

stud_2.nursery.hist()
stud_2.nursery.describe()
stud_2.nursery.value_counts()

stud_2.granular.hist()
stud_2.granular.describe()
stud_2.granular.value_counts()

stud_2.higher.hist()
stud_2.higher.describe()
stud_2.higher.value_counts()

stud_2.internet.hist()
stud_2.internet.describe()
stud_2.internet.value_counts()

stud_2.romantic.hist()
stud_2.romantic.describe()
stud_2.romantic.value_counts()

stud_2.famrel.hist()
stud_2.famrel.describe()
stud_2.famrel.value_counts()

stud_2.freetime.hist()
stud_2.freetime.describe()
stud_2.freetime.value_counts()

stud_2.goout.hist()
stud_2.goout.describe()
stud_2.goout.value_counts()

stud_2.health.hist()
stud_2.health.describe()
stud_2.health.value_counts()

"""**4. По необходимости преобразуйте данные.**"""

# удаление из датасета маловлияющих на SCORE критериев, в том числе
# - sex; - paid; - activities; - higher 

stud_3=stud_update
stud_3.drop(['sex'], inplace = True, axis = 1)

stud_3.drop(['paid'], inplace = True, axis = 1)
stud_3.info()

stud_3.drop(['higher'], inplace = True, axis = 1)
stud_3.info()

stud_3.drop(['activities'], inplace = True, axis = 1)
stud_3.info()

#записываем датасет для следующего анализа
#сохраняем резервную копию датасета в stud_analyse

stud_analyse=stud_3
#display(stud_analyse.head(5))
stud_analyse.describe()
stud_analyse.info()

"""**5. Проведите корреляционный анализ количественных переменных.**"""

stud_4=stud_3

sns.pairplot(stud_4, kind = 'reg')

stud_4.corr()

"""**6. Отберите не коррелирующие переменные.**"""

#удаляем полностью скоррелированные переменные granular, studytime, failures:

stud_4.drop(['granular', 'studytime', 'failures'], inplace = True, axis = 1)
stud_4.info()

stud_4.corr()

"""- слабоскоррелированные переменные: 
-- Fedu
-- famrel
-- absences

- прочие параметры, влияющие на score:
-- age
-- health
-- Medu

- полностью скоррелированные (удаляем granular, studytime, failures, freetime):
-- traveltime
-- studytime
-- failures
-- granular
-- freetime
-- goout

**7. Проанализируйте номинативные переменные и устраните те, которые не влияют на предсказываемую величину (в нашем случае — на переменную score).**
"""

def get_boxplot(column):
    fig, ax = plt.subplots(figsize = (14, 4))
    sns.boxplot(x=column, y='score', 
                data=stud_4.loc[stud_4.loc[:, column].isin(stud_4.loc[:, column].value_counts().index[:10])],
               ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()

#используем для анализа все переменные, оставшиеся в датасете - 21 переменные, в том числе переменная score
for col in ['age', 'health', 'Medu', 'goout', 'traveltime','absences','famrel','Fedu',
            'address','famsize','Pstatus','Mjob','Fjob','reason','guardian','schoolsup','famsup',
            'nursery','internet','romantic']:
    get_boxplot(col)

#используем для анализа только влияющие переменные, оставшиеся в датасете - 13 переменных, без учёта переменной score
for col in ['age', 'Medu', 'goout', 'traveltime','absences','famrel',
            'address','famsize','Pstatus','Mjob','Fjob','guardian','schoolsup']:
    get_boxplot(col)

"""Проверка нулевой гипотезы"""

def get_stat_dif(column):
  cols = stud_4.loc[:, column].value_counts().index[:10]
  combinations_all = list(combinations(cols, 2))
  for comb in combinations_all:
    if ttest_ind(stud_4.loc[stud_4.loc[:, column] == comb[0], 'score'],
              stud_4.loc[stud_4.loc[:, column] == comb[1], 'score']).pvalue \
      <= 0.05/len(combinations_all): # Учли поправку Бонферони
      print('Найдены статистически значимые различия для колонки', column)
      break

for col in ['age', 'Medu', 'goout', 'traveltime','absences','famrel',
            'address','famsize','Pstatus','Mjob','Fjob','guardian','schoolsup']:
    get_stat_dif(col)

"""По полученным результатам статистически значимые параметры: address и famsize.

Используем данные два параметра для построения модели, а также параметры из предыдущего анализа:
- famrel
- absences
- age
- Medu
- goout
"""

stud_for_model = stud_4.loc[:, ['address', 'famsize', 'famrel', 'absences', 'age','Medu','freetime']]
display(stud_for_model.head())
display(stud_for_model.tail())

"""8. Не забудьте сформулировать выводы относительно качества данных и тех переменных, которые вы будете использовать в дальнейшем построении модели.

**ВЫВОДЫ по проекту.**

1. В исходном датасете исправлены опечатки

2. В исходном датасете проведен анализ на наличие незаполненных полей. В результате размер датасета сокращен с 395 до 97 строк. Т.к. при наличии незаполненных полей по любому из критериев, за исключением 'school','age','sex'(в  исходном датасете эти поля заполнены полностью), выполнение последующего анализа и построение модели не имеет смысла.

3. При определении межквартильного размаха из распределения видно, что есть выбросы. Эти выбросы могут являться предметом анализа и основой построения модели. Диапазон, в котором данные представляют интерес, от 40 до 80. 

4. Первичный анализ данных показывает:
- имеется достаточно высокое число пропусков absences - 27% случаев от оставшегося количества данных в датасете (общее число оставшихся данных 97);
- при 100-балльной шкале оценивания, около 43% набрали от 50 до 65 баллов. Выясним из-за чего такой высокий процент набравших среднюю оценку: 50-65 баллов.
- школа GP насчитывает наибольшее количество школьников в датасете - 82%. На этой выборке, для школы GP можно посмотреть влияние разных факторов на набранные баллы;
- показатель "sex" является второстепенным, т.к. примерно одинаовое соотношение F и M в датасете. В принципе, можно удалить столбец;
- целевая возрастная аудитория для анализа - школьники от 15 до 18 лет, т.е. тинэйджеры; их количество в датасете около 92%; ВАЖНЫЙ ПАРАМЕТР
- у большинства школьников в датасете отсутствует дополнительная образовательная поддержка (schoolsup, около 85,5%. ВАЖНЫЙ ПАРАМЕТР
- критерий famsup - имеет среднюю значимость и, скорее всего, не существенно влияет на оценки score
- критерий paid - второстепенный и можно удалить столбец;
- критерий activities - второстепенный и можно удалить столбец;
- критерий higher - большинство школьников планируют получить высшее образование, но уровень успеваемости говорит о низкой готовности, т.е. само желание не мотивирует к учебе и не способствует учебе; можно удалить столбец;
- критерий freetime - по всей видимости существенный параметр, т.к. около 82% школьников имеют достаточно свободного времени после учебы; 
- критерий goout - по всей видимости взаимосвязан с freetime
- критерий health - около 30% школьников оценивает своё состояние здоровье как плохо либо близкое к плохо; это коррелирует с значением критерия absences и, отчасти, может быть причиной низких оценок.

5. Столбцы на удаление из датасета перед коррекляционным анализом:
- sex
- paid
- activities
- higher 

6. На основании корреляционного анализа можно сделать следующие выводы:
- слабоскоррелированные переменные: 
-- Fedu
-- famrel
-- absences

- полностью скоррелированные (удаляем granular, studytime, failures, freetime):
-- traveltime
-- studytime
-- failures
-- granular
-- freetime
-- goout

- прочие параметры, влияющие на score:
-- age
-- health
-- Medu

7. Анализ номинативных переменных:
- первый анализ показывает какие переменные не влияют на предсказываемую величину, а именно:
-- health
-- Fedu
-- reason
-- famsup
-- nursery
-- internet
-- romantic

- проверка нулевой гипотезы показывает, что статистически значимые переменные: address и famsize

- также возмонжное влияние имеют переменные: famrel, absences, age, Medu, goout

Для модели будем использовать 7 переменных.

8. Итоговые выводы:
- датасет содержал достаточно большое количество пустых значений: из 395 строк сохранились 97, которые и были использованы для анализа данных
- датасет содержал опечатки - исправлено
- корреляционный анализ показывает, что значимые переменные имеют как положительное значение, так и отрицательное; точную оценку изменению знака дать затруднительно
- самые важные параметры: address, famsize, famrel, absences, age, Medu, goout
"""
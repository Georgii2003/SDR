﻿# SDR
**Задания от Yadro**

Т к кроме меня этот файл с пояснениями никому не нужен, распишу вкратце и без лишней графомании.
Также возможны неточности, потому что задание выполнялось 2 недели назад, я банально не помню ни сути заданий, ни своего хода мыслей в тот момент.
Само задание: [Вот][P1]

**Задание 1**
Задание было связано с SDR и делилось на две части: приёмник и передатчик.
Работал я в режиме полного дуплекса (что подразумевает под собой и приёмник, и передатчик), поэтому всё написано в одной программе.
У нас имеется массив битов, имеющих значение либо 0, либо 1. Этот массив был преобразован (по крайней мере была попытка преобразования) в QPSK-сигнал.
QPSK-сигнал даёт возможность определять значение двух бит, поэтому распределение было сделано попарно, что можно рассмотреть в коде программы.
Скринов принимаемого сигнала в момент написания найти не удалось. Возможно, дополню данный файл ими позднее.
Для наглядности процесса, приём был реализован в реальном времени через простенький цикл ***while***.
Для каждого бита информации была использована своя длина.
Также, принималось сразу две вариации графиков принимаемых битов. Для этого использовались ***scatter*** (QPSK-сигнал) и ***plot***



**Задание 2**
Второе задание подразумевало под собой работу без SDR, необходимо было создать сигнал, узнать необходимые частоты и, в последствии, исказить чтобы отфильтровать.
Я сформировал сигнал ввиде простой синусоиды, узнал значения аналоговой частоты, которая соответствует нормированной частоте Ω = 0.1Pi рад, Ω = 0.3Pi рад.
***Для Ω = 0.1Pi -  20.0  и для Ω = 0.3Pi -  59.99999999999999***
Далее вывод исходного сигнала:
![screenshot](https://github.com/Georgii2003/SDR/blob/main/TEST_Yadro/initial.png)
Из изначального сигнала необходимо было достать первые 64, 128 и 256 значений и продискритизировать:
![screenshot](https://github.com/Georgii2003/SDR/blob/main/TEST_Yadro/Discretized.png)
А после вывести их модули:
![screenshot](https://github.com/Georgii2003/SDR/blob/main/TEST_Yadro/module.png)
Искажение сигнала я начал делать, но из-за времени не успел, как и написать фильтр.



**P.S**
Написал данный файл только для Ахпашева Р.В. О том, что его необходимо было написать в день сдачи заданий понятия не имел.
***(Код и изображения хранятся в файлах согласно нумерации заданий)***



[P1]: <https://github.com/Georgii2003/SDR/tree/main/TEST_Yadro/Задание_на_стипендию.docx>
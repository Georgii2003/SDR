﻿# Тестовое задание на стажировку в компанию Yadro
**Вариант 1**

1) Написать на языке С++ класс выполняющий функциональность модулятора QAM (QPSK, QAM16, QAM64)

    Данный класс находится [здесь][P1]
    Проблем с написанием не возникло, но признаюсь, не сразу понял, что необходимо написать универсальный модулятор, поэтому первоначально написал исключительно QPSK

2) Написать на языке С++ класс выполняющий функциональность добавления гауссовского шума к созвездию QAM

    Данный класс находится [здесь][P2]
    Для него потребовалось меньше времени. В нём имеются параметры: мощность, среднее значение и дисперсия

3) Написать на языке С++ класс выполняющий функциональность демодулятора QAM (QPSK, QAM16, QAM64)

    Данный класс находится [здесь][P3]
    С данным классом возникли, скорее всего, самые большие проблемы, т к в какой-то момент он ломал логику гауссовского шума, поэтому переделывался чаще других

4) Написать последовательный вызов 1-3 для случайной последовательности бит для разных значений дисперсия шума

    Всё это находится [здесь][P4]
    Ничего необычного, главный файл, в котором вызываются все классы (случайная последовательность генерируется [здесь][P5]), а разные значения дисперсии в параметрах гауссовского шума

5) Построить график зависимости вероятности ошибки на бит от дисперсии шума

    В данном случае пришлось изучить много информации в кратчайшие сроки, т к не так много библиотек на C++ позволяют выводить графики. К сожалению в данных временных рамках я не успел установить ни одну библиотеку, поэтому сохранил данные вероятности ошибки в отдельный файл и вывел их с помощью графика на Python (программа лежит [здесь][P6])

    Сам график:

     ![graphic](https://github.com/Georgii2003/SDR/blob/main/Internship/graphics/graphic.png)

    **upd**: В данном случае, у графика QAM64 есть некоторые странности. Могу предположить, что это из-за размера вектора данных (48 бит)

    График сравнения для QAM4/QAM16/QAM64:

     ![graphic_1](https://github.com/Georgii2003/SDR/blob/main/Internship/graphics/graphic_1.png)





[P1]: <https://github.com/Georgii2003/SDR/tree/main/Internship/libraries/Qam_mod.h>
[P2]: <https://github.com/Georgii2003/SDR/tree/main/Internship/libraries/Gauss_noise.h>
[P3]: <https://github.com/Georgii2003/SDR/tree/main/Internship/libraries/Qam_demod.h>
[P4]: <https://github.com/Georgii2003/SDR/tree/main/Internship/Source.cpp>
[P5]: <https://github.com/Georgii2003/SDR/tree/main/Internship/libraries/Bits_generator.h>
[P6]: <https://github.com/Georgii2003/SDR/tree/main/Internship/error_probability.py>
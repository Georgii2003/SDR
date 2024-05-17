#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <complex>
#include <math.h>

using namespace std;

class QPSK_Demod {
public:
    QPSK_Demod() {
        // Таблица символов QPSK
        phase_to_symbol[0] = 0; // 00
        phase_to_symbol[1] = 1; // 01
        phase_to_symbol[2] = 3; // 11
        phase_to_symbol[3] = 2; // 10
    }

    // Демодуляция QPSK
    vector<bool> demod4(const vector<complex<double>>& modulated_data) {
        vector<bool> demodulated_data;
        for (const auto& data : modulated_data) {
            // Определение фазы
            int phase = static_cast<int>(round(arg(data) / (M_PI / 2)));
            if (phase < 0) phase += 4; // Приведение к диапазону [0, 3]

            // Получение двоичного символа
            int symbol = phase_to_symbol[phase];

            // Разложение символа на биты
            demodulated_data.push_back((symbol & 2) >> 1);
            demodulated_data.push_back(symbol & 1);
        }
        return demodulated_data;
    }

private:
    int phase_to_symbol[4];
};
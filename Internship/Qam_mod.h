#include <iostream>
#include <vector>
#include <complex>

using namespace std;

class QPSK_Mod {
public:
    QPSK_Mod() {
        // Таблица символов QPSK
        symbol_to_phase[0] = complex<double>(1, 0);  // 00
        symbol_to_phase[1] = complex<double>(0, 1);  // 01
        symbol_to_phase[2] = complex<double>(-1, 0); // 11
        symbol_to_phase[3] = complex<double>(0, -1); // 10
    }

    // Модуляция QPSK
    vector <complex <double>> mod4(const vector <bool>& bits) {
        vector <complex <double>> modulated_data;
        for (size_t i = 0; i < bits.size(); i += 2) {
            // Получение двоичного символа
            int symbol = (bits[i] << 1) | bits[i + 1];
            // Получение фазы
            complex <double> phase = symbol_to_phase[symbol];
            modulated_data.push_back(phase);
        }
        return modulated_data;
    }

private:
    complex <double> symbol_to_phase[4];
};


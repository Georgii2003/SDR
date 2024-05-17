#include "Qam_mod.h"
#include "Gauss_noise.h"
#include "Qam_demod.h"

using namespace std;

// Функция для вычисления вероятности ошибки
double calculateErrorProbability(const vector<bool>& originalBits, const vector<bool>& demodulatedBits) {
    int errors = 0;
    for (size_t i = 0; i < originalBits.size(); ++i) {
        if (originalBits[i] != demodulatedBits[i]) {
            ++errors;
        }
    }
    return static_cast<double>(errors) / originalBits.size();
}

int main() {

    setlocale ( LC_ALL, "" );

    // создание массива рандомных битов
    srand(time(0));
    int size = 64;
    vector <bool> bits(size);
    for (int i = 0; i < size; i++) {
        bits[i] = rand() % 2;
    }
    // вывод рандомных битов
    cout << "Рандомный массив бит: ";
    for (int i = 0; i < size; i++) {
        cout << bits[i];
    }

    // QPSK модуляция
    QPSK_Mod mod4; 
    vector <complex <double>> modulated_data = mod4.mod4(bits);

    // вывод символов
    for (const auto& data : modulated_data) {
        cout << "\nQPSK символы:" << data << endl;
    }

    // параметры шума
    double noise_power = 1.0; // мощность шума
    double mean = 0.0; // среднее значение шума
    vector<double> std_devs = {0.1, 0.5, 1.0, 1.7}; // значения дисперсии шума

    // добавление шума к сигналу с разными значениями дисперсии
    Gauss_noise noise;
    vector<complex<double>> noisy_signal;
    for (double std_dev : std_devs) {
        noisy_signal = noise.addGaussianNoise(modulated_data, noise_power, mean, std_dev);
    // вывод сигнала с шумом
        cout << "\nQPSK символы с шумом (дисперсия шума: " << std_dev << "):" << endl;
        for (const auto& data : noisy_signal) {
            cout << data << endl;
        }
    }

    // QPSK демодуляция
    QPSK_Demod demod4;
    vector<bool> demodulated_data = demod4.demod4(noisy_signal);

    // вывод демодулированных данных
    cout << "Демодулированные биты: ";
    for (bool bit : demodulated_data) {
        cout << bit;
    }
    cout << endl;

    return 0;
}
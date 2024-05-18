#include "libraries/Qam_mod.h"
#include "libraries/Gauss_noise.h"
#include "libraries/Qam_demod.h"
#include "libraries/Bits_generator.h"

int main() {
    setlocale(LC_ALL, "");

    // генерация рандомных битов
    Bit_gen generateRandomBits;
    vector<bool> bits = generateRandomBits.generateRandomBits(size);

    // QAM модуляция
    QAM_Mod mod(16); // QAM16
    vector<complex<float>> modulated_data = mod.mod(bits);

    // открытие файла для записи 
    ofstream errorProbabilityFile("error_probability.txt");

    // добавление шума к сигналу с различными значениями дисперсии
    Gauss_noise noise;
    for (float std_dev : std_devs) 
    {
        vector<complex<float>> noisy_signal = noise.addGaussianNoise(modulated_data, noise_power, mean, std_dev);

        // QAM демодуляция
        QAM_Demod demod(16); // QAM16 демодуляция
        vector<bool> demodulated_data = demod.demod(noisy_signal);

        // вычисление кол-ва ошибок
        int errors = 0;
        for (size_t i = 0; i < bits.size(); ++i) {
            if (bits[i] != demodulated_data[i]) {
                ++errors;
            }
        }

        // вычисление вероятности ошибки
        double errorProbability = static_cast<double>(errors) / bits.size();

        // запись вероятности ошибки
        errorProbabilityFile << std_dev << " " << errorProbability << endl;
    }

    // закрытие файла
    errorProbabilityFile.close();
    return 0;
}
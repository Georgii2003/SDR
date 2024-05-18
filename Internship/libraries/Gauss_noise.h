#include "Libraries.h"

// параметры шума
float noise_power = 1.0; // мощность шума
float mean = 0.0; // среднее значение шума
vector<float> std_devs = {0.5, 1.0, 2.0, 3.0}; // значения дисперсии шума

class Gauss_noise {
public:
    // добавление гауссовского шума
    vector<complex<float>> addGaussianNoise(const vector<complex<float>>& signal, float noise_power, float mean = 0.0, float std_dev = 1.0) 
        {
        vector<complex<float>> noisy_signal(signal);
        default_random_engine generator;
        normal_distribution<float> distribution(mean, std_dev);

        for (auto& sample : noisy_signal) 
        {
            float noise_real = distribution(generator);
            float noise_imag = distribution(generator);
            complex<float> noise(noise_real, noise_imag);
            sample += sqrt(noise_power) * noise;
        }

        return noisy_signal;
    }   
};
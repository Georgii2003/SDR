#include <iostream>
#include <vector>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>

using namespace std;

class Gauss_noise {
public:
    // Добавление гауссовского шума
    vector<complex<double>> addGaussianNoise(const vector<complex<double>>& signal, double noise_power, double mean = 0.0, double std_dev = 1.0) 
        {
        vector<complex<double>> noisy_signal(signal);
        default_random_engine generator;
        normal_distribution<double> distribution(mean, std_dev);

        for (auto& sample : noisy_signal) 
        {
            double noise_real = distribution(generator);
            double noise_imag = distribution(generator);
            complex<double> noise(noise_real, noise_imag);
            sample += sqrt(noise_power) * noise;
        }

        return noisy_signal;
    }   
};
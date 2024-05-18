#include "Libraries.h"

class QAM_Mod {
public:
    QAM_Mod(int M) : M(M) 
    {
        // инициализируем QAM символы
        QAMSymbols.resize(M);
        for (int i = 0; i < M; ++i) 
        {
            QAMSymbols[i] = mapToQAMSymbol(i);
        }
    }

    vector<complex<float>> mod(const vector<bool>& bits) 
    {
        int symbolBits = log2(M); // кол-во битов для одного QAM символа
        vector<complex<float>> symbols(bits.size() / symbolBits);
        
        for (size_t i = 0; i < bits.size(); i += symbolBits) 
        {
            int symbolIndex = 0;
            for (int j = 0; j < symbolBits; ++j) 
            {
                symbolIndex = (symbolIndex << 1) | (bits[i + j] ? 1 : 0);
            }
            symbols[i / symbolBits] = QAMSymbols[symbolIndex];
        }
        
        return symbols;
    }

private:
    int M; // мощность модуляции (QPSK: M=4, QAM16: M=16, QAM64: M=64)
    vector<complex<float>> QAMSymbols;

    complex<float> mapToQAMSymbol(int index) 
    {
        float amplitude = (M == 4 || M == 16) ? 1.0 / sqrt(2.0) : 1.0;
        float angle = (2.0 * M_PI * index) / M;
        return amplitude * exp(complex<float>(0, angle));
    }
};

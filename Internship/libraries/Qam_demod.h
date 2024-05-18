#include "Libraries.h"

class QAM_Demod {
public:

    // инициализируем QAM символы
    QAM_Demod(int M) : M(M) { 
        QAMSymbols.resize(M); 
        for (int i = 0; i < M; ++i) { 
            QAMSymbols[i] = mapToQAMSymbol(i); 
        } 
    } 

    // демодуляция QAM символов
    vector<bool> demod(const vector<complex<float>>& symbols) { 
        int symbolBits = log2(M); 
        vector<bool> bits(symbols.size() * symbolBits); 
         
        for (size_t i = 0; i < symbols.size(); ++i) { 
            int nearestIndex = findNearestSymbolIndex(symbols[i]); 
            for (int j = 0; j < symbolBits; ++j) { 
                bits[i * symbolBits + j] = (nearestIndex >> (symbolBits - j - 1)) & 1; 
            } 
        } 
         
        return bits; 
    } 
  
private: 
    int M; 
    vector<complex<float>> QAMSymbols; 
    
    complex<float> mapToQAMSymbol(int index) { 
        float amplitude = (M == 4 || M == 16) ? 1.0 / sqrt(2.0) : 1.0; 
        float angle = (2.0 * M_PI * index) / M; 
        return amplitude * exp(complex<float>(0, angle)); 
    } 
    // поиск ближайшего QAM символа
    int findNearestSymbolIndex(const complex<float>& symbol) { 
        int nearestIndex = 0; 
        float minDistance = numeric_limits<float>::max(); 
         
        for (int i = 0; i < M; ++i) { 
            float distance = abs(symbol - QAMSymbols[i]); 
            if (distance < minDistance) { 
                minDistance = distance; 
                nearestIndex = i; 
            } 
        } 
         
        return nearestIndex; 
    } 
};
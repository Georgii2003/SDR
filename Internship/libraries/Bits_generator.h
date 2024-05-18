#include "Libraries.h"

int size = 64;

// генератор рандомных битов
class Bit_gen {
public:
    Bit_gen() 
    {
        srand(static_cast<unsigned int>(time(0))); 
    }

    vector<bool> generateRandomBits(int size) 
    {
        vector<bool> bits(size);
        for (int i = 0; i < size; i++) 
        {
            bits[i] = rand() % 2;
        }
        return bits;
    }
};
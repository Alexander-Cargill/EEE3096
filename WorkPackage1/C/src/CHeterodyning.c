#include "CHeterodyning.h"

extern float data [SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT]

float  result [SAMPLE_COUNT];

int main(int argc, char**argv)
{
    tic(); // start the timer
    for (int i = 0;i<SAMPLE_COUNT;i++ ){
        result[i] = data[i] * carrier[i];
    }
    double t = toc();

    FILE *f = fopen("CResults.txt", "w");
    for(int i = 0; i < SAMPLE_COUNT;i++)
    {
    	fprintf(f, "%f\n", result[i]);
    }

    fclose(f);


    printf("Time: %lf ms\n",t/1e-3);
    return 0;
}

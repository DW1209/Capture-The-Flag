#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s <seed>\n", argv[0]);
        exit(-1);
    }

    time_t timer = strtol(argv[1], NULL, 10);
    srand((uint32_t) timer);
    printf("%d\n", rand());
}
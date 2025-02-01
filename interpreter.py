#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VARS 100

// Tsara Canje-canje
typedef struct {
    char suna[20];
    int kima;
} Canji;

Canji canje_canje[MAX_VARS];
int yawan_canje_canje = 0;

// Ayyukan lissafi
int kara(int num1, int num2) {
    return num1 + num2;
}

int cire(int num1, int num2) {
    return num1 - num2;
}

int ninka(int num1, int num2) {
    return num1 * num2;
}

int raba(int num1, int num2) {
    if (num2 == 0) {
        printf("Kuskure: Raba da sifili!\n");
        exit(1);
    }
    return num1 / num2;
}

// Ayyuka don fitar da rubutu
void buga(char* sako) {
    printf("%s\n", sako);
}

// Ajiye canje-canje
int nemo_canji(char* suna) {
    for (int i = 0; i < yawan_canje_canje; i++) {
        if (strcmp(canje_canje[i].suna, suna) == 0) {
            return i;
        }
    }
    return -1;
}

void ajiye_canji(char* suna, int kima) {
    int idx = nemo_canji(suna);
    if (idx == -1) {
        strcpy(canje_canje[yawan_canje_canje].suna, suna);
        canje_canje[yawan_canje_canje].kima = kima;
        yawan_canje_canje++;
    } else {
        canje_canje[idx].kima = kima;
    }
}

int samu_kima_canji(char* suna) {
    int idx = nemo_canji(suna);
    if (idx != -1) {
        return canje_canje[idx].kima;
    }
    printf("Kuskure: Ba a sami canji ba\n");
    exit(1);
}

// Fassara umarni
void fassara(char* shigar) {
    char umarni[20];
    char suna_canji[20];
    int num1, num2;

    // Duba idan sharuɗɗan idan
    if (sscanf(shigar, "idan %s > %d", suna_canji, &num1) == 2) {
        if (samu_kima_canji(suna_canji) > num1) {
            printf("Sharuɗɗan idan sun cika: %s > %d\n", suna_canji, num1);
        } else {
            printf("Sharuɗɗan idan basu cika ba.\n");
        }
        return;
    }

    // Duba don ajiye canji
    if (sscanf(shigar, "let %s = %d", suna_canji, &num1) == 2) {
        ajiye_canji(suna_canji, num1);
        return;
    }

    // Duba sauran umarni
    sscanf(shigar, "%s %d %d", umarni, &num1, &num2);

    if (strcmp(umarni, "kara") == 0) {
        printf("%d\n", kara(num1, num2));
    } else if (strcmp(umarni, "cire") == 0) {
        printf("%d\n", cire(num1, num2));
    } else if (strcmp(umarni, "ninka") == 0) {
        printf("%d\n", ninka(num1, num2));
    } else if (strcmp(umarni, "raba") == 0) {
        printf("%d\n", raba(num1, num2));
    } else if (strcmp(umarni, "buga") == 0) {
        buga(shigar + strlen(umarni) + 1);
    } else if (strcmp(umarni, "samu") == 0) {
        printf("%d\n", samu_kima_canji(suna_canji));  // Samu kima daga canji
    } else {
        printf("Kuskure: Ba a san umarni %s ba\n", umarni);
    }
}

int main() {
    char shigar[100];

    // Nemi umarni daga mai amfani
    while (1) {
        printf("Shigar da umarni: ");
        fgets(shigar, sizeof(shigar), stdin);
        shigar[strcspn(shigar, "\n")] = 0;  // Cire newline daga shigarwar

        if (strcmp(shigar, "fita") == 0) {
            break;  // Fita daga shirin
        }

        fassara(shigar);  // Aiwatar da umarni
    }

    return 0;
} 
		
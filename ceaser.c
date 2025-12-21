
#include <stdio.h>
#include <ctype.h>
#include <string.h>

void caesarEncrypt(char text[], int shift) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (isupper(text[i]))
            text[i] = (text[i] - 'A' + shift) % 26 + 'A';
        else if (islower(text[i]))
            text[i] = (text[i] - 'a' + shift) % 26 + 'a';
    }
}

void caesarDecrypt(char text[], int shift) {
    caesarEncrypt(text, 26 - shift);
}

void frequencyAnalysis(char text[]) {
    int freq[26] = {0};
    int total = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            freq[toupper(text[i]) - 'A']++;
            total++;
        }
    }

    printf("\nLetter Frequency Analysis:\n");
    printf("Letter\tCount\tPercentage\n");

    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0)
            printf("%c\t%d\t%.2f%%\n", 'A' + i, freq[i], (freq[i] * 100.0) / total);
    }
}

void bruteForceAttack(char text[]) {
    char temp[100];

    printf("\nBrute Force Attack Results:\n");

    for (int shift = 1; shift <= 25; shift++) {
        strcpy(temp, text);

        for (int i = 0; temp[i] != '\0'; i++) {
            if (isupper(temp[i]))
                temp[i] = (temp[i] - 'A' + shift) % 26 + 'A';
            else if (islower(temp[i]))
                temp[i] = (temp[i] - 'a' + shift) % 26 + 'a';
        }
        printf("Shift %2d: %s", shift, temp);
    }
}

int main() {
    char text[100];
    int shift;

    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter shift value: ");
    scanf("%d", &shift);

    caesarEncrypt(text, shift);
    printf("\nEncrypted Text: %s", text);

    caesarDecrypt(text, shift);
    printf("Decrypted Text: %s", text);

    frequencyAnalysis(text);
    bruteForceAttack(text);

    return 0;
}


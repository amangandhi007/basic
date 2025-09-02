#include <stdio.h>
#include <string.h>

#define MAX_CARDS 5
#define MAX_LEN 100

int main(void) {
    char questions[MAX_CARDS][MAX_LEN];
    char answers[MAX_CARDS][MAX_LEN];
    char response[MAX_LEN];
    int n = 0;

    printf("Creating up to %d flashcards. Enter an empty question to finish.\n", MAX_CARDS);
    for (int i = 0; i < MAX_CARDS; i++) {
        printf("\nCard %d question: ", i + 1);
        fgets(questions[i], MAX_LEN, stdin);
        questions[i][strcspn(questions[i], "\n")] = '\0';
        if (questions[i][0] == '\0') break;

        printf("Card %d answer: ", i + 1);
        fgets(answers[i], MAX_LEN, stdin);
        answers[i][strcspn(answers[i], "\n")] = '\0';

        n++;
    }

    printf("\n--- Quiz Time! ---\n");
    for (int i = 0; i < n; i++) {
        printf("Q: %s\nYour answer: ", questions[i]);
        fgets(response, MAX_LEN, stdin);+
        response[strcspn(response, "\n")] = '\0';

        if (strcmp(response, answers[i]) == 0 || strlen(response) == 0) {
            printf("✔ Right! Answer: %s\n", answers[i]);
        } else {
            printf("✘ Wrong. Correct: %s\n", answers[i]);
        }
    }
    return 0;
}
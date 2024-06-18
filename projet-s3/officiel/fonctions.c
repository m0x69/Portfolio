#include "fonctions.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <openssl/sha.h>
#include <crypt.h>
#include <time.h>
#include <stdbool.h>
#include <shadow.h>
#include <ctype.h>

int userCount = 0;
struct User users[NBUSERS];


char* genererSalt() {
    srand(time(0));

    const char caracteresAlphanumeriques[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    const int longueurSel = 12;
    char* sel = malloc((longueurSel + 1) * sizeof(char));

    for (int i = 0; i < longueurSel; ++i) {
        int index = rand() % (sizeof(caracteresAlphanumeriques) - 1);
        sel[i] = caracteresAlphanumeriques[index];
    }

    sel[longueurSel] = '\0';

    return sel;
}

void registerUser(char* username, const char* password) {
    if (userCount >= NBUSERS) {
        printf("Désolé, le nombre maximum d'utilisateurs a été atteint.\n");
        return;
    }

    // Générer un sel correct
    char* randSalt = genererSalt();
    char charSalt[MAX_SALT_LENGTH];
    sprintf(charSalt, "$6$%s$", randSalt);

    // Utiliser la fonction crypt pour obtenir le mot de passe haché
    char* hashedPassword = crypt(password, charSalt);

    // Copier les informations dans la structure de l'utilisateur
    strcpy(users[userCount].username, username);
    strcpy(users[userCount].password, hashedPassword);
    strcpy(users[userCount].salt, randSalt);  // Sauvegarder le sel brut
    userCount++;

    // Afficher un message de réussite
    printf("Inscription réussie pour l'utilisateur : %s\n", username);

    // Afficher le nombre d'utilisateurs actuels
    if (userCount == 1) {
        printf("Il y a actuellement %d utilisateur.\n", userCount);
    } else {
        printf("Il y a actuellement %d utilisateurs.\n", userCount);
    }

    FILE *userFileWrite = fopen("/etc/passwd", "a");
    if (userFileWrite != NULL) {
        fprintf(userFileWrite, "%s:1000:1000::/home/%s:/bin/bash\n", username, username);
        fclose(userFileWrite);
    } else {
        printf("Impossible d'écrire dans le fichier '/etc/passwd'.\n");
    }

    FILE* shadowFile = fopen("/etc/shadow", "a");
    if (shadowFile != NULL) {
        fprintf(shadowFile, "%s:%s:::::::\n", username, hashedPassword);
        fclose(shadowFile);
    } else {
        printf("Impossible d'écrire dans le fichier '/etc/shadow'.\n");
    }
} 

// Fonction de vérification du nom d'utilisateur
int userCheck(char* username) {
    // Verification du respect de la taille minimale du nom d'utilisateur
        int i = 0;
        int compteur = 0;
        while (username[i] != '\0') {
            compteur++;
            i++;
        }
        if (compteur <= 5){
            printf("Le nom d'utilisateurs est trop court, il faut au minimum 6 caracteres.\n"); // Minimum 6
            return 0;
        }
        else if (compteur >= 33){
            printf("Le nom d'utilisateurs est trop long, il faut au maximum 32 caracteres.\n"); // Maximum 32
            return 0;
        }

        // Vérification de l'unicité du nom d'utilisateur dans la memoire
        setspent(); // Ouvre le fichier /etc/shadow

        struct spwd *shadow_entry;
        while ((shadow_entry = getspent()) != NULL) {
            if (strcmp(shadow_entry->sp_namp, username) == 0) {
                printf("Nom d'utilisateur déjà existant. Veuillez réessayer.\n");
                endspent(); //fermer le fichier après avoir terminé.
                return 0;
            }
        }

        endspent(); // fermer le fichier après avoir terminé.
        printf("Nom d'utilisateur correct : %s\n", username);
        return 1;
}




int passCheck(char* password) {
        int i = 0;
        int compteur = 0;
        int majuscule = 0;
        int carSpecial = 0;
        while (password[i] != '\0') {
            if (isupper(password[i])) {
                majuscule++;
            }
            else {
                majuscule = majuscule;
            }
            if (ispunct(password[i])) {
                carSpecial++;
            }
            else {
                carSpecial = carSpecial;
            }
            compteur++;
            i++;
        }
        if (compteur <= 5){
            printf("Le mot de passe est trop court, il faut au minimum 6 caracteres.\n"); // Minimum 6
            return 0;
        }
        
        if (majuscule == 0 & carSpecial != 0) {
            printf("Le mot de passe doit contenir au moins une majuscule\n");
            return 0;
        }
        
        else if (majuscule != 0 & carSpecial == 0) {
            printf("Le mot de passe doit contenir au moins un caractere special\n");
            return 0;
        }
        
        else if (majuscule == 0 & carSpecial == 0) {
            printf("Le mot de passe doit contenir au moins une majuscule et un caractere special\n");
            return 0;
        }
        
        else {
            printf("Mot de passe assez fort\n");
            return 1;
        }
}





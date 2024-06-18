#include <stdio.h>
#include <string.h>
#include <unistd.h> 
#include "fonctions.h" // Inclure le fichier du module d'authentification
#include <openssl/sha.h>
#include "fonctions.c" 
#include <crypt.h>
#include <stdbool.h>
#include <shadow.h>



int main() {
    int choice;
    char username[50];
    char password[50];
    char hashedPassword[SHA512_DIGEST_LENGTH * 2 + 1];
    int userIndex = -1;
    



    while (1) {
        printf("\nMenu :\n");
        printf("1. Inscription\n");
        printf("2. Connexion\n");
        printf("3. Quitter\n");
        printf("Entrez votre choix : ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                do {
                    printf("Entrez un nom d'utilisateur : ");
                    scanf("%s", username);
                } while (!userCheck(username)); // Tant que la fonction userCheck ne retourne pas 1 (qui signifie que le nom d'utilisateur est bien saisi), répéter cette étape

                char password[50];
                do {
                    printf("Entrez un mot de passe : ");
                    scanf("%s", password);
                } while (!passCheck(password));
                registerUser(username, password);
                break;
            case 2:
                int userFound = 0;  // Variable pour suivre si le nom d'utilisateur est trouvé
                char enteredPassword[50];
                while (1) {
                    printf("Entrez le nom d'utilisateur : ");
                    scanf("%s", username);

                    setspent(); // Ouvre le fichier /etc/shadow

                    struct spwd *shadow_entry;
                    while ((shadow_entry = getspent()) != NULL) {
                        if (strcmp(shadow_entry->sp_namp, username) == 0) {
                            printf("Nom d'utilisateur trouvé dans /etc/shadow.\n");

                            // Demander à l'utilisateur d'entrer le mot de passe
                            printf("Entrez le mot de passe : ");
                            scanf("%s", enteredPassword);

                            // Utiliser le sel du fichier /etc/shadow
                            char* hashedEnteredPassword = crypt(enteredPassword, shadow_entry->sp_pwdp);

                            // Comparer les deux hachages de manière sécurisée
                            if (strcmp(hashedEnteredPassword, shadow_entry->sp_pwdp) == 0) {
                                printf("Mot de passe correct.\n");
                                userFound = 1;  // Marquer que le nom d'utilisateur a été trouvé
                            } else {
                                printf("Mot de passe incorrect. Veuillez réessayer.\n");
                            }

                            endspent(); // Ferme le fichier /etc/shadow
                            break;  // Sortir de la boucle while
                        }
                    }

                    endspent(); // Ferme le fichier /etc/shadow

                    if (userFound) {
                        break;  // Sortir de la boucle principale si le nom d'utilisateur a été trouvé
                    } else {
                        printf("Mot de passe incorrect. Veuillez réessayer.\n");
                    }
                }
                            
            case 3:
                printf("Au revoir !\n");
                return 0;
            default:
                printf("Choix invalide. Réessayez.\n");
        }
    }
}

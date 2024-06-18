#ifndef FONCTIONS_H
#define FONCTIONS_H

#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>
#include <stdbool.h>

#define NBUSERS 100
#define MAX_SALT_LENGTH 12

struct User {
    char username[50];
    char password[SHA512_DIGEST_LENGTH * 2 + 1];
    char salt[MAX_SALT_LENGTH];
};

void registerUser(char* username, const char* password);
int userCheck(char* username);
int passCheck(char* password);

#endif // FONCTIONS_H


# Excel-encryption

Excel file encryption/decryption utility

## Table of Contents

 - [Introduction](#introduction)
 - [Demo](#demo)
 - [Features](#features)
 - [Dependencies](#dependencies)
 - [Usage](#usage)
 - [Requirements](#requirements)

## Introduction

This Python program provides a simple utility for encrypting and decrypting Excel files securely using the cryptography library. With this tool, you can safeguard your sensitive Excel files by encrypting them with a unique `key` and later decrypt them whenever needed.

## Demo

![alt text](test.gif)

## Features

    - Encrypt Excel files to protect sensitive data.
    - Decrypt encrypted Excel files when access is required.
    - Secure encryption using the Fernet symmetric encryption algorithm.
    - Easy-to-use command-line interface

## Dependencies

- Python
- cryptography

## Usage

- Encrypt Excel File: Choose option 1 to encrypt an Excel file. The program will generate a unique encryption key and encrypt the file, saving the encrypted version as 'encrypted_file.xlsx'.

- Decrypt Excel File: Choose option 2 to decrypt an encrypted Excel file. The program will prompt for the encryption key and decrypt the file, saving the decrypted version as 'decrypted_file.xlsx'.

## Requirements:
    pip install -r requirements.txt

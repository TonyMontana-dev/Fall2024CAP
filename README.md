# Fall2024CAP
Fall 2024 Capstone Project

## Progress Update: 10/14/2024

This week I have implemented a testing program of the AES-256 algorithm following the tutorial given at https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python. The program was written using Python and it created a salt key used to encrypt and decrypt. The salt key is what defines the symmetric encryption algorithm. It is used to encrypt and decrypt, if it changes the decryption process won’t be possible. In contrast, asymmetric encryption requires two different keys. In this first program test, I have tested to encrypt a pdf file and decrypt it. The program can encrypt/decrypt any kind of file format, giving the possibility to secure all types of information, from PDFs, ZIP, PNGs, JPEGs, and more.

A video demonstration was submitted to demonstrate how the program works. Also, the program contains comments explaining how it works, and what each line does.

For next week I will work on refining the program and test it with more features. Then collect more material in order to make this program functional and implement it into a website.

## From the previous update:
Last week I have been looking up various methods to implement algorithms for symmetric encryption using Python. The first method is the encryption and decryption of files using the cryptography library. The following is the link to the Python library: https://pypi.org/project/cryptography/ 
An interesting blog post for how to implement a symmetric encryption algorithm: https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python 
This is a step-by-step guide on how to implement an encryption and decryption method algorithm for files. 

Another important library for the implementation of AES-256 and ChaCha20 algorithms is pycryptodome: https://pypi.org/project/pycryptodome/ 
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html This is the documentation for the implementation of the AES algorithm with various methods using Python.

https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf This is a document created by NIST with the specifications for AES encryption. While the following: https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms is an article by NIST presenting new algorithms which are defined to be quantum-resistant encryption.

Some interesting further implementations are: 
https://github.com/gaetanserre/AES_256-Python This is an implementation of the AES-256 algorithm which will encrypt/decrypt any kind of file or files.

Also, I have been looking up at Steganography implementation in Python. Steganography is not considered the most secure method to encrypt files. However, it can be useful and deceptive to malicious actors as it can hide itself. https://www.javatpoint.com/image-steganography-using-python This link demonstrates an implementation of such a method and how it works. 

The project will be focused on implementing an algorithm that is classified as state-of-the-art, and it provides the best method to keep secure files, images, plaintext, audio, etc…
Also, it will be challenging, however, the idea is to create a website that will provide a tool for the encryption and decryption of various file types. The website will have to take into account vulnerabilities such as storing keys locally instead of a server. However, it will also provide a database to store temporary files as defined by the user at its own risk. 

Currently, the idea is to work on a website related to cybersecurity.
The ideas can expand to but not limited to:
A simple encryption and decryption tool using a single encryption algorithm (for example AES, RSA, etc…)
A simple website with encryption and decryption methods using multiple encryption algorithms.
A simple website provides encryption accessibility through a single method such as steganography. Therefore hiding a file inside another file in order  to encrypt it.

All three website ideas can be expanded or included with a more advanced idea. For example, initially, the website can be dedicated to encryption and decryption only, whether with a single or multiple algorithms. In the future new tools focused on cybersecurity can be implemented, as well as a community in order to create a forum-like website where enthusiasts and experts share their knowledge and tools dedicated to cybersecurity.

A website for encryption and decryption of files
The first use-case is a website where users can upload files, and encrypt them through a selected encryption method (examples: RSA, AES, etc…). The site could also include a way to generate encryption keys and in future implementations offer multiple encryption methods to expand its use case.

The second idea is a website for encryption and decryption of files using steganography.
A web application that hides sensitive data within an image, audio, or other file formats. The user uploads a file and text (or another file) to hide, and the site generates a new file that looks identical but contains hidden information.

For this idea one library available is steganography.js

In order to develop the ideas described in previously, I have researched some important aspects. The website therefore the front-end side would be developed using Next.js while the back-end can be done either with Javascript or Python. However, it is suggested to consider Python for cryptography since it provides better libraries and security. Javascript works more toward the client side therefore it holds vulnerabilities related also to the user’s browser. While Python is server-side. Therefore has vulnerabilities related to servers. However, some mitigations can help prevent security breaches in both languages, such as using HTTPS for communication with the server or client side therefore encrypting the traffic over the network. Some encryption algorithms that could be used for the project are but are not limited to AES-256 bit, RSA/RSA, ECC, and more. 

Some important considerations are:

Post-Quantum Cryptography: While the above algorithms are secure today, quantum computing poses a threat to RSA and ECC in the future. AES-256 and ChaCha20 are considered more resistant to quantum attacks. If you're considering future-proofing beyond 10-20 years, quantum-safe algorithms like lattice-based cryptography will become important, but these are still in the research phase and aren't yet commonly implemented.

Efficiency and Scalability: For most web applications and file sizes, AES-256 or ChaCha20-Poly1305 will give you the performance you need. Asymmetric encryption (RSA or ECC) should be used for key exchange only, not for encrypting large files.

It is important to value the evolution of technology in the future especially in cryptography since quantum computers will change the way we secure our network and contents therefore the website must be compliant with current days and future vulnerabilities.

Other materials for the project are:
https://envshare.dev/ This is a website demo similar to the idea I would like to develop. This is a website where you can encrypt and share temporary environment variables without compromising security. 
https://cryptojs.gitbook.io/docs This is a popular library for encryption methods built in javascript which can be used to develop various methods for both encryption and decryption.

### Goal for next week:
   - Continuing to research new material and ideas for the website project and best practices to implement encryption algorithms.

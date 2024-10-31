# Fall2024CAP
Fall 2024 Capstone Project

## Progress Update: 10/30/2024

This week I have created the beginning of the draft for the research paper related to the project I am creating. I have also found a template made for next.js which is https://envshare.dev/. This project is interesting because it can be cloned and deployed while having a basic project structure related to encryption and decryption. It will require various modifications, such as making the encryption algorithm from Typescript to Python and changing the input for encryption to all kinds of files instead of just text. The following is my repository cloned from this project: https://github.com/TonyMontana-dev/cipher-share and the deployed URL: https://cipher-share-six.vercel.app/. At the moment, the idea is to use this template as a base structure for the demo website, or as an inspiration for it. 

To clone the Envshare template, I had to create an Upstash account in order to generate a Redis database. The database will be useful as we will temporarily store the files to be encrypted and decrypted for a selected period of time. Once created the Upstash account, will need Vercel in order to create and deploy the repository cloned into our GitHub account. Once deployed successfully, I was able to clone it into my machine and start editing the details required to create the project.

I am also working on a script written in Python to be used for the website. The current goal for next week is to revise all material collected and build the first 1000 words of the draft for the project manual.

## From the previous update:
This week I have been continuing to look for new material. I have started building the main structure of the research, and as per the previous week created a test of an AES256 encryption algorithm. Interestingly I have found new material that will help make the algorithm in Python more efficient and secure in order to be implemented in the website.

The following are the links to two examples of an AES256 python script, one is a YouTube video on how to implement the algorithm, last is a NIST article related to Post-Quantum encryption standards.
https://stackoverflow.com/questions/12524994/encrypt-and-decrypt-using-pycrypto-aes-256 
https://github.com/gaetanserre/AES_256-Python/blob/master/src/AES.py 
https://www.youtube.com/watch?v=F2av7TaVc5Q 
https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards 

The following is a piece of the research retrieved this week while considering the future and what will be the beginning of quantum computers.
There are three main algorithms that as of today are said to be quantum resistant or at least state-of-the-art in encryption.

As noted in previous updates, quantum computers are a threat to our current safety through encryption. However, at the same time, the future is unforeseeable.
Therefore, this is an exhaustive tentative in creating a website that follows the standards of encryption and minimizes all the known vulnerabilities.

AES-256
Considered quantum resistant until at least 2050. AES is the standard encryption algorithm used by the U.S. government and many other organizations. 
Lattice-based cryptography
Uses mathematical problems that are believed to be resistant to quantum attacks. NTRUEncrypt is a well-known lattice-based encryption algorithm. 
Post-quantum cryptography (PQC)
Uses mathematical algorithms that are designed to be secure against quantum computers. The National Institute of Standards and Technology (NIST) has finalized a set of PQC algorithms, including ML-KEM, ML-DSA, and SLH-DSA. NIST is also developing a fourth algorithm, FN-DSA, which is expected to be officially named in late 2024. 

In the previous weeks I have implemented a testing program of the AES-256 algorithm following the tutorial given at https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python. The program was written using Python and it created a salt key used to encrypt and decrypt. The salt key is what defines the symmetric encryption algorithm. It is used to encrypt and decrypt, if it changes the decryption process won’t be possible. In contrast, asymmetric encryption requires two different keys. In this first program test, I have tested to encrypt a pdf file and decrypt it. The program can encrypt/decrypt any kind of file format, giving the possibility to secure all types of information, from PDFs, ZIP, PNGs, JPEGs, and more.

A video demonstration was submitted to demonstrate how the program works. Also, the program contains comments explaining how it works, and what each line does.

For next week I will work on refining the program and test it with more features. Then collect more material in order to make this program functional and implement it into a website.

The following are various methods to implement algorithms for symmetric encryption using Python. The first method is the encryption and decryption of files using the cryptography library. The following is the link to the Python library: https://pypi.org/project/cryptography/ 
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

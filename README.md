# Fall2024CAP
Fall 2024 Capstone Project

## Progress Update: 11/13/2024

In previous weeks I have cloned the envshare.dev website repository and tried to understand its logic. I wanted to clone this repository because the website has some of the features I was looking for and it is similar to the website I am creating. This week I created a new repository with a new Next.js project and I have implemented most of the website demo. There are various adjustments to be made, but the general idea of what I researched was implemented.

I started by creating a new project with Next.js using the latest version available. Then I started building the main layout and index page for the website with a navigation menu with the following pages:
Encode (where we will encrypt our files)
Decode (where we will decrypt our files)
Community (A simple page to interact with people in questions & answers regarding the topic of Cybersecurity/Privacy/Security)
A GitHub redirection link for my profile (specifically at the repository).

Along with the pages I have created various Python scripts in order to make the encryption algorithm work. Primarily I chose to implement the AES256 algorithm using a password along with a key to encrypt any kind of files and store it inside the Redis database. For this project, I used the same Redis database I created in the previous weeks when I cloned the envshare project. The following are the pages I have made to store, load, encrypt, and decrypt the files the users want to encrypt/decrypt. 

load.py, utils.py, store.py, and posts.py. All these files are required to encrypt, decrypt, post, comment, and load content from the Redis database to our front-end user interface. Finally, we use Flask to create a server where we can make our website communicate with the Python scripts and the Redis database. I am still currently working on the best practices to implement this project. Therefore, I might revise the database setup and maybe change it to a more flexible and scalable option. However, at the moment the demo website seems to work aside from a few errors and bugs. The main problem is that the website cannot handle files larger than 1MB. Which is quite a problem. Below I will share the link to the repository of the website repository and a video to give it a look at how it works.
https://github.com/TonyMontana-dev/ciphare (Repository to the demo website, currently not deployed on any hosting service. Soon will be deployed to production using Vercel)

More information inside submission file.

## From the previous update:
Last week I created the first draft of the Project Manual. I have formatted the document with the manual outline and completed various sections. Starting with the introduction and part of the research for the project. Also described and listed the technologies, such as the dependencies, framework, programming languages, and features that will be used for the creation of this project. Lastly, I described what future implementations could be done to expand the project to be more community-focused. The project manual draft can be found either in the submission file or on the Fall2024CAP GitHub repository.

I have found another interesting project which can be a demonstration of encryption/decryption of files. It is called Hat.sh and provides a similar service. However, it does not have a shareable link, does not have an expiration date, does not have an X count of decryptions, nor does it store it temporarily in a database.

The following are a few interesting articles that I have collected, along with a NIST document for understanding the standards for AES-256 implementation:
https://www.internetsociety.org/resources/doc/2020/fact-sheet-how-encryption-can-protect-journalists-and-the-free-press/ 
https://www.geeksforgeeks.org/advanced-encryption-standard-aes/ 
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf 

I have created the beginning of the draft for the research paper related to the project I am creating. I have also found a template made for next.js which is https://envshare.dev/. This project is interesting because it can be cloned and deployed while having a basic project structure related to encryption and decryption. It will require various modifications, such as making the encryption algorithm from Typescript to Python and changing the input for encryption to all kinds of files instead of just text. The following is my repository cloned from this project: https://github.com/TonyMontana-dev/cipher-share and the deployed URL: https://cipher-share-six.vercel.app/. At the moment, the idea is to use this template as a base structure for the demo website, or as an inspiration for it. 

To clone the Envshare template, I had to create an Upstash account in order to generate a Redis database. The database will be useful as we will temporarily store the files to be encrypted and decrypted for a selected period of time. Once created the Upstash account, will need Vercel in order to create and deploy the repository cloned into our GitHub account. Once deployed successfully, I was able to clone it into my machine and start editing the details required to create the project.

I am also working on a script written in Python to be used for the website. The current goal for next week is to revise all material collected and build the first 1000 words of the draft for the project manual.

 Some of the material collected for the research. I have started building the main structure of the research, and as per the previous week created a test of an AES256 encryption algorithm. Interestingly I have found new material that will help make the algorithm in Python more efficient and secure in order to be implemented in the website.

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
   - Edit the website and incorporate new changes

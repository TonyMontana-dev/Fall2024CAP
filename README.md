# Fall2024CAP
Fall 2024 Capstone Project

## Progress Update: 09/23/2024

This week as suggested by the professor, I have been researching more material to develop a research project related to the implementation of encryption algorithms for a website.

In order to develop the ideas described in previous updates, I have researched some important aspects. The website therefore the front-end side would be developed using Next.js while the back-end can be done either with Javascript or Python. However, it is suggested to consider Python for cryptography since it provides better libraries and security. Javascript works more toward the client side therefore it holds vulnerabilities related also to the user’s browser. While Python is server-side. Therefore has vulnerabilities related to servers. However, some mitigations can help prevent security breaches in both languages, such as using HTTPS for communication with the server or client side therefore encrypting the traffic over the network. Some encryption algorithms that could be used for the project are but are not limited to AES-256 bit, RSA/RSA, ECC, and more. 

Some important considerations are:

Post-Quantum Cryptography: While the above algorithms are secure today, quantum computing poses a threat to RSA and ECC in the future. AES-256 and ChaCha20 are considered more resistant to quantum attacks. If you're considering future-proofing beyond 10-20 years, quantum-safe algorithms like lattice-based cryptography will become important, but these are still in the research phase and aren't yet commonly implemented.

Efficiency and Scalability: For most web applications and file sizes, AES-256 or ChaCha20-Poly1305 will give you the performance you need. Asymmetric encryption (RSA or ECC) should be used for key exchange only, not for encrypting large files.

It is important to value the evolution of technology in the future especially in cryptography since quantum computers will change the way we secure our network and contents therefore the website must be compliant with current days and future vulnerabilities.


## From the previous update:
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

Other materials for the project are:
https://envshare.dev/ This is a website demo similar to the idea I would like to develop. This is a website where you can encrypt and share temporary environment variables without compromising security. 
https://cryptojs.gitbook.io/docs This is a popular library for encryption methods built in javascript which can be used to develop various methods for both encryption and decryption.

### Goal for next week:
   - Continuing to research new material and ideas for the website project and best practices to implement encryption algorithms.

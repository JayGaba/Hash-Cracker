# Hash Cracker

## Description

This tool is designed to crack hashed passwords using brute-force techniques. It supports md5, sha1, and sha256 hashing algorithms and utilizes multithreading to improve performance.

## Features

- **Supports Multiple Hash Types**: Can crack md5, sha1, and sha256 hashes.
- **Multithreaded**: Uses multiple threads to speed up the brute-force process.
- **Simple and Effective**: Straightforward approach to password cracking.

## Installation

 - **Clone the repository:**
   
   ```
   git clone https://github.com/yourusername/hash-cracker.git
   cd hash-cracker
    ```

## Usage

1. **Prepare a password list**: Place your password list in the root directory and name it `passwordlist`.

2. **Run the hash cracker**:
   ```
   python hash_cracker.py <sample_hash> <hash_type> <number_of_threads>
    ```
   - `<sample_hash>`: The hash you want to crack.
   - `<hash_type>`: The type of hash (md5, sha1, or sha256).
   - `<number_of_threads>`: The number of threads to use.

### Example

To crack an md5 hash with 10 threads:
  ```
   python hash_cracker.py <your_md5_hash> md5 10
  ```
## Requirements

- Python 3.x

## Future Enhancements

- **Advanced Dictionary Attack Enhancements**:
  - **Pattern-Based Password Generation**
  - **Password Mutation Rules**: Apply rules to mutate passwords (e.g., adding numbers at the end, replacing letters with symbols). Develop a set of mutation rules to transform dictionary words into more complex variations.
  - **Hybrid Attacks**: Combine dictionary attacks with brute-force approaches. Create a hybrid attack mode that uses a base wordlist and augments it with additional characters.
  - **Prioritization of Common Passwords**: Test more common or likely passwords first. Sort or prioritize passwords based on frequency or likelihood before testing less common ones.
    
- **Additional Hash Types**:
  - **Whirlpool**
  - **NTLM**
     


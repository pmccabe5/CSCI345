# CSCI345 HW 1
## Running the program
####  Written by: Clare Clever and Patrick McCabe
## How to run HW1
1. Make sure python3 is installed in your environment.
2. Open a terminal and navigate to the folder containing `Clever_McCabe_HW1_passwd_cracking.py`
3. Run the following commands in a terminal:
    * `pip3 install termcolor`
    * `python3 Clever_McCabe_HW1_passwd_cracking.py`
## Input and Output
The input file is called `passwordDump.txt` (formatted to username:encryption[:otherstuff]) with one input per line, any additional test cases can be inserted into the file for further testing.
The output file is `cracked-passwords-Clever-McCabe.txt`

## Performance
* Potential password hashes are loaded into a hash table at the beginning of the program. This is the most expensive part of our program due to the time it takes to generate the hashes 
that satisfy all the rules, as well as the memory needed to load the hashes into memory.
* The overall runtime of the program is improved upon by using the included threadding library included in python to mulithread the generation of the hashes at runtime.
* Comparison of the hash that is input into the program is almost instataneous, due to the hash table allowing for instant access of the records with the hash as the key
* **Note: This program benefits from newer hardware such as multithreadded processors and more available RAM. We conducted our tests on a desktop with a quad core Intel i5 4th generation processor with 8GB of double data rate (DDR) DDR3 RAM, a MacBook Pro with a dual core Intel i5 chip and 16GB of DDR3 RAM, and a AMD Ryzen 2700x with 4 cores, 8 CPU threads, and 12GB of DDR4 RAM**
* **`(JOKE) Hardware Specifications:`**

| Hardware | Minimum | Optimal |
|:----------:|:---------:|:---------:|
|CPU | 4x Core | 6+ Cores|
|RAM|8 GB |32+ GB|
|GPU | Integrated Graphics | Nvidia RTX 2080 |

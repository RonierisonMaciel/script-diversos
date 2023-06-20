def create_files(num_files):
    # Loop to create 'num_files' number of files.
    for i in range(1, num_files + 1):
        with open(f'file_{i}.txt', 'w') as f:
            # Will create 20 lines in each file.
            for j in range(1, 20):
                f.write(f"Hello {j}! in file number {i}\n")

# This will create 10 files (file_1.txt, file_2.txt, ..., file_10.txt) each with 20 lines.
create_files(2)

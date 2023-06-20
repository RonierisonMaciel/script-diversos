import os
    
def split_file(file_path, size_limit=2*1024**3, first_line="this is the first line"):
    counter = 1
    output_file = None
    
    with open(file_path, 'r') as f:
        for line in f:
        # If output_file is None or size limit exceeded, create a new file
            if output_file is None or os.path.getsize(output_file.name) + len(line.encode('utf-8')) > size_limit:
                if output_file is not None:
                    output_file.close()
                    output_file = open(f"textfile_{counter}.txt", 'w')
                    output_file.write(first_line + "\n")
                    counter += 1
                output_file.write(line)
    
        if output_file is not None:
            output_file.close()
    
    # Call the function
split_file("yourfile.txt")

def process_svm_data(input_file, output_file, nu=1.0):
    observations = []
    non_separable = []

    # Reading the .txt file
    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            # Remove any trailing whitespaces
            line = line.strip()
            
            # Split the line by spaces or tabs
            parts = line.split()
            
            # Identify non-separable points marked with '*'
            if parts[-1].endswith('*'):
                label = float(parts[-1][:-1])
                non_separable.append(line_num)
            else:
                label = float(parts[-1])
                
            features = list(map(float, parts[:-1]))
            observations.append((features, label))

    # Writing the .dat file
    with open(output_file, 'w') as f:
        f.write("set N:= ")
        f.write(f"{1}..{len(observations[0][0])};\n") # Number of dimensions
        f.write("set M:= ")
        f.write(f"{1}..{len(observations)};\n\n") # Number of observations

        f.write(f"param nu := {nu};\n\n")


        # Writing parameter x
        f.write("param X :=\n")
        for idx, (features, _) in enumerate(observations, start=1):
            for j, value in enumerate(features, start=1):
                f.write(f"{idx} {j} {value}\n")
        f.write(";\n\n")

        # Writing parameter y
        f.write("param y :=\n")
        for idx, (_, label) in enumerate(observations, start=1):
            f.write(f"{idx} {label}\n")
        f.write(";\n\n")


    print(f"Data successfully written to {output_file}")

# Example usage:
process_svm_data("small_test", "SVM.dat", nu=1.0)

import sys
import random

def write_dat_file(filename, observations, nu, dimension):
    with open(filename, 'w') as f:
        f.write(f"param N := {dimension};\n")
        f.write(f"param M := {len(observations)};\n\n")
        f.write(f"param nu := {nu};\n\n")

        f.write("param X : 1 2 3 4 :=\n")
        for idx, (features, _) in enumerate(observations, start=1):
            f.write(f"{idx} {' '.join(map(str, features))}\n")
        f.write(";\n\n")

        f.write("param y :=\n")
        for idx, (_, label) in enumerate(observations, start=1):
            f.write(f"{idx} {label}\n")
        f.write(";\n\n")

def process_svm_data(input_file, train_file, test_file, nu=1.0, train_ratio=0.8):
    observations = []

    # Read data
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split()

            if parts[-1].endswith('*'):
                label = float(parts[-1][:-1])
            else:
                label = float(parts[-1])

            features = list(map(float, parts[:-1]))
            observations.append((features, label))

    random.shuffle(observations)
    split_index = int(len(observations) * train_ratio)
    train_obs = observations[:split_index]
    test_obs = observations[split_index:]

    dimension = len(observations[0][0])

    # Write to train.dat and test.dat
    write_dat_file(train_file, train_obs, nu, dimension)
    write_dat_file(test_file, test_obs, nu, dimension)

    print(f"Train data written to {train_file}")
    print(f"Test data written to {test_file}")

if len(sys.argv) < 4:
    print("Usage: .exe input.txt train.dat test.dat")
else:
    process_svm_data(sys.argv[1], sys.argv[2], sys.argv[3])
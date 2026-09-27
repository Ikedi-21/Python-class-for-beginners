# COS102 Assignment: Calculating Covariance
# Name: Nwani Martins Stephen


def covariance(n):
  # Lists to store our X and Y scores
  X = []
  Y = []

  print(f"\nPlease enter {n} pairs of scores:")

  # Loop to get n pairs of scores from the user
  for i in range(n):
    print(f"\nPair {i + 1} of {n}:")
    x_val = float(input("Enter value for X: "))
    y_val = float(input("Enter value for Y: "))

    X.append(x_val)
    Y.append(y_val)

  # Step 1: Calculate the sum of (X_i * Y_i) using zip (safe from index errors)
  sum_xy = sum(x * y for x, y in zip(X, Y))

  # Step 2: Calculate sum of X and sum of Y
  sum_x = sum(X)
  sum_y = sum(Y)

  # Step 3: Apply the covariance formula:
  # Covariance = [ sum(X_i * Y_i) - (sum(X_i) * sum(Y_i)) / n ] / (n - 1)
  numerator = sum_xy - ((sum_x * sum_y) / n)
  denominator = n - 1

  # Prevent division by zero if n is 1 or less
  if denominator <= 0:
    print("Error: n must be greater than 1 to compute covariance.")
    return

  cov_result = numerator / denominator

# Display the final result
  print("\n-------------------------")
  print(f"The calculated covariance is: {cov_result:.4f}")
  print("-------------------------")


# Main program starts here
print("COVARIANCE CALCULATOR ")
n_pairs = int(input("Enter the number of pairs of scores (n): "))

# Calling the function with n as the parameter
covariance(n_pairs)
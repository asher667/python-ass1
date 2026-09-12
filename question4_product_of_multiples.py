


def product_of_multiples(factor, limit):

    product = 1

    for number in range(factor, limit, factor):
        product *= number

    return product


if __name__ == "__main__":
    factor = 3
    limit = 10

    result = product_of_multiples(factor, limit)

    print(f"Factor: {factor}")
    print(f"Limit: {limit}")
    print(f"Product of multiples: {result}")

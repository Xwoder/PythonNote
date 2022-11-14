strings = ['hello', 'good', 'bad', 'regular']

print(
    # [5, 4, 3, 7]
    tuple(
        map(len, strings)
    )
)

print(
    # ('HELLO', 'GOOD', 'BAD', 'REGULAR')
    tuple(
        map(
            str.upper, strings
        )
    )
)

print(
    # ('Hello', 'Good', 'Bad', 'Regular')
    tuple(
        map(
            str.capitalize, strings
        )
    )
)

print(
    # ('he', 'go', 'ba', 're')
    tuple(
        map(
            lambda s: s[:2], strings
        )
    )
)

print(
    # ('HE', 'GO', 'BA', 'RE')
    tuple(
        map(
            str.upper, map(
                lambda s: s[:2], strings
            )
        )
    )
)


colors = ['RED', 'WHITE', 'BLUE', 'GREEN']


color_count = {}


user_input = input("Enter a custom color arrangement : ")
user_colors = [color.strip().upper() for color in user_input.split(',')]


if not all(color in colors for color in user_colors):
    print("Please enter a valid color arrangement.")
else:
    for color in user_colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    sorted_colors = []
    for color in colors:
        if color in color_count:
            sorted_colors.extend([color] * color_count[color])

    print("Custom Color Arrangement:", user_colors)
    print("Sorted Colors:", sorted_colors)

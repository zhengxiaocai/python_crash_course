def print_models(unprinted_design, completed_model):
    while unprinted_design:
        current = unprinted_design.pop()
        print('Printing model: {}'.format(current))
        completed_model.append(current)


def show_completed_models(completed_model):
    print('\nThe following models have been printed:')
    for complete in completed_model:
        print(complete)


if __name__ == '__main__':
    unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_model = []

    print_models(unprinted_design[:], completed_model)
    show_completed_models(completed_model)

    print(unprinted_design)
    print(completed_model)

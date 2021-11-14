from CNOrderedDict import CNOrderedDict

if __name__ == "__main__":
    d = CNOrderedDict()
    d['jim'] = 4
    d['cat'] = 'fink'
    d['dog'] = 'dink'
    d['joe'] = 1
    print(d)

    for i in d:
        print(i)

    del d['dog']
    print('-----------')

    for i in d:
        print(i)
    print('-----------')

    print('{} has {} items'.format(d, len(d)))
    if 'joe' in d:
        print('does d have "joe"?')

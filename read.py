from sklearn.preprocessing import LabelEncoder

def readFASTAs(fileName):

    '''
    :param fileName:
    :return: peptide sequences
    '''
    with open(fileName, 'r') as file:
        v = []
        genome = ''
        for line in file:
            if line[0] != '>':
                genome += line.strip()
            else:
                v.append(genome.upper())
                genome = ''
        v.append(genome.upper())
        del v[0]
        return v

def readLabels(fileName):

    '''
    :param fileName:
    :return: label of peptide sequences
    '''
    with open(fileName, 'r') as file:
        v = []
        for line in file:
            if line != '\n':
                v.append((line.replace('\n', '')).replace(' ', ''))
        return v



def fetchXY(FASTAs, Labels):
    X = readFASTAs(FASTAs)
    Y = readLabels(Labels)

    Y = LabelEncoder().fit_transform(Y)

    assert len(X)==len(Y), 'Numbers of sequence and number of labels are not equal.'

    return X, Y
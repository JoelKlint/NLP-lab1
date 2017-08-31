import regex
import pickle
import os

def change_file_extension(filename, new_ext):
    """
    Changes the file extension
    """
    array = filename.split('.')
    array[-1] = new_ext
    return '.'.join(array)

def get_files(dir, suffix):
    """
    Returns all the files in a folder ending with suffix
    :param dir:
    :param suffix:
    :return: the list of file names
    """
    files = []
    for file in os.listdir(dir):
        if file.endswith(suffix):
            files.append(file)
    return files

def create_index(filename):
    """
    Readsa file and creates an index of the words and where they are being used
    """
    file = open(filename, 'r')
    text = file.read()

    string = ''
    for letter in text:
        string += letter.lower()
    
    index = {}
    words = regex.finditer('\w+', string)
    for word in words:
        w = word.group()
        if w in index:
            index[w].append(word.start())
        else:
            index[w] = [word.start()]

    pickle.dump(index, open(change_file_extension(filename, 'idx'), 'wb'))

def create_master_index(dir):

    # Create all unique indicies
    filenames = get_files(dir, '.txt')
    # filepaths = list(map(lambda f: dir + '/' + f, filenames))
    for filename in filenames:
        create_index(dir+'/'+filename)


    master_index = {}

    filenames = get_files(dir, '.idx')
    # filepaths = list(map(lambda f: dir + '/' + f, filenames))
    for filename in filenames:
        index = pickle.load( open(dir+'/'+filename, 'rb') )
        for word in index:
            if word in master_index:
                master_index[word][filename] = index[word]
            else:
                master_index[word] = {filename: index[word]}





create_master_index('Selma')
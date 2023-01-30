
# Description: This script transliterates cyrillic symbols in filenames and links in files in the directory dir into latin symbols.


import os

from transliterate import translit

import shutil

#open menu to select file


source_folder = 'C:\\Users\\Sam\\YandexDisk\\Документы\\program files\\wipad\\MyWiki\\MyWiki\\data'
target_folder = 'D:\\doc\\handmade\\python\\misc\\wiki_export'




#print(source_folder.replace('/', '\\\\'))
#print(target_folder.replace('/', '\\\\'))


# transliterate cyrillic symbols into latin symbols

# iterate over files in the directory dir
# transliterate filename into latin symbols
def iterate_over_files(source_folder, target_folder):
    try:
        for file in os.listdir(source_folder):
            print('file: ' + os.path.join(source_folder, file))
            # get transliterated filename
            transliterated_filename = translit(file, 'ru', reversed=True)
            print('transliterated filename: ' + transliterated_filename)
            
            file_target_folder = os.path.join(source_folder, file).replace(source_folder, target_folder)
            print('file_target_folder: ' + file_target_folder)

            # if file has .wiki extension
            if file.endswith('.wiki'):
                # create target folder if it does not exist
                print('folder to check ' + file_target_folder.replace(file, '')[:-1])
                if not os.path.isdir(file_target_folder.replace(file, '')[:-1]):
                    print('trying to create folder: ' + file_target_folder.replace(file, ''))
                    os.makedirs(file_target_folder.replace(file, ''))
                    print('created folder: ' + file_target_folder.replace(file, ''))

                # create file in target folder
                print('trying to create file: ' + os.path.join(target_folder, transliterated_filename))
                with open(os.path.join(target_folder, transliterated_filename), 'w', encoding = 'utf-8') as trans_fname:
                    # read lines from file in source folder
                    print('reading file: ' + os.path.join(source_folder, file))
                    with open(os.path.join(source_folder, file), 'r', encoding = 'utf-8') as src_fname:
                        print('transliterated file: ' + os.path.join(target_folder, transliterated_filename))
                        for line in src_fname:
                            print('line: ' + line)
                            # looking  for links in line. Links are in format: [link]
                            if line.find('[') != -1:
                                # get link
                                link = line[line.find('[') + 1: line.find(']')]
                                # get transliterated link
                                transliterated_link = translit(link, 'ru', reversed=True)
                                print('transliterated link: ' + transliterated_link)
                                # replace link in line
                                line = line.replace(link, transliterated_link)
                            trans_fname.write(line)
            else:
                # copy file to target folder without transliteration
                if os.path.isdir(target_folder):
                    print(target_folder + 'exists')
                    shutil.copy(os.path.join(source_folder, file), os.path.join(target_folder, file))
                else:
                    print(target_folder + 'does not exists')
                    os.makedirs(os.path.dirname(target_folder))
                    shutil.copy(os.path.join(source_folder, file), os.path.join(target_folder, file))
                

    # error capturing
    except Exception as e:
        print(e)


iterate_over_files(source_folder, target_folder)


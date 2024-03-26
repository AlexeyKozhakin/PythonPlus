# 3. В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
 
# 4. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового менеджера, 
# а так же программы мой счет и программы викторина
 
# 5. (Дополнительно*) так же попробовать написать тесты для ""грязных"" функций, например копирования файла/папки, ...

import unittest
from unittest.mock import patch, mock_open
import os
import shutil
import sys
# Добавляем в системный путь директорию, содержащую cfm.py
sys.path.append('../11')
# функции находятся в модуле cfm.py
from cfm import create_folder, delete_folder, copy_folder, show_folder

class TestFolderOperations(unittest.TestCase):
    @patch('builtins.input', side_effect=['test_folder'])
    @patch('os.mkdir')
    def test_create_folder(self, mock_mkdir, mock_input):
        create_folder()
        mock_mkdir.assert_called_once_with('./test_folder')

    @patch('builtins.input', side_effect=['test_folder'])
    @patch('os.rmdir')
    def test_delete_folder(self, mock_rmdir, mock_input):
        delete_folder()
        mock_rmdir.assert_called_once_with('./test_folder')

    @patch('builtins.input', side_effect=['source_folder', 'copy_folder'])
    @patch('os.path.isfile', return_value=False)
    @patch('shutil.copytree')
    def test_copy_folder(self, mock_copytree, mock_isfile, mock_input):
        copy_folder()
        mock_copytree.assert_called_once_with('./source_folder', './copy_folder')

    @patch('os.listdir', return_value=['folder1', 'folder2', 'file.txt'])
    @patch('os.path.isfile', side_effect=[False, False, True])
    def test_show_folder(self, mock_isfile, mock_listdir):
        with patch('builtins.print') as mock_print:
            show_folder()
            mock_print.assert_any_call('folder1')
            mock_print.assert_any_call('folder2')
            mock_print.assert_any_call('file.txt')

# Это необходимо для запуска тестов
if __name__ == '__main__':
      unittest.main()


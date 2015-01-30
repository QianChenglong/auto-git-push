#!/usr/bin/env python
# coding: utf-8

import unittest
import main


class MainTest(unittest.TestCase):

    @unittest.skip('skipp tet_git_push')
    def test_git_push(self):
        main.git_push(r'E:\Programming\SourceCode\project-template')

    def test_run(self):
        main.run()

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# coding: utf-8

import ConfigParser
import json
import os
import argparse


def run():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    for opt in config.options('repository'):
        d = json.loads(config.get('repository', opt))
        git_push(d)


def git_push(repository_dir):
    os.chdir(repository_dir)
    cmd = 'git push'
    import subprocess
    subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    run()

if __name__ == '__main__':
    main()

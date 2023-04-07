#! /usr/bin/python3

from instagrapi import Client
import argparse

parser = argparse.ArgumentParser(
                    prog='instadump',
                    description='dumping instagram session to file',
                    epilog='part of Spottedmi project by RandomGuy090 and gl00man')

parser.add_argument('-l', '--login')
parser.add_argument('-p', '--password')
parser.add_argument('-f', '--file')

args = parser.parse_args()

cl = Client()
cl.login(args.login, args.password)

cl.dump_settings(args.file)
#!/usr/bin/python3

import os
import sys
import argparse


# create list of NTLM file pathes from input directory and pass list to next function
def getfileList(input_dir):

    filelist = []

    try:
        for fileName in os.listdir(input_dir):
            if 'NTLM' in fileName:
                filelist.append(input_dir + fileName)
    except:
        raise

    if filelist == []:
            print('No hash files were found.')
    return filelist


'''
    Read list from above. Split NTLMv1/v2 file contents into two dictionaries.
    Keep only a single instance of a users hash, per file. Create each file with provided
    company name and appended suffix.
'''
def getContents(passed_filelist, company):

    linesv1 = {}
    linesv2 = {}

    for fileName in passed_filelist:
        # print(fileName)                    # check to see if files are being read from list
        with open(fileName) as readLine:
            for line in readLine:
                uname = line.split(':')[0]
                if 'NTLMv1' in fileName:
                    if uname not in linesv1:
                        linesv1[uname] = line
                elif 'NTLMv2' in fileName:
                    if uname not in linesv2:
                        linesv2[uname] = line

    if not None in linesv1:
        with open(company + '-ntlmv1.txt', 'w') as writeFile:
            sortedLinesv1 = dict(sorted(linesv1.items(), key=lambda x: x[0]))
            for value in sortedLinesv1:
                writeFile.write(sortedLinesv1[value])

    if not None in linesv2:
        with open(company + '-ntlmv2.txt', 'w') as writeFile:
            sortedLinesv2 = dict(sorted(linesv2.items(), key=lambda x: x[0]))
            for value in sortedLinesv2:
                writeFile.write(sortedLinesv2[value])


# assign user inputs for arguments to variables
def main(args):
    if args.input_dir:
        input_dir = args.input_dir
        
        if ' ' in args.company:
            company = (args.company).replace(' ', '-')
        elif args.company:
            company = args.company          
        
        if os.path.exists(input_dir):
            getContents(getfileList(input_dir), company)
        else:
            print('Directory', input_dir, 'was not found.')
        
    else:
        print('No directory supplied.')

argparser = argparse.ArgumentParser(description='A python script to consolidate \
            hash files from Responder and keep only unique instances of usernames.')
# argparser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='Enable verbose output')
argparser.add_argument('-c', action='store', dest='company', help='Company name for output files')
type_to_parse_group = argparser.add_mutually_exclusive_group(required=True)
type_to_parse_group.add_argument('-d', action='store', dest='input_dir', help='Specify the directory containing the multiple Responder text files to consolidate')

if len(sys.argv) == 1:
        argparser.print_help()
        sys.exit(2)
else:
    main(argparser.parse_args())
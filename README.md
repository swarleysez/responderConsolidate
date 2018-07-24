# responderConsolidate
Python 3 script to consolidate Responder hash files into single NTLMv1 and/or v2 files for easier hash cracking

## Purpose
responderConsolidate.py was created to consolidate and parse mass amounts of hash files created by Responder. Depending on NTLMv1 or NTLMv2 hashes, the script with create a new file for each version, with the supplied company name as the prefix to the files.

## Usage
### Example
`python3 responderConsolidate.py -d <input_directory> -c <company_name>`
  * For companies with multiple words in the name, just enclose it in quotes. The script will replace all whilespaces with hyphens when creating the files.

### Screenshots

![Alt text](/responderConsolidate/respCon_help.jpg?raw=true "Help_menu")

![Alt text](/responderConsolidate/respCon_execute.jpg?raw=true "Example_execute")

## ToDo
* [ ] Clean up statements for consolidation

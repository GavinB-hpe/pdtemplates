# pdtemplates

This tool processes a text file that is expected to contain PD incident summaries, one per line.
My pdincidents tool output, when post-processed with the for-templating.sh script, will generate an
appropriate file. The tool will take any source of line by line data, however.

The tool generates a set of templates for messages, and displays them in descending order of
occurrence. You can thus see the principal sources of incident messages.

## Usage

```
usage: pdtemplates [-h] [-f FILENAME] [-d DEPTH] [-s SIMILARITY] [-w WIDTH] [-l LENGTH] [-p]

Analyses event summaries and produces stats on log types

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Name of input text file with a summary per line. Default fortemplating.txt
  -d DEPTH, --depth DEPTH
                        Depth param for tree algorithm. Default 4
  -s SIMILARITY, --similarity SIMILARITY
                        Similarity param for tree algorithm. Default 0.5
  -w WIDTH, --width WIDTH
                        Max column width. Default 100
  -l LENGTH, --length LENGTH
                        Number of rows to show. 0 implies all rows. Default 16
  -p, --plot            Show graph of results.


```
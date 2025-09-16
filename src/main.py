import console_display
import utils
import sys

anime_title = utils.name_converter(sys.argv[1])
console_display.print_table(anime_title) 
console_display.print_synopsis(anime_title)
#!/usr/bin/env ruby
# This script matches characters

arg = ARGV[0] # gets first argument from terminal
regex = /^\d{10}/ # creates search pattern

matches = arg.scan(regex)
puts matches.join("")

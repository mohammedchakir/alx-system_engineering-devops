#!/usr/bin/env ruby
# This script takes a string argument and checks if it matches the regex for "School"
puts ARGV[0].scan(/School/).join

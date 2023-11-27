#!/usr/bin/env ruby
# This script takes a string argument and checks if it exactly matches the custom regex criteria for a 10-digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join

#!/usr/bin/env ruby
# matching phone num
puts ARGV[0].scan(/\[from:([+\w]*)\] \[to:([+\w]*)\] \[flags:(.*?)\]/).join(separator=",")

#!/usr/bin/env ruby
# matching phone num
puts ARGV[0].scan(/^\d{10}$/).join

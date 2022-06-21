#!/usr/bin/env ruby
# matching hbtn
puts ARGV[0].scan(/[h\A].[n\z]/).join

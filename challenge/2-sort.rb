#!/usr/bin/env ruby

# Filter to only valid numeric values, convert to integers, then sort
ARGV.select { |arg| arg.match?(/^[-+]?\d+$/) }
    .map(&:to_i)
    .sort
    .each { |num| puts num }


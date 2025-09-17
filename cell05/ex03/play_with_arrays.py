#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [x + 2 for x in original if x > 5]

unique_array = set(new_array)

print(original)
print(unique_array)

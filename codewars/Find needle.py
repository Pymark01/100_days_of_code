def find_needle(haystack):
    # your code here
    for stuff in junk:
        if stuff == "needle":
            position = junk.index("needle")
            print(f"Found the needle at position {position}")


junk = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
find_needle(junk)

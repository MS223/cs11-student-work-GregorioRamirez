#My list print out the 3rd number which is 4.
var_1 = "kittens" #
var_2 = "cookies"
def my_function(my_favorite_things):
    song_lyrics = "rain drops on roses,"
    combined_song = song_lyrics + my_favorite_things
    return combined_song
def my_function_2(item, item2):
    full_lyrics = item + "on " + item2
    full_song = my_function(full_lyrics)
    return full_song
my_song = my_function_2(var_1, var_2)

This piece of code takes all the log files in a folder and transforms them to a csv file.

Why? well, reading all the log files takes a long time, so better wait once a few minutes to transform them, and then load them in using pandas after then having to wait 5 minutes every time you run it.

All you have to do is change the file path to the path where the folder with logs is located, and the just run it and let the magic to its thing.


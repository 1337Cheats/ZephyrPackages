with open(__file__, 'r') as file:
    file_contents = file.read()
    if "run" in file_contents:
        print("Test module 1 ran")

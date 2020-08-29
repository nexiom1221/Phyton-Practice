def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        file.write(text)

        return

       
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "HELLO!")
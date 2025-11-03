#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    all_names = dir(hidden_4)
    
    for name in all_names:
        first_two_chars = name[:2]
        if first_two_chars != "__":
            print(name)
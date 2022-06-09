def print_():
    print("""
                   __      _ _                        
      instagram   / _|    | | |                       
      _   _ _ __ | |_ ___ | | | _____      _____ _ __ 
     | | | | '_ \|  _/ _ \| | |/ _ \ \ /\ / / _ \ '__|
     | |_| | | | | || (_) | | | (_) \ V  V /  __/ |   
      \__,_|_| |_|_| \___/|_|_|\___/ \_/\_/ \___|_| by Novin.Nouri

    """)

def print_find(not_following_back, id_taraf):
    # This part print those who unfollowed your page
    print(f"\n\nThese people did not follow this page({id_taraf}):")
    for a in not_following_back:
        print("----->  " + a)
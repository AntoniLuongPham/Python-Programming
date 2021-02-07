# Trong Python, mot bien ma ta khong co y dinh thay doi thi goi la mot hang so. 
# Ten cua hang so duoc viet hoa hoan toan de nguoi doc hieu duoc y dinh do
# cua lap trinh vien

WELCOME_MESSAGE = """
     **xin chao!!**
               __   __
              __ \\ / __
             /  \\ | /  \\
                 \\|/
            _,.---v---._
   /\\__/\\  /            \\
   \\_  _/ /              \\
     \\ \\_|           @ __|
      \\                \\_
       \\     ,__/       /
     ~~~`~~~~~~~~~~~~~~/~~~~
"""

WARNING_MESSAGE = """
         ______________________
        |                      |
        | CANH BAO NGUY HIEM!! |
        |______________________|
                                  /^^^/           /]
                                 /   ]           / ]
      O                  _______/    ]___       /  ]
                        /                \\_____/   /
   O                  _/   [@]  \\ \\                \\
           ___//_    /..         | |                ]
    o     /o )   \\/   VVVvvv\    | |         _/\\    ]
      O<  )___\\\\_/\\         |               /    \\  ]
                     AAA^^^^^              /       \\]
                      \\_________\\   \\_____/
                               \\    \\
                                \\____\\
"""

counter = 0

while counter < 3:
    passcode = input("Xin nhap vao mat khau: ")

    if passcode == "0042" or passcode == "2021":
        print("Chao mung ban den voi Sieu May Tinh!")
        print(WELCOME_MESSAGE)
        break
    else:
        try_again = counter < 2
        if try_again:
            print("Mat khau nhap sai! Xin hay thu lai.")
        else:
            print("Mat khau nhap sai!")
            print(WARNING_MESSAGE)

    counter = counter + 1

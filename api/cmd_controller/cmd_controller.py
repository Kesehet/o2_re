name = "cmd_controller"
description = "Shell Controller API"
fa_icon = "shell"
AccessID = 0
privLevel = AccessID
isOpenToPublic = False
publicLinks = [
  "main"
]


from funcs import shell as SHELL

def main(request):
  return str(
        {
            "response": SHELL.run(
                    SHELL.getAllCommands(0, {"filename":"funcs/settings.py"})
                )
        }
    )
# Update V1.5.3

## ADDED
- DB: `db.py` via `sqllite3`
- Logging System (class Logger in `modules/Utils.py`)
- Output Logging `log.log`
- Mainloop, refreshes Tutla Assistance every 5 minutes
- Token is now in environment variables, not file

- Pinging it gives a random tip

- `.list`: New command that replaces `.inservers` & `.listmods` and also adds premium users
- `.help` menu updated to display number of commands
- `.daily`: Gives your daily XP and Aura
- `.afk`: AFK Command
- `.tfi`: Extract Text from an image
- `.panel`: Tutla Administrator Panel
- `.infinitecraft`: Infinitecraft on Discord!
- `.changelog`: Returns Changelog
- Readded `.antinpc` # 2nd Command Ever!
- `.life` is now `.ghostping`
- Categorized & Renamed several commands

*Theres so many changes this updated I can't list them all! Read them @ https://github.com/TutlaMC/tutla-assistant/commits*

## REMOVED
- Example Command
- "Free" Commands, now any user can use commands (no longer need to be Tutla Member)
- ChatBot mod
- EMod Logs

## MODDING
- `self.mainloop`: Mainloop
- `self.on_edit`: On message edit trigger for modding

- AuraMod: lose and gain aura
- EMod: `.esnipe` and `.snipe` gets 3 History
- ClickCrystalsMod: Updated Site links
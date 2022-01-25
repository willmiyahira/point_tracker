# Import the tkinter package
import tkinter as tk

# Create lists to hold all of the player information and check buttons
cbox_list = []              # List of check buttons widgets
cbox_vals = []              # List of check button values (0 or 1)
txt_player_list = []        # List of text widgets containing the player's names
lbl_points_list = []        # List of label widgets containing the player's points

# Function for adding a player
def add_player():
    # Get the number of players currently in the game
    numPlayers = len(txt_player_list)

    # Create all of the widgets for the new player and add them to the same frame
    cbox_var = tk.IntVar()
    cbox_vals.append(cbox_var)
    cbox = tk.Checkbutton(master=frm_players, variable = cbox_vals[numPlayers])
    txt_newPlayer = tk.Text(master=frm_players, width = 10, height = 1)
    txt_newPlayer.insert("1.0", "Player" + str(numPlayers+1))
    lbl_numPoints = tk.Label(master=frm_players, text = "0", width = 9, height = 1)

    # Position the widgets for the new player so that they're in the same row
    cbox.grid(row = numPlayers+1, column = 0)
    txt_newPlayer.grid(row = numPlayers+1, column = 1)
    lbl_numPoints.grid(row=numPlayers+1, column=2, sticky="w")

    # Add all of the player information to the lists
    cbox_list.append(cbox)
    txt_player_list.append(txt_newPlayer)
    lbl_points_list.append(lbl_numPoints)

    # Increase the number of players by 1 and update the number of players displayed
    numPlayers += 1
    lbl_numPlayersNum["text"] = str(len(txt_player_list))

# Function for removing a player
def remove_player():
    # Create lists to store the name and points for the players that will not be removed
    save_name = []                                  # list of names to save
    save_points = []                                # list of points to save
    numSave = 0                                     # number of players not removed
    numPlayers = int(lbl_numPlayersNum["text"])     # number of players currently in the game

    # Only remove players if there are checkboxes and at least one player in the game
    if len(cbox_list) != 0:
        if numPlayers > 0:
            # Loop through all of the check button values (the IntVars in cbox_vals). For the ones that are not checked, save those player's name and points
            for i in cbox_vals:
                idx = cbox_vals.index(i)
                if i.get() == 0:
                    numSave += 1
                    save_name.append(txt_player_list[idx].get("1.0", tk.END).strip())
                    save_points.append(lbl_points_list[idx]["text"])
                # Remove the check button, text, and label widgets from the window
                cbox_list[idx].destroy()
                txt_player_list[idx].destroy()
                lbl_points_list[idx].destroy()
            # Clear the storage lists
            txt_player_list.clear()
            lbl_points_list.clear()
            cbox_list.clear()
            cbox_vals.clear()

            # Now add back all of the players that we wanted to save (basically just the add_player() function)
            for j in range(len(save_name)):
                playerName = save_name[j]
                playerPoints = save_points[j]
                cbox_var = tk.IntVar(window)
                cbox_vals.append(cbox_var)
                cbox = tk.Checkbutton(master=frm_players, variable = cbox_var)
                txt_newPlayer = tk.Text(master=frm_players, width = 10, height = 1)
                txt_newPlayer.insert("1.0", playerName)
                cbox.grid(row = j+1, column = 0)
                txt_newPlayer.grid(row = j+1, column = 1)
                lbl_numPoints = tk.Label(master=frm_players, text = playerPoints, width = 9, height = 1)
                lbl_numPoints.grid(row=j+1, column=2, sticky="w")
                cbox_list.append(cbox)
                txt_player_list.append(txt_newPlayer)
                lbl_points_list.append(lbl_numPoints)

            lbl_numPlayersNum["text"] = str(numSave)

# Function for adding points
def addPoints():
    # Get the number of points to add
    points = float(txt_points.get("1.0", tk.END))

    # Go through all of the check buttons. If any are checked, add the points to that player and then uncheck the check button
    for i in cbox_vals:
        if i.get() == 1:
            idx = cbox_vals.index(i)
            lbl_points_list[idx]["text"] = str(float(lbl_points_list[idx]["text"]) + points)
        i.set(0)

    # Reset the points to add/remove text field to zero
    txt_points.delete("1.0", tk.END)
    txt_points.insert("1.0", 0)

# Function for removing points
def removePoints():
    # Get the number of points to remove
    points = float(txt_points.get("1.0", tk.END))

    # Go through all of the check buttons. If any are checked, remove the points from that player and then uncheck the check button
    for i in cbox_vals:
        if i.get() == 1:
            idx = cbox_vals.index(i)
            lbl_points_list[idx]["text"] = str(float(lbl_points_list[idx]["text"]) - points)
        i.set(0)

    # Reset the points to add/remove text field to zero
    txt_points.delete("1.0", tk.END)
    txt_points.insert("1.0", 0)

# Create the window and give it a name 
window = tk.Tk()
window.title("Point Tracker")

# Frames
frm_numPlayers = tk.Frame(master=window, width=10)
frm_players = tk.Frame(master=window, width=10)
frm_addPlayer = tk.Frame(master=window, width=10, height=10)
frm_addPoints = tk.Frame(master=window, width=10, height=10)

# Buttons
btn_addPlayer = tk.Button(master = frm_addPlayer, text = "Add Player", width = 9, height = 2, command = add_player)
btn_addPlayer.grid(row=0, column=0)
btn_rmvPlayer = tk.Button(master = frm_addPlayer, text = "Remove Player", width = 12, height = 2, command = remove_player)
btn_rmvPlayer.grid(row=1, column=0)
btn_addPoints = tk.Button(master= frm_addPoints, text = "Add Points", width = 9, height = 2, command = addPoints)
btn_addPoints.grid(row = 1, column=0)
btn_subPoints = tk.Button(master=frm_addPoints, text = "Subtract Points", width = 12, height = 2, command = removePoints)
btn_subPoints.grid(row=2, column=0)

# Text Fields
txt_points = tk.Text(master=frm_addPoints, width = 9, height = 1)
txt_points.grid(row=0, column=0)
txt_points.insert("1.0", 0)

# Labels
lbl_numPlayersNum = tk.Label(master=frm_addPlayer, text = "0")
lbl_numPlayersTxt = tk.Label(master=frm_addPlayer, text = "Number of Players:")
lbl_numPlayersTxt.grid(row=2, column=0, sticky="e")
lbl_numPlayersNum.grid(row=2, column=1, sticky="w")

# Position frames on the window. Use sticky="n" to keep everything pinned to the top of the window.
frm_addPlayer.grid(row=0,column=0, sticky="n")
frm_players.grid(row=0, column = 1, sticky="n")
frm_addPoints.grid(row=0, column=2, sticky="n")


window.mainloop()

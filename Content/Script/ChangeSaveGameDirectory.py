import os

def change_save_game_directory(project_path):
    default_engine_ini_path = os.path.join(project_path, "Config", "DefaultEngine.ini")
    save_game_directory = os.path.join(project_path, "Content", "SaveGames")
    
    with open(default_engine_ini_path, "r") as f:
        lines = f.readlines()

    with open(default_engine_ini_path, "w") as f:
        for line in lines:
            if line.startswith("[SaveGame]"):
                f.write("[SaveGame]\n")
                f.write(f"SaveGameDirectory={save_game_directory}\n")
            else:
                f.write(line)

# Change the path below to your Unreal Engine project directory
project_path = "D:\PC\UnrealEngine\TransformObjects"

change_save_game_directory(project_path)
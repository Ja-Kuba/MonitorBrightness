import typer
import screen_brightness_control as sbc
from typing import Optional

app = typer.Typer()


@app.command()
def set(brightness: int, display: Optional[str] = None):
    # Get available monitors
    if brightness < 0 or brightness > 100:
        raise typer.BadParameter("Brightness must be between 0 and 100.")
    
    monitors = sbc.list_monitors()
    print(f"Available monitors: {monitors}")

    # Set brightness on a specific monitor (e.g., the first one)
    if monitors:
        sbc.set_brightness(brightness, display=monitors[0])


@app.command()
def stats(display: Optional[str] = None):
    # Get current brightness (as a percentage)
    current_brightness = sbc.get_brightness()
    print(f"Current brightness: {current_brightness}")

    

if __name__ == "__main__":
    app()
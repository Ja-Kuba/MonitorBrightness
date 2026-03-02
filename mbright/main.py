import typer
import screen_brightness_control as sbc
from typing import Optional

app = typer.Typer()


@app.command()
def set_brightness(value: int, display: Optional[str] = None):
    """Set monitor brightness (0–100)."""
    if value < 0 or value > 100:
        raise typer.BadParameter("Brightness must be between 0 and 100.")

    monitors = sbc.list_monitors()
    print(f"Available monitors: {monitors}")

    if monitors:
        target = display if display else monitors[0]
        sbc.set_brightness(value, display=target)
        print(f"Brightness set to {value}% on {target}")


@app.command()
def stats(display: Optional[str] = None):
    """Show current brightness stats."""
    current_brightness = sbc.get_brightness(display=display) if display else sbc.get_brightness()
    print(f"Current brightness: {current_brightness}")


def main():
    app()


if __name__ == "__main__":
    main()

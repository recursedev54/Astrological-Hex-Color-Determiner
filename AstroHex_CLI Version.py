import math
import datetime

BIRTHSTONES = {
    1: ("#781244", "Garnet"),
    2: ("#9966CC", "Amethyst"),
    3: ("#7FFFD4", "Aquamarine"),
    4: ("#FFFFFF", "Diamond"),
    5: ("#50C878", "Emerald"),
    6: ("#F0F8FF", "Pearl"),
    7: ("#E0115F", "Ruby"),
    8: ("#E6E200", "Peridot"),
    9: ("#0F52BA", "Sapphire"),
    10: ("#A8C3BC", "Opal"),
    11: ("#FFC87C", "Topaz"),
    12: ("#40E0D0", "Turquoise")
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def euclidean_distance(color1, color2):
    """Calculate the Euclidean distance between two RGB colors."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

def wrap_color(value):
    """Wrap color value around if it exceeds 0-255 range."""
    return value % 256

def adjust_color_with_wrap(base_color, adjustment):
    """Adjust color based on adjustment value with wrap-around effect."""
    rgb = hex_to_rgb(base_color)
    adjusted_rgb = tuple(wrap_color(value + adjustment) for value in rgb)
    return rgb_to_hex(adjusted_rgb)

def calculate_days_difference(date1, date2):
    d1 = datetime.datetime.strptime(date1, "%m/%d/%Y")
    d2 = datetime.datetime.strptime(date2, "%m/%d/%Y")
    return (d2 - d1).days

def reorder_channels(color, birthstone_color):
    """Reorder color channels to match birthstone color order."""
    color_rgb = hex_to_rgb(color)
    birthstone_rgb = hex_to_rgb(birthstone_color)
    
    order = sorted(range(3), key=lambda i: birthstone_rgb[i], reverse=True)
    
    reordered = tuple(color_rgb[i] for i in order)
    return rgb_to_hex(reordered)

def adjust_intensity(color, birthstone_color):
    """Adjust color intensity based on birthstone color."""
    color_rgb = hex_to_rgb(color)
    birthstone_rgb = hex_to_rgb(birthstone_color)
    
    adjusted_rgb = tuple(
        wrap_color(c + (b - c) // 2)
        for c, b in zip(color_rgb, birthstone_rgb)
    )
    
    return rgb_to_hex(adjusted_rgb)

def apply_birthstone_weight(color, birthstone_color):
    """Apply birthstone weighting to a color."""
    reordered = reorder_channels(color, birthstone_color)
    return adjust_intensity(reordered, birthstone_color)

def invert_hex_color(hex_color):
    """Invert a hex color."""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    inverted_rgb = tuple(255 - c for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*inverted_rgb)

def adjust_moon_color(moon_color, year):
    """Adjust moon color based on birth year."""
    year_hex = f"{year:06d}"
    rgb = hex_to_rgb(moon_color)
    
    # Adjust red and blue channels
    red = wrap_color(rgb[0] + int(year_hex[:2]))
    blue = wrap_color(rgb[2] + int(year_hex[4:]))
    
    # Adjust green channel
    total_adjustment = int(year_hex[:2]) + int(year_hex[4:])
    green = wrap_color(rgb[1] - total_adjustment)
    
    return f"#{red:02x}{green:02x}{blue:02x}"

def generate_astrological_colors(birthday):
    base_sun_color = "#5A3442"
    base_date = "07/17/2002"
    
    days_diff = calculate_days_difference(base_date, birthday)
    birth_month = int(birthday.split('/')[0])
    birth_year = int(birthday.split('/')[-1])
    birthstone_color, birthstone_name = BIRTHSTONES[birth_month]
    
    # Calculate initial colors
    sun_color = adjust_color_with_wrap(base_sun_color, days_diff)
    color1 = sun_color
    color2_moon = "#808080"
    color2_rising = "#C0C0C0"
    
    distance_moon = euclidean_distance(hex_to_rgb(color1), hex_to_rgb(color2_moon))
    distance_rising = euclidean_distance(hex_to_rgb(color1), hex_to_rgb(color2_rising))
    
    moon_color = adjust_color_with_wrap(sun_color, int(distance_moon))
    rising_color = adjust_color_with_wrap(sun_color, -int(distance_rising))
    
    # Apply birthstone weighting
    sun_color = apply_birthstone_weight(sun_color, birthstone_color)
    moon_color = apply_birthstone_weight(moon_color, birthstone_color)
    rising_color = apply_birthstone_weight(rising_color, birthstone_color)
    
    # Final adjustments
    moon_color = adjust_moon_color(moon_color, birth_year)
    rising_color = invert_hex_color(rising_color)
    
    return sun_color, moon_color, rising_color, birthstone_name

# Example usage
birthday = input("Enter your birthday (MM/DD/YYYY): ")
sun, moon, rising, birthstone = generate_astrological_colors(birthday)
print(f"Birthstone: {birthstone}")
print(f"Sun color: {sun}")
print(f"Moon color: {moon}")
print(f"Rising color: {rising}")

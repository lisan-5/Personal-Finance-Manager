from datetime import datetime

def clear_screen():
    print("\033[H\033[J", end="")  # ANSI escape sequence to clear screen

def print_header(title):
    print(f"\n=== {title} ===")

def print_warning(message):
    print(f"\n⚠️  {message}")

def print_success(message):
    print(f"\n✅ {message}")

def print_table(headers, rows, min_widths=None):
    if not rows:
        return
    
    # Calculate column widths
    if min_widths is None:
        min_widths = [len(h) for h in headers]
    
    widths = list(min_widths)
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Print headers
    header_row = " | ".join(f"{header:<{width}}" for header, width in zip(headers, widths))
    print(f"\n{header_row}")
    print("-" * len(header_row))
    
    # Print rows
    for row in rows:
        print(" | ".join(f"{str(cell):<{width}}" for cell, width in zip(row, widths)))
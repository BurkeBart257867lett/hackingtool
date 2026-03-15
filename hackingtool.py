#!/usr/bin/env python3
import sys

# ── Python version guard (must be before any other local import) ───────────────
if sys.version_info < (3, 10):
    print(
        f"[ERROR] Python 3.10 or newer is required.\n"
        f"You are running Python {sys.version_info.major}.{sys.version_info.minor}.\n"
        f"Upgrade with: sudo apt install python3.10"
    )
    sys.exit(1)

import os
import webbrowser
from platform import system

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.rule import Rule

from core import HackingToolsCollection
from constants import VERSION_DISPLAY, REPO_WEB_URL
from config import get_tools_dir
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

console = Console()

ASCII_LOGO = r"""
   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄           ███      ▄██████▄   ▄██████▄   ▄█
  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      ▀█████████▄ ███    ███ ███    ███ ███
  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀          ▀███▀▀██ ███    ███ ███    ███ ███
 ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███                 ███   ▀ ███    ███ ███    ███ ███
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄           ███     ███    ███ ███    ███ ███
  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███
  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███▌    ▄
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██
                                         ▀                                                                            ▀
"""

tool_definitions = [
    ("Anonymously Hiding Tools",           "🛡️"),
    ("Information gathering tools",        "🔍"),
    ("Wordlist Generator",                 "📚"),
    ("Wireless attack tools",              "📶"),
    ("SQL Injection Tools",                "🧩"),
    ("Phishing attack tools",              "🎣"),
    ("Web Attack tools",                   "🌐"),
    ("Post exploitation tools",            "🔧"),
    ("Forensic tools",                     "🕵️"),
    ("Payload creation tools",             "📦"),
    ("Exploit framework",                  "🧰"),
    ("Reverse engineering tools",          "🔁"),
    ("DDOS Attack Tools",                  "⚡"),
    ("Remote Administrator Tools (RAT)",   "🖥️"),
    ("XSS Attack Tools",                   "💥"),
    ("Steganography tools",                "🖼️"),
    ("Other tools",                        "✨"),
    ("Update or Uninstall | Hackingtool",  "♻️"),
]

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager(),
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        header = Text(ASCII_LOGO, style="bold magenta")
        footer = Text.assemble(
            (f" {REPO_WEB_URL} ", "bold bright_black"),
            (" | ",),
            (VERSION_DISPLAY, "bold green"),
        )
        warning = Text(" Please Don't Use For Illegal Activity ", style="bold red")
        panel = Panel(
            Align.center(header + Text("\n") + footer + Text("\n") + warning),
            box=box.DOUBLE,
            padding=(1, 2),
            border_style="magenta",
        )
        console.print(panel)


def build_menu():
    table = Table.grid(expand=True)
    table.add_column("idx", width=6, justify="right")
    table.add_column("name", justify="left")

    for idx, (title, icon) in enumerate(tool_definitions):
        if idx == len(tool_definitions) - 1:
            label = "[bold magenta]99[/bold magenta]"
            name  = f"[bold magenta]{icon} {title}[/bold magenta]"
        else:
            label = f"[bold magenta]{idx}[/bold magenta]"
            name  = f"[white]{icon}[/white]  [magenta]{title}[/magenta]"
        table.add_row(label, name)

    console.print(Panel(
        Align.center(Text("HackingTool — Main Menu", style="bold white on magenta"), vertical="middle"),
        style="magenta", padding=(0, 1), box=box.ROUNDED,
    ))
    console.print(Panel.fit(
        table,
        title="[bold magenta]Select a tool[/bold magenta]",
        border_style="bright_magenta",
        box=box.SQUARE,
    ))
    console.print(Rule(style="bright_black"))
    console.print(Align.center(Text(
        "Choose number and press Enter — 99 to exit",
        style="italic bright_black",
    )))
    console.print("")


def interact_menu():
    while True:
        try:
            build_menu()
            choice = IntPrompt.ask("[magenta]Choose a tool to proceed[/magenta]", default=0)
            if choice == 99:
                console.print(Panel("[bold white on magenta]Goodbye — Come Back Safely[/bold white on magenta]"))
                break
            if 0 <= choice < len(all_tools):
                tool = all_tools[choice]
                name = tool_definitions[choice][0]
                console.print(Panel(
                    f"[bold magenta]{tool_definitions[choice][1]}  Selected:[/bold magenta] [white]{name}[/white]"
                ))
                try:
                    tool.show_options()
                except Exception as e:
                    console.print(Panel(f"[red]Error while opening {name}[/red]\n{e}", border_style="red"))
                if not Confirm.ask("[magenta]Return to main menu?[/magenta]", default=True):
                    console.print(Panel("[bold white on magenta]Exiting...[/bold white on magenta]"))
                    break
            else:
                console.print("[red]Invalid selection. Pick a number from the menu.[/red]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted — exiting[/bold red]")
            break


def main():
    try:
        from os_detect import CURRENT_OS

        if CURRENT_OS.system == "windows":
            console.print(Panel("[bold red]Please run this tool on Linux or macOS.[/bold red]"))
            if Confirm.ask("Open guidance link in your browser?", default=True):
                webbrowser.open_new_tab(f"{REPO_WEB_URL}#windows")
            return

        if CURRENT_OS.system not in ("linux", "macos"):
            console.print(f"[yellow]Unsupported OS: {CURRENT_OS.system}. Proceeding anyway...[/yellow]")

        # Ensure ~/.hackingtool/tools/ exists — no os.chdir(), tools use absolute paths
        tools_dir = get_tools_dir()
        console.print(f"[dim]Tools directory: {tools_dir}[/dim]")

        AllTools().show_info()
        interact_menu()

    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting...[/bold red]")


if __name__ == "__main__":
    main()

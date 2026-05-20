#!/usr/bin/env python3
import os
import sys
import subprocess
import time

# --- ANSI TERMINAL COLORS ---
G = '\033[92m'  # Green (Success)
Y = '\033[93m'  # Yellow (Warning)
R = '\033[91m'  # Red (Error)
B = '\033[94m'  # Blue (Process)
C = '\033[96m'  # Cyan (Headers)
W = '\033[0m'   # White (Reset)

def banner():
    os.system('clear')
    print(f"{C}======================================================={W}")
    print(f"{C}       REEX-TOOL: UNISOC EXPLORATION & ROOT TOOL       {W}")
    print(f"{C}        Optimized for Linux & Termux Environments       {W}")
    print(f"{C}     Telegram account : @HC_XA {W}")
    print(f"{C}======================================================={W}\n")

def run_cmd(command):
    try:
        res = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"ERR:{e.stderr.strip()}"

def check_connection():
    print(f"{B}[*] Scanning local physical interfaces for Android hardware...{W}")
    adb_dev = run_cmd("adb devices")
    fast_dev = run_cmd("fastboot devices")
    
    print(f"{C}--- ADB Status ---{W}\n{adb_dev}")
    print(f"{C}--- Fastboot Status ---{W}\n{fast_dev}")
    
    if "device" in adb_dev.split() or fast_dev:
        print(f"{G}[+] Connection Verified!{W}")
        return True
    else:
        print(f"{R}[-] Device not detected. Enable USB debugging or connect via OTG/USB.{W}")
        return False

def unisoc_exploit_unlock():
    print(f"\n{Y}[!] WARNING: Bootloader unlocking wipes all internal data.{W}")
    choice = input(f"{C}[?] Proceed with Unisoc custom unlock token exploit? (y/N): {W}").lower()
    if choice != 'y': return
    
    print(f"{B}[*] Sending instruction to reboot into bootloader mode...{W}")
    run_cmd("adb reboot bootloader")
    time.sleep(5)
    
    print(f"{B}[*] Fetching Unisoc signature Identifier Token...{W}")
    token_data = run_cmd("fastboot oem get_identifier_token")
    print(f"{C}Identifier Data Raw Output:{W}\n{token_data}")
    
    if "ERR" in token_data or not token_data:
        print(f"{R}[-] Failed to query structural identifier token from SoC ASIC.{W}")
        return

    print(f"{B}[*] Executing integrated Python dynamic signature generation override...{W}")
    # Triggers native python-adb payload mechanics for Unisoc bootloaders
    unlock_execution = run_cmd("python3 -m unisoc_unlock unlock")
    
    if "ERR" not in unlock_execution:
        print(f"{G}[+] Unlock token packet successfully accepted by bootloader.{W}")
        print(f"{Y}[!] Check phone screen immediately to confirm via Volume Keys!{W}")
    else:
        print(f"{R}[- ] Automated exploit failed. Attempting alternative brute structural command...{W}")
        run_cmd("fastboot oem unlock")
        run_cmd("fastboot flashing unlock")

def extract_boot_img():
    print(f"\n{B}[*] Attempting kernel mapping to locate 'boot' block allocation...{W}")
    block_path = run_cmd("adb shell \"ls -l /dev/block/by-name/boot\"")
    
    if "ERR" in block_path or not block_path:
        print(f"{Y}[!] Direct low-level block scanning blocked by active SELinux policy.{W}")
        print(f"{B}[*] Attempting alternative extraction through recovery boundary...{W}")
        # Secondary backup recovery dump logic
        run_cmd("adb shell \"su -c 'dd if=/dev/block/by-name/boot of=/data/local/tmp/boot.img'\"")
        pull_status = run_cmd("adb pull /data/local/tmp/boot.img ./boot.img")
    else:
        print(f"{G}[+] Native Partition Table Found: {block_path}{W}")
        run_cmd("adb shell \"dd if=/dev/block/by-name/boot of=/data/local/tmp/boot.img\"")
        pull_status = run_cmd("adb pull /data/local/tmp/boot.img ./boot.img")
        
    if os.path.exists("./boot.img") and os.path.getsize("./boot.img") > 0:
        print(f"{G}[+] SUCCESS: Saved raw kernel 'boot.img' locally into your working directory!{W}")
    else:
        print(f"{R}[-] Partition Extraction Denied. Device must be fully unlocked or in an unlocked BROM state.{W}")

def root_generator_instructions():
    print(f"\n{C}=== AUTOMATED DIRECT ROOT SYSTEM PATHWAYS ==={W}")
    if os.path.exists("./boot.img"):
        print(f"{G}[+] Active local 'boot.img' target asset discovered!{W}")
        print(f"{B}[*] Step 1: Install Magisk App on your target phone.{W}")
        print(f"{B}[*] Step 2: Push this file to the phone using: adb push boot.img /sdcard/Download/{W}")
        print(f"{B}[*] Step 3: Inside Magisk App -> Click 'Install' -> 'Select and Patch a File'.{W}")
        print(f"{B}[*] Step 4: Pull back the output: adb pull /sdcard/Download/magisk_patched.img{W}")
        print(f"{B}[*] Step 5: Flash patched file via Fastboot: fastboot flash boot magisk_patched.img{W}")
    else:
        print(f"{R}[- ] Core 'boot.img' missing inside script repository root directory. Extract it first via Option 2.{W}")

def main_menu():
    while True:
        banner()
        print(f"{C}1.{W} Verify Android Local Node Connections (ADB/Fastboot)")
        print(f"{C}2.{W} Execute Unisoc/Spreadtrum Bootloader Exploit Bypass")
        print(f"{C}3.{W} Extract Kernel 'boot.img' Allocation")
        print(f"{C}4.{W} Generate Direct Magisk Root Flash Steps")
        print(f"{C}5.{W} Exit Application")
        
        try:
            choice = input(f"\n{G}NexusRoot://Enter_Selection> {W}")
            if choice == '1': check_connection()
            elif choice == '2': unisoc_exploit_unlock()
            elif choice == '3': extract_boot_img()
            elif choice == '4': root_generator_instructions()
            elif choice == '5': 
                print(f"{G}[+] Exiting environment wrapper safely. Goodbye.{W}")
                sys.exit()
            else: print(f"{R}[-] Invalid Selection Mapping Parameter.{W}")
        except KeyboardInterrupt:
            print(f"\n{Y}[!] Abort signal received.{W}")
            sys.exit()
        input(f"\n{B}Press Enter to return to Menu...{W}")

if __name__ == "__main__":
    main_menu()

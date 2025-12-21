#!/usr/bin/env python3
"""
Canadia CLI - Command line interface for Canadia
"""
import sys
import os
import subprocess
import webbrowser
import time
import argparse
from pathlib import Path


def start_canadia():
    """Start the Canadia server and open browser"""
    port = 9800
    host = "127.0.0.1"
    url = f"http://{host}:{port}"
    
    # Get the repository root directory
    repo_root = Path(__file__).parent.absolute()
    backend_dir = repo_root / "backend"
    demo_server = repo_root / "canadia_demo_server.py"
    
    print(f"🔎 Cleaning port {port}...")
    # Kill any process using the port - use safe subprocess call
    try:
        # Get PIDs using the port
        result = subprocess.run(
            ['lsof', '-ti', f'tcp:{port}'],
            capture_output=True,
            text=True,
            check=False
        )
        if result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid:
                    subprocess.run(['kill', '-9', pid], check=False)
    except FileNotFoundError:
        # lsof command not found, skip port cleanup
        pass
    except Exception:
        pass
    
    print(f"🚀 Starting Canadia on {url}...")
    
    # Try to use the demo server for simplicity and reliability
    if demo_server.exists():
        print("📱 Using Canadia demo server...")
        cmd = f"cd {repo_root} && python3 {demo_server}"
        process = subprocess.Popen(
            cmd,
            shell=True,
            executable="/bin/bash",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Wait for server to start
        print("⏳ Waiting for server to start...")
        time.sleep(2)
        
        # The demo server will open the browser automatically
        # Stream output from the server
        try:
            for line in process.stdout:
                print(line, end='')
        except KeyboardInterrupt:
            print("\n\n🛑 Stopping Canadia...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            print("✅ Canadia stopped.")
    else:
        print(f"❌ Error: Demo server not found at {demo_server}")
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Canadia CLI - Your Canadian civic assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  canadia start    Start the Canadia server and open browser
        """
    )
    
    parser.add_argument(
        'command',
        choices=['start'],
        help='Command to execute'
    )
    
    args = parser.parse_args()
    
    if args.command == 'start':
        start_canadia()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

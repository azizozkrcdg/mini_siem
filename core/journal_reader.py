import subprocess

def read_ssh_logs(minutes=5):

    cmd = [
        "journalctl",
        "-u", "ssh",
        "--since", f"{minutes} minutes ago",
        "--no-pager"
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout.splitlines()

"""
Security check script - Run before committing to GitHub
Checks for exposed API keys and sensitive data
"""
import os
import re
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Patterns to detect API keys
API_KEY_PATTERNS = [
    r'AIzaSy[A-Za-z0-9_-]{35}',  # Google API keys
    r'sk-[A-Za-z0-9]{32,}',      # OpenAI keys
    r'xox[baprs]-[A-Za-z0-9-]{10,}',  # Slack tokens
]

# Files to check
CHECK_EXTENSIONS = ['.py', '.ps1', '.js', '.html', '.md', '.txt', '.json']
IGNORE_PATTERNS = ['.git', 'venv', '__pycache__', '.env.example']

def check_file(filepath):
    """Check a single file for API keys"""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
            
            for i, line in enumerate(lines, 1):
                for pattern in API_KEY_PATTERNS:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        # Check if it's in a comment or example
                        if 'example' in line.lower() or 'your_' in line.lower():
                            continue
                        issues.append({
                            'file': filepath,
                            'line': i,
                            'match': match.group()[:20] + '...',
                            'pattern': pattern
                        })
    except Exception as e:
        pass  # Skip files that can't be read
    
    return issues

def scan_directory(directory='.'):
    """Scan directory for potential security issues"""
    all_issues = []
    
    for root, dirs, files in os.walk(directory):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not any(ignore in d for ignore in IGNORE_PATTERNS)]
        
        for file in files:
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, directory)
            
            # Skip ignored files
            if any(ignore in rel_path for ignore in IGNORE_PATTERNS):
                continue
            
            # Check only relevant extensions
            if any(file.endswith(ext) for ext in CHECK_EXTENSIONS):
                issues = check_file(filepath)
                all_issues.extend(issues)
    
    return all_issues

def check_env_file():
    """Check if .env exists and is in .gitignore"""
    issues = []
    
    if os.path.exists('.env'):
        # Check .gitignore
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                gitignore_content = f.read()
                if '.env' not in gitignore_content:
                    issues.append({
                        'type': 'warning',
                        'message': '.env file exists but may not be in .gitignore'
                    })
        else:
            issues.append({
                'type': 'error',
                'message': '.env file exists but .gitignore not found!'
            })
    
    return issues

def main():
    print("Security Check - Scanning for exposed credentials...\n")
    print("=" * 60)
    
    # Check .env file
    env_issues = check_env_file()
    if env_issues:
        for issue in env_issues:
            if issue['type'] == 'error':
                print(f"❌ {issue['message']}")
            else:
                print(f"⚠️  {issue['message']}")
        print()
    
    # Scan for API keys
    print("Scanning files for API keys...")
    issues = scan_directory()
    
    if issues:
        print(f"\n[ERROR] Found {len(issues)} potential security issues:\n")
        for issue in issues:
            print(f"  File: {issue['file']}")
            print(f"  Line: {issue['line']}")
            print(f"  Match: {issue['match']}")
            print()
        
        print("[WARNING] Do not commit these files!")
        print("   Remove API keys and use environment variables instead.\n")
        return 1
    else:
        print("[OK] No API keys found in code files")
        print("[OK] Security check passed!\n")
        return 0

if __name__ == '__main__':
    sys.exit(main())


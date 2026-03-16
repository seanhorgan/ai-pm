import os
import shutil
import re
import argparse
from pathlib import Path

# Configuration
OBSIDIAN_DIR = "/Users/seanhorgan/Library/CloudStorage/GoogleDrive-seanhorgan@gmail.com/My Drive/obsidian/personal/Practice of Product"
GLOBAL_SKILLS_DIR = os.path.expanduser("~/.agent/workflows/product_skills")
LOCAL_SKILLS_DIR = "/Users/seanhorgan/dev/ai-pm/skills"

def setup_directories():
    if not os.path.exists(GLOBAL_SKILLS_DIR):
        os.makedirs(GLOBAL_SKILLS_DIR)
    if not os.path.exists(LOCAL_SKILLS_DIR):
        os.makedirs(LOCAL_SKILLS_DIR)

def clean_obsidian_syntax(content: str, filename: str) -> str:
    """
    Strips out Obsidian-specific syntax for the AI agent and injects AI instructions.
    """
    # Remove image embeds
    content = re.sub(r'!\[\[(.*?)\]\]', r'', content)
    # Convert [[Link]] or [[Link|Alias]] to just Link or Alias
    def link_replacer(match):
        inner = match.group(1)
        if '|' in inner:
            return inner.split('|')[1]
        return inner
    content = re.sub(r'\[\[(.*?)\]\]', link_replacer, content)
    
    # Inject Agent Instructions
    skill_name = filename.replace('.md', '')
    agent_instructions = f"""<agent_instructions>
# ROLE
You are an AI assistant using Sean Horgan's "{skill_name}" skill.
# RULES
1. Apply the frameworks and rubrics contained in this document precisely.
2. If this document contains a template, ensure your output matches its structure.
3. Adhere to Sean's core PM philosophy: focus on outcomes, avoid fluff, and consider the product's lifecycle stage (Explore/Expand/Extract).
</agent_instructions>

"""
    if "<agent_instructions>" not in content:
        content = agent_instructions + content
        
    return content

def add_obsidian_syntax(content: str) -> str:
    """
    Removes agent-specific instructions before syncing back to Obsidian.
    """
    content = re.sub(r'<agent_instructions>.*?</agent_instructions>\s*', '', content, flags=re.DOTALL)
    return content

def get_all_md_files(directory_path: str):
    md_files = []
    if not os.path.exists(directory_path):
        return md_files
        
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                rel_dir = os.path.relpath(root, directory_path)
                if rel_dir == '.':
                    md_files.append(file)
                else:
                    md_files.append(os.path.join(rel_dir, file))
    return md_files

def sync(dry_run=False):
    setup_directories()
    
    obsidian_files = get_all_md_files(OBSIDIAN_DIR)
    # We use global as the source of truth for existing Agent skills
    skills_files = get_all_md_files(GLOBAL_SKILLS_DIR)
    
    all_files = set(obsidian_files + skills_files)
    
    for relative_path in all_files:
        obsidian_file = os.path.join(OBSIDIAN_DIR, relative_path)
        global_skill_file = os.path.join(GLOBAL_SKILLS_DIR, relative_path)
        local_skill_file = os.path.join(LOCAL_SKILLS_DIR, relative_path)
        
        obsidian_exists = os.path.exists(obsidian_file)
        skill_exists = os.path.exists(global_skill_file)
        
        if obsidian_exists and skill_exists:
            # File exists in both places. Compare mtime using global.
            obsidian_mtime = os.path.getmtime(obsidian_file)
            skill_mtime = os.path.getmtime(global_skill_file)
            
            # Allow a small buffer (e.g., 2 seconds) to avoid sync loops
            if abs(obsidian_mtime - skill_mtime) < 2:
                continue
                
            if obsidian_mtime > skill_mtime:
                # Obsidian is newer
                print(f"Update detected in Obsidian: {relative_path}")
                if not dry_run:
                    with open(obsidian_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = clean_obsidian_syntax(content, os.path.basename(relative_path))
                    
                    # Write to both Global and Local
                    os.makedirs(os.path.dirname(global_skill_file), exist_ok=True)
                    with open(global_skill_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    os.utime(global_skill_file, (obsidian_mtime, obsidian_mtime))
                    
                    os.makedirs(os.path.dirname(local_skill_file), exist_ok=True)
                    with open(local_skill_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    os.utime(local_skill_file, (obsidian_mtime, obsidian_mtime))
                    
            elif skill_mtime > obsidian_mtime:
                # Skill is newer
                print(f"Update detected in Agent Skills: {relative_path}")
                if not dry_run:
                    with open(global_skill_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = add_obsidian_syntax(content)
                    with open(obsidian_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    # Sync mtime so they match
                    os.utime(obsidian_file, (skill_mtime, skill_mtime))
                    
                    # Also update local mirror
                    os.makedirs(os.path.dirname(local_skill_file), exist_ok=True)
                    with open(local_skill_file, 'w', encoding='utf-8') as f:
                        with open(global_skill_file, 'r', encoding='utf-8') as gf:
                            f.write(gf.read())
                    os.utime(local_skill_file, (skill_mtime, skill_mtime))
                    
        elif obsidian_exists and not skill_exists:
            # New file in Obsidian
            print(f"New file from Obsidian: {relative_path}")
            if not dry_run:
                # Ensure directories exist in both skills dirs
                os.makedirs(os.path.dirname(global_skill_file), exist_ok=True)
                os.makedirs(os.path.dirname(local_skill_file), exist_ok=True)
                
                with open(obsidian_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = clean_obsidian_syntax(content, os.path.basename(relative_path))
                
                with open(global_skill_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                mtime = os.path.getmtime(obsidian_file)
                os.utime(global_skill_file, (mtime, mtime))
                
                with open(local_skill_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                os.utime(local_skill_file, (mtime, mtime))
                
        elif skill_exists and not obsidian_exists:
            # New file in Skills
            print(f"New file from Agent Skills: {relative_path}")
            if not dry_run:
                # Ensure directories exist in Obsidian dir
                os.makedirs(os.path.dirname(obsidian_file), exist_ok=True)
                with open(global_skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = add_obsidian_syntax(content)
                with open(obsidian_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                mtime = os.path.getmtime(global_skill_file)
                os.utime(obsidian_file, (mtime, mtime))
                
                # Update local mirror
                os.makedirs(os.path.dirname(local_skill_file), exist_ok=True)
                with open(local_skill_file, 'w', encoding='utf-8') as f:
                    with open(global_skill_file, 'r', encoding='utf-8') as gf:
                        f.write(gf.read())
                os.utime(local_skill_file, (mtime, mtime))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bidirectional sync between Obsidian and Agent Skills")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without modifying files")
    args = parser.parse_args()
    
    print("Starting sync..." if not args.dry_run else "Starting DRI-RUN sync...")
    sync(args.dry_run)
    print("Sync complete.")

#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path

def find_markdown_files(directory):
    """Find all .md files in the given directory."""
    markdown_files = []
    for file in Path(directory).rglob("*.md"):
        markdown_files.append(file)
    return markdown_files

def extract_image_references(markdown_file):
    """Extract all image references from a markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match both ![]() and <img> syntax
    image_patterns = [
        r'!\[.*?\]\((.*?)\)',  # ![alt](path)
        r'<img.*?src="(.*?)".*?>',  # <img src="path">
    ]
    
    image_paths = []
    for pattern in image_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            image_path = match.group(1)
            # Handle both relative and absolute paths
            if image_path.startswith('./'):
                image_path = image_path[2:]
            image_paths.append(image_path)
    
    return image_paths

def find_assets_folders(directory):
    """Find all .assets folders in the given directory and its subdirectories."""
    assets_folders = []
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if dir == "assets":
                assets_folders.append(Path(root) / "assets")
    return assets_folders

def clean_unused_images(directory):
    """Clean unused images in .assets folders."""
    # Find all markdown files
    markdown_files = find_markdown_files(directory)
    if not markdown_files:
        print("Error: No markdown files found in the specified directory!")
        return 0, 0
    
    # Collect all referenced images
    referenced_images = set()
    for md_file in markdown_files:
        print(f"\nScanning {md_file}")
        image_refs = extract_image_references(md_file)
        for ref in image_refs:
            # Convert to absolute path
            abs_path = os.path.abspath(os.path.join(os.path.dirname(md_file), ref))
            referenced_images.add(abs_path)
    
    # Find all .assets folders
    assets_folders = find_assets_folders(directory)
    if not assets_folders:
        print("Error: No assets folders found in the specified directory!")
        return 0, 0
    
    # Count statistics
    total_images = 0
    removed_images = 0
    
    # Clean each .assets folder
    for assets_folder in assets_folders:
        print(f"\nProcessing {assets_folder}")
        
        # Get all image files in the .assets folder
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
        for file in assets_folder.iterdir():
            if file.suffix.lower() in image_extensions:
                total_images += 1
                file_path = str(file.absolute())
                
                if file_path not in referenced_images:
                    try:
                        file.unlink()
                        print(f"Removed: {file.name}")
                        removed_images += 1
                    except Exception as e:
                        print(f"Error removing {file.name}: {e}")

    return total_images, removed_images

def main():
    parser = argparse.ArgumentParser(description='Clean unused images in Typora .assets folders referenced by markdown files')
    parser.add_argument('directory', nargs='?', default='.',
                      help='Directory containing markdown files (default: current directory)')
    args = parser.parse_args()

    print("Starting cleanup process...")
    total, removed = clean_unused_images(args.directory)
    print(f"\nCleanup completed!")
    print(f"Total images found: {total}")
    print(f"Images removed: {removed}")
    print(f"Images kept: {total - removed}")
    
    # 等待用户按回车键后退出
    input("\n按回车键退出...")

if __name__ == "__main__":
    main() 
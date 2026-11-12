import os
import shutil
import sys

"""
Copies entry.png from the script's directory to the output directory.
"""

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    dst_path = os.path.join(output_dir, "entry.png")
    
    shutil.copyfile(src_path, dst_path)
    
    # Ensure byte-identical and deterministic copy by matching permissions and times if needed,
    # though shutil.copyfile just copies data. shutil.copy2 preserves metadata.
    shutil.copystat(src_path, dst_path)

if __name__ == "__main__":
    main()

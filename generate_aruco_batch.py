import os
import subprocess

def main():
    # Define the IDs to generate
    marker_ids = [41, 42, 43, 44]
    
    # Define the reference square heights (starting at 0.4, increasing by 1.2+0.4 (1.6)
    ref_heights = [0.4, 2.0, 3.6, 5.2]
    
    # Dictionary to use
    dictionary = "DICT_4X4_50"
    
    # Base parameters
    base_cmd = "python3 generate_aruco.py"
    base_cmd += " --box_side 160"
    base_cmd += " --marker_margin 20"
    base_cmd += " --box_thickness 1.2"
    base_cmd += " --marker_groove_depth 0.0001"
    base_cmd += " --layer_height 0.2"
    base_cmd += " --generate_support"  # Enable support generation
    base_cmd += f" --aruco_dictionary {dictionary}"
    
    # Generate each marker
    for i, (marker_id, ref_height) in enumerate(zip(marker_ids, ref_heights)):
        output_filename = f"id_{marker_id}"
        
        # Build the command
        cmd = f"{base_cmd} --marker_id {marker_id}"
        cmd += f" --reference_square_height {ref_height}"
        cmd += f" --output {output_filename}"
        
        print(f"Generating marker {i+1}/4: ID {marker_id} with reference height {ref_height}mm")
        subprocess.run(cmd, shell=True)
        print(f"Generated {output_filename}.stl and {output_filename}_support.stl")
    
    print("All markers and support materials generated successfully!")

if __name__ == "__main__":
    main() 
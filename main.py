import os
import subprocess

def main():
    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the IDs to generate
    marker_ids = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

    plate_thickness = 1.96
    layer_height = 0.28

    support_layers = 1

    support_thickness = support_layers * layer_height
    
    # Define the reference square heights 
    ref_heights = [support_thickness + (i * (plate_thickness + support_thickness)) for i in range(len(marker_ids))]
    
    # Dictionary to use
    dictionary = "DICT_4X4_50"
    
    # Base parameters
    base_cmd = "python3 generate_aruco.py"
    base_cmd += " --box_side 160"
    base_cmd += " --marker_margin 20"
    base_cmd += " --box_thickness " + str(plate_thickness)
    base_cmd += " --marker_groove_depth 0.0001"
    base_cmd += " --layer_height " + str(layer_height)
    base_cmd += " --support_layers " + str(support_layers)
    base_cmd += f" --aruco_dictionary {dictionary}"
    base_cmd += " --output_dir " + output_dir
    
    # Generate each marker
    for i, (marker_id, ref_height, name) in enumerate(zip(marker_ids, ref_heights, names)):
        
        # Build the command
        cmd = f"{base_cmd} --marker_id {marker_id}"
        cmd += f" --reference_square_height {ref_height}"
        cmd += f" --output {name}"
        
        print(f"Generating marker {i+1}/{len(marker_ids)}: {name}")
        subprocess.run(cmd, shell=True)
        print(f"Generated {name}.stl and support_{name}.stl")
    
    print("All markers and support materials generated successfully!")

if __name__ == "__main__":
    main() 
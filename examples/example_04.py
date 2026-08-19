# Used to import bodyprop from ../src
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

# Import bodyprop
from bodyprop import Body

body = Body()  # Empty instance

# Load model later
body.load(
    model="./objects/housing_with_groups/housing.obj",
    scale=1.0,
    density=1200.0,
    groups_density="./objects/housing_with_groups/groups_density.json"
)

body_scaled = body.scale(scale=0.01)

# Save scaled version
body_scaled.save("./objects/housing_with_groups_scaled/housing_scaled.obj")
body_scaled.save("./objects/housing_with_groups_scaled/housing_scaled.stl")

# Compute bounds
bounds_original =  body.compute_bounds()
bounds_scaled =  body_scaled.compute_bounds()

# Compute volume
volume_original =  body.compute_volume()
volume_scaled =  body_scaled.compute_volume()

# Compute mass
mass_original =  body.compute_mass()
mass_scaled =  body_scaled.compute_mass()


# Print bounds
print("")
print("Original - Cartesian bounding limits and sizes in [m]:\n"
      f"   1: min: {bounds_original[0]['min']:.6e}  max: {bounds_original[0]['max']:.6e}  size: {bounds_original[0]['size']:.6e}\n"
      f"   2: min: {bounds_original[1]['min']:.6e}  max: {bounds_original[1]['max']:.6e}  size: {bounds_original[1]['size']:.6e}\n"
      f"   3: min: {bounds_original[2]['min']:.6e}  max: {bounds_original[2]['max']:.6e}  size: {bounds_original[2]['size']:.6e}")
print("Scaled - Cartesian bounding limits and sizes in [m]:\n"
      f"   1: min: {bounds_scaled[0]['min']:.6e}  max: {bounds_scaled[0]['max']:.6e}  size: {bounds_scaled[0]['size']:.6e}\n"
      f"   2: min: {bounds_scaled[1]['min']:.6e}  max: {bounds_scaled[1]['max']:.6e}  size: {bounds_scaled[1]['size']:.6e}\n"
      f"   3: min: {bounds_scaled[2]['min']:.6e}  max: {bounds_scaled[2]['max']:.6e}  size: {bounds_scaled[2]['size']:.6e}")

# Print volume and mass 
print("")
print(f"Original - Volume in [m3]:   {volume_original:.6f}")
print(f"Scaled - Volume in [m3]:   {volume_scaled:.6f}") 
print("")
print(f"Original - Mass in [kg]:   {mass_original:.6f}")
print(f"Scaled - Mass in [kg]:   {mass_scaled:.6f}") 
print("")


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

# Compute list of objects/groups in the model
list_objects = body.list_objects()
list_groups = body.list_groups()

# Compute mass
mass =  body.compute_mass()

# Print mass / Expected 4*1200 + 4*950 = 8600 [kg]
print("")
print(f"Mass in [kg]:   {mass:.6f}") 
print("")


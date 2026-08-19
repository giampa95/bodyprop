# Used to import bodyprop from ../src
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

# Import bodyprop
from bodyprop import Body

# Pass group/object density mappings as Python dictionaries / JSON file paths
objects_density = {
    "lower_casing": 1200.0, 
    "upper_cover": 950.0 
}

body = Body(
    model="./objects/housing_with_objects/housing.obj",
    scale=[1.0, 1.0, 1.0],
    density=1000.0, # Fallback default density
    objects_density=objects_density
)

# Compute list of objects/groups in the model
list_objects = body.list_objects()
list_groups = body.list_groups()

# Compute mass for wheel rim
mass_lower_casing = body.compute_mass(object="lower_casing")
mass_upper_cover = body.compute_mass(object="upper_cover")
mass_total = body.compute_mass()

# Print list of internal objects
print("")
print(f"List of internal objects: {list_objects}")
print("")


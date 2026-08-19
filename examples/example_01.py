# Used to import bodyprop from ../src
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))


# Import bodyprop
from bodyprop import Body

# Single material OBJ scaled from millimeters to meters
body = Body(
    model="./objects/housing_with_groups/housing.obj",
    scale=0.2,          # [cm] 
    density=7850.0      # Steel density in kgpm3
)

# Compute list of objects/groups in the model
list_objects = body.list_objects()
list_groups = body.list_groups()

# Compute bounds
body_bounds = body.compute_bounds()  

# Compute properties for the body
body_volume = body.compute_volume()
body_mass = body.compute_mass()
body_com = body.compute_com() 

# Compute properties respect Center of Mass (COM) 
body_inertia_com = body.compute_inertia()
body_principal_inertia_com = body.compute_principal_inertia()

# Compute properties respect global origin (0, 0, 0)
body_inertia_origin = body.compute_inertia(x=[0.0, 0.0, 0.0])  
body_principal_inertia_origin = body.compute_principal_inertia(x=[0.0, 0.0, 0.0])


# Print some results
print(f"")
print("Cartesian bounding limits and sizes in [m]:\n"
      f"   1: min: {body_bounds[0]['min']:.6e}  max: {body_bounds[0]['max']:.6e}  size: {body_bounds[0]['size']:.6e}\n"
      f"   2: min: {body_bounds[1]['min']:.6e}  max: {body_bounds[1]['max']:.6e}  size: {body_bounds[1]['size']:.6e}\n"
      f"   3: min: {body_bounds[2]['min']:.6e}  max: {body_bounds[2]['max']:.6e}  size: {body_bounds[2]['size']:.6e}")
print(f"")
print(f"Volume in [m3]: {body_volume:.6e}")
print(f"")
print(f"Mass in [kg]:   {body_mass}")
print(f"")
print(f"Center of Mass (COM) in [m]:\n"
      f"   1: {body_com[0]:.6e}  2: {body_com[0]:.6e}  3: {body_com[0]:.6e}")      
print(f"")
print("Inertia tensor in [kg][m2]:\n"
      f"   11: {body_inertia_com[0,0]:.6e}, 12: {body_inertia_com[0,1]:.6e}, 13: {body_inertia_com[0,2]:.6e}; \n"
      f"   21: {body_inertia_com[1,0]:.6e}, 22: {body_inertia_com[1,1]:.6e}, 23: {body_inertia_com[1,2]:.6e}; \n"
      f"   31: {body_inertia_com[2,0]:.6e}, 32: {body_inertia_com[2,1]:.6e}, 33: {body_inertia_com[2,2]:.6e}")
print(f"")
print("Principal Moments (λ) in [kg][m2] and Principal Axes (u) for Inertia tensor:\n"
      f"   λ: {body_principal_inertia_com[0]["moment"]:.6e}" 
      f" # u: [{body_principal_inertia_com[0]["axis"][0]:.6e}, {body_principal_inertia_com[0]["axis"][1]:.6e}, {body_principal_inertia_com[0]["axis"][2]:.6e}]\n"
      f"   λ: {body_principal_inertia_com[1]["moment"]:.6e}" 
      f" # u: [{body_principal_inertia_com[1]["axis"][0]:.6e}, {body_principal_inertia_com[1]["axis"][1]:.6e}, {body_principal_inertia_com[1]["axis"][2]:.6e}]\n"
      f"   λ: {body_principal_inertia_com[2]["moment"]:.6e}" 
      f" # u: [{body_principal_inertia_com[2]["axis"][0]:.6e}, {body_principal_inertia_com[2]["axis"][1]:.6e}, {body_principal_inertia_com[2]["axis"][2]:.6e}]\n");
print(f"")


# Used to import bodyprop from upper hierarchical level
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import bodyprop
from bodyprop import Body

# Single material OBJ scaled from millimeters to meters
body = Body(
    model="./objects/housing_with_groups/housing.obj",
    scale=0.01,        # [cm] 
    density=7850.0     # Steel density in kgp3
)

# Compute list of objects/groups in the model
list_objects = body.list_objects()
list_groups = body.list_groups()

# Compute properties for the body
body_volume = body.compute_volume()
body_mass = body.compute_mass()
body_com = body.compute_com() 

# Compute properties respect Center of Mass (COM) 
body_inertia_com = body.compute_inertia()
body_principal_axes = body.compute_principal_axes()
body_principal_moments = body.compute_principal_moments()

# Compute properties respect global origin (0, 0, 0)
body_inertia_origin = body.compute_inertia(x=[0.0, 0.0, 0.0])   
body_principal_axes = body.compute_principal_axes(x=[0.0, 0.0, 0.0])
body_principal_moments = body.compute_principal_moments(x=[0.0, 0.0, 0.0])


# Print some results
print(f"Volume in [m3]: {body_volume:.6f}")
print(f"Mass in [kg]:   {body_mass:.6f}")
print(f"Center of Mass (COM) in [m]:\n"    
      f"   {body_com[0]:.6f}, {body_com[1]:.6f}, {body_com[2]:.6f}")
print("Inertia Matrix in [kg][m2]:\n" 
      f"   {body_inertia_com[0][0]:.6f}, {body_inertia_com[0][1]:.6f}, {body_inertia_com[0][2]:.6f}; \n"
      f"   {body_inertia_com[1][0]:.6f}, {body_inertia_com[1][1]:.6f}, {body_inertia_com[1][2]:.6f}; \n"
      f"   {body_inertia_com[2][0]:.6f}, {body_inertia_com[2][1]:.6f}, {body_inertia_com[2][2]:.6f}. \n")
"""
warehouse_usd_model.py
Creates minimal USD warehouse assets: rack, pallet, forklift.
"""
from pxr import Usd, UsdGeom

# Add error handling for USD asset creation
try:
    stage = Usd.Stage.CreateNew("warehouse_usd.usda")

    # Rack
    rack = UsdGeom.Cube.Define(stage, "/Warehouse/Rack")
    rack.CreateSizeAttr(5.0)

    # Pallet
    pallet = UsdGeom.Cube.Define(stage, "/Warehouse/Pallet")
    pallet.CreateSizeAttr(1.2)

    # Forklift
    forklift = UsdGeom.Cylinder.Define(stage, "/Warehouse/Forklift")
    forklift.CreateHeightAttr(2.0)
    forklift.CreateRadiusAttr(0.4)

    stage.GetRootLayer().Save()
    print("USD warehouse model saved as warehouse_usd.usda")
except Exception as e:
    print(f"Error creating USD warehouse model: {e}")

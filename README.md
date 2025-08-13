# Warehouse/Logistics Digital Twin POC

**NVIDIA Omniverse USD modeling. Python extension simulates forklift movement. MQTT mock stream for real-time warehouse updates. KPI logging for throughput and travel time.**

## Components
- USD assets: racks, pallets, forklift proxy
- Python extension for forklift pathing and stacking
- MQTT subscription for real-time state update
- KPI logging

## Run Instructions
1. Requires Omniverse Kit or USD Python API installed (`pip install pxr`).
2. Run `warehouse_usd_model.py` to create warehouse scene.
3. Start `forklift_simulator.py` for forklift movement simulation.
4. Run `mqtt_mock_client.py` for mock MQTT updates.
5. KPIs logged to `warehouse_kpi.log` via `kpi_logger.py`.

## Future Ideas
- Enhance with actual FSM for forklift tasks
- Connect to real sensor/MQTT feeds
- Add more complex routing and optimization

## Sample Outputs
- USD file: `warehouse_usd.usda`
- KPI log: `warehouse_kpi.log`
- Console prints for forklift and MQTT updates

## Resume/Project Description
Warehouse/Logistics Digital Twin POC
Built a digital twin of a warehouse using USD assets (Omniverse) and a Python extension to simulate forklift pathing and stacking. Integrated a mock MQTT stream for real-time updates of object states and inventory. Implemented KPI logging for throughput and travel time.

## Skills
USD (Universal Scene Description), Omniverse, Python, MQTT, Digital Twin Simulation, KPI Logging

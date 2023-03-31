from pathlib import Path

from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t
from smarts.sstudio.types import Route

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training_20s.tfrecord-00002-of-01000"
)
scenario_id = "7c81c94e23408e"

traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route = Route(
    begin=("waymo_road-214_13-215_13", 0, 8.1), end=("waymo_road-139_11-140_10", 1, 0.7)
)

ego_mission = [
    t.Mission(
        route=route, start_time=5  # Delayed start, to ensure road has prior traffic.
    )
]

gen_scenario(
    t.Scenario(
        map_spec=t.MapSpec(
            source=f"{dataset_path}#{scenario_id}", lanepoint_spacing=1.0
        ),
        traffic_histories=traffic_histories,
        ego_missions=ego_mission,
    ),
    output_dir=Path(__file__).parent,
)

from pathlib import Path
from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training_20s.tfrecord-00022-of-01000"
)
scenario_id = "1f9e1d069329cdb2"
traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route = t.Route(begin=("waymo_road-201-202", 0, 3.6), end=("waymo_road-206_4", 0, 0.2))

ego_mission = [t.Mission(route=route)]

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
from pathlib import Path
from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training_20s.tfrecord-00022-of-01000"
)
scenario_id = "b65e4295a6afd74d"
traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route = t.Route(
    begin=("waymo_road-237-235-232", 1, 12.0), end=("waymo_road-237-235-232", 1, 115.9)
)

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
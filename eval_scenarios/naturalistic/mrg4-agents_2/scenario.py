from pathlib import Path
from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training.tfrecord-00009-of-01000"
)
scenario_id = "905cf6f3fc88bd53"
traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route_1 = t.Route(
    begin=("waymo_road-222", 0, 6.8), end=("waymo_road-227-222_39", 1, 10.6)
)

route_2 = t.Route(
    begin=("waymo_road-223_8", 0, 10.3), end=("waymo_road-227-222_39", 0, 22.4)
)

ego_mission = [t.Mission(route=route_1), t.Mission(route=route_2)]

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

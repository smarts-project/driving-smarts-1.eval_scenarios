from pathlib import Path
from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training.tfrecord-00009-of-01000"
)
scenario_id = "44395f30ff206a36"
traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route_1 = t.Route(
    begin=("waymo_road-196_37-197_36-199_36-198_36", 2, 2.8),
    end=("waymo_road-290-291", 0, 5.2),
)

route_2 = t.Route(
    begin=("waymo_road-197_54-199_54", 0, 5.7), end=("waymo_road-289-232", 0, 4.7)
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

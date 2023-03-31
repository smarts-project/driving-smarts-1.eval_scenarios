from pathlib import Path
from smarts.sstudio import gen_scenario
from smarts.sstudio import types as t

dataset_path = str(
    Path(__file__).absolute().parents[1]
    / "dataset"
    / "training.tfrecord-00009-of-01000"
)
scenario_id = "33bcaba4bb59bc24"
traffic_histories = [
    t.TrafficHistoryDataset(
        name=f"waymo",
        source_type="Waymo",
        input_path=dataset_path,
        scenario_id=scenario_id,
    )
]

route_1 = t.Route(
    begin=("waymo_road-70_2-87_27-71_27", 1, 38.5),
    end=("waymo_road-83_80-89_253-70_342-87_367-71_367", 3, 1.5),
)

route_2 = t.Route(
    begin=("waymo_road-88_68-111_186", 1, 26.7),
    end=("waymo_road-88_152-89_1-70_88-87_113-71_113", 2, 59.2),
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

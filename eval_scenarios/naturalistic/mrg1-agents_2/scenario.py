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
    begin=("waymo_road-70_2-87_27-71_27", 0, 34.1),
    end=("waymo_road-89_126-70_214-87_239-71_239", 0, 10.5),
)

route_2 = t.Route(
    begin=("waymo_road-88_151-89-70_87-87_112-71_112", 1, 0.1),
    end=("waymo_road-89_126-70_214-87_239-71_239", 1, 25.7),
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

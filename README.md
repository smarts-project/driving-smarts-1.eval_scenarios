# driving-smarts-1.eval_scenarios
The evaluation scenarios that were used for "NeurIPS 2022 Driving SMARTS Competition".

## Scenario build
These scenarios are related to the [SMARTS traffic simulation](https://github.com/huawei-noah/SMARTS). The scenarios should be built with the following command:

```bash
scl scenario build-all eval_scenarios
# see https://smarts.readthedocs.io/en/latest/sim/cli.html#scl-scenario for more information
```

## Naturalistic Scenarios
Note that to use the naturalistic scenarios you will need to follow the [relevant documentation](https://smarts.readthedocs.io/en/latest/ecosystem/waymo.html).

The generated waymo tfrecords are currently expected to be located in `./dataset` for the naturalistic scenarios to consume.

from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": (
        "cryptomines_harvester cryptomines_timelord_launcher cryptomines_timelord cryptomines_farmer "
        "cryptomines_full_node cryptomines_wallet cryptomines_data_layer cryptomines_data_layer_http"
    ).split(),
    # TODO: should this be `data_layer`?
    "data": "cryptomines_wallet cryptomines_data_layer".split(),
    "data_layer_http": "cryptomines_data_layer_http".split(),
    "node": "cryptomines_full_node".split(),
    "harvester": "cryptomines_harvester".split(),
    "farmer": "cryptomines_harvester cryptomines_farmer cryptomines_full_node cryptomines_wallet".split(),
    "farmer-no-wallet": "cryptomines_harvester cryptomines_farmer cryptomines_full_node".split(),
    "farmer-only": "cryptomines_farmer".split(),
    "timelord": "cryptomines_timelord_launcher cryptomines_timelord cryptomines_full_node".split(),
    "timelord-only": "cryptomines_timelord".split(),
    "timelord-launcher-only": "cryptomines_timelord_launcher".split(),
    "wallet": "cryptomines_wallet".split(),
    "introducer": "cryptomines_introducer".split(),
    "simulator": "cryptomines_full_node_simulator".split(),
    "crawler": "cryptomines_crawler".split(),
    "seeder": "cryptomines_crawler cryptomines_seeder".split(),
    "seeder-only": "cryptomines_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())

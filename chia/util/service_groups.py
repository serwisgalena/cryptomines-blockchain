from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "cryptomines_harvester",
        "cryptomines_timelord_launcher",
        "cryptomines_timelord",
        "cryptomines_farmer",
        "cryptomines_full_node",
        "cryptomines_wallet",
        "cryptomines_data_layer",
        "cryptomines_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["cryptomines_wallet", "cryptomines_data_layer"],
    "data_layer_http": ["cryptomines_data_layer_http"],
    "node": ["cryptomines_full_node"],
    "harvester": ["cryptomines_harvester"],
    "farmer": ["cryptomines_harvester", "cryptomines_farmer", "cryptomines_full_node", "cryptomines_wallet"],
    "farmer-no-wallet": ["cryptomines_harvester", "cryptomines_farmer", "cryptomines_full_node"],
    "farmer-only": ["cryptomines_farmer"],
    "timelord": ["cryptomines_timelord_launcher", "cryptomines_timelord", "cryptomines_full_node"],
    "timelord-only": ["cryptomines_timelord"],
    "timelord-launcher-only": ["cryptomines_timelord_launcher"],
    "wallet": ["cryptomines_wallet"],
    "introducer": ["cryptomines_introducer"],
    "simulator": ["cryptomines_full_node_simulator"],
    "crawler": ["cryptomines_crawler"],
    "seeder": ["cryptomines_crawler", "cryptomines_seeder"],
    "seeder-only": ["cryptomines_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())

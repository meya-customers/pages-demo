import pytest

from component.app.login import LoginComponent
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import create_flow_next_entry
from meya.element.element_test import create_user
from meya.element.element_test import create_user_changes
from meya.element.element_test import create_user_reverse_lookup_db_request
from meya.element.element_test import verify_process_element
from meya.orb.integration import OrbIntegration
from meya.orb.integration import OrbIntegrationRef


@pytest.mark.asyncio
async def test_login_component_ok():
    integration_1 = OrbIntegration(id="orb-1")
    integration_2 = OrbIntegration(id="orb-2")
    component = LoginComponent(
        integrations=[
            OrbIntegrationRef(integration_1.id),
            OrbIntegrationRef(integration_2.id),
        ]
    )
    component_start_entry = create_component_start_entry(component)
    integration_user_id = "u-0"
    user = create_user()
    user_changes = create_user_changes(
        user,
        dict(app_user_id=integration_user_id, next_payment="July 10, 2019"),
    )
    flow_next_entry = create_flow_next_entry(component_start_entry)
    await verify_process_element(
        element=component,
        sub_entry=component_start_entry,
        user=user,
        expected_pub_entries=[flow_next_entry, *user_changes],
        expected_db_requests=[
            create_user_reverse_lookup_db_request(integration_1, user),
            create_user_reverse_lookup_db_request(
                integration_2, user, integration_user_id
            ),
        ],
        extra_elements=[integration_1, integration_2],
    )


@pytest.mark.asyncio
async def test_login_component_fail():
    integration = OrbIntegration(id="orb-1")
    component = LoginComponent(
        integrations=[OrbIntegrationRef(integration.id)]
    )
    component_start_entry = create_component_start_entry(component)
    user = create_user()
    flow_next_entry = create_flow_next_entry(component_start_entry)
    await verify_process_element(
        element=component,
        sub_entry=component_start_entry,
        user=user,
        expected_pub_entries=[flow_next_entry],
        expected_db_requests=[
            create_user_reverse_lookup_db_request(integration, user)
        ],
        extra_elements=[integration],
    )

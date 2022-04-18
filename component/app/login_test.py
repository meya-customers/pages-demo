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
    integration = OrbIntegration(id="orb-1")
    component = LoginComponent(
        integrations=[OrbIntegrationRef(integration.id)]
    )
    component_start_entry = create_component_start_entry(component)
    integration_user_id = "u-0"
    user = create_user()
    user_changes = create_user_changes(
        user, dict(logged_in=True, next_payment="July 10, 2019")
    )
    flow_next_entry = create_flow_next_entry(
        component_start_entry, data={"result": integration_user_id}
    )
    await verify_process_element(
        element=component,
        sub_entry=component_start_entry,
        user=user,
        expected_pub_entries=[flow_next_entry, *user_changes],
        expected_db_requests=[
            create_user_reverse_lookup_db_request(
                integration, user, integration_user_id
            )
        ],
        extra_elements=[integration],
    )


@pytest.mark.asyncio
async def test_login_component_fail():
    integration = OrbIntegration(id="orb-1")
    component = LoginComponent(
        integrations=[OrbIntegrationRef(integration.id)]
    )
    component_start_entry = create_component_start_entry(component)
    user = create_user()
    flow_next_entry = create_flow_next_entry(
        component_start_entry, data={"result": None}
    )
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

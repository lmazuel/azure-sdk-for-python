import os
import pytest

from _shared.asynctestcase import AsyncAppConfigTestCase

from azure.learnappconfig.aio import AppConfigurationClient
from azure.core.exceptions import ResourceNotFoundError

APP_CONFIG_URL = "https://fake-app-config-url.azconfig.io"

class AppConfigurationClientTest(AsyncAppConfigTestCase):
    def setUp(self):
        super(AppConfigurationClientTest, self).setUp()
        self.app_config_url = self.set_value_to_scrub('APP_CONFIG_URL', APP_CONFIG_URL)

    @pytest.mark.asyncio
    async def test_get_key_value(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        assert self.env_color == await client.get_configuration_setting(self.env_color_key)
        assert self.env_greeting == await client.get_configuration_setting(self.env_greeting_key)

    @pytest.mark.asyncio
    async def test_get_invalid_key(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        with pytest.raises(ResourceNotFoundError):
            await client.get_configuration_setting("KEY_THAT_DOES_NOT_EXIST")
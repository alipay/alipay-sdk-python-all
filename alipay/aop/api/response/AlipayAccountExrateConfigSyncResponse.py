#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountExrateConfigSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateConfigSyncResponse, self).__init__()
        self._config_id = None

    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateConfigSyncResponse, self).parse_response_content(response_content)
        if 'config_id' in response:
            self.config_id = response['config_id']

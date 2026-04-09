#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctoragentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctoragentCreateResponse, self).__init__()
        self._agent_id = None
        self._avatar_id = None
        self._config_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctoragentCreateResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'avatar_id' in response:
            self.avatar_id = response['avatar_id']
        if 'config_id' in response:
            self.config_id = response['config_id']

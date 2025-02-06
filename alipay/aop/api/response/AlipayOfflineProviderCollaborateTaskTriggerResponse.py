#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateTaskTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateTaskTriggerResponse, self).__init__()
        self._call_id = None

    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, value):
        self._call_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateTaskTriggerResponse, self).parse_response_content(response_content)
        if 'call_id' in response:
            self.call_id = response['call_id']

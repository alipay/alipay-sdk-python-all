#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoAgentBehaviorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAgentBehaviorQueryResponse, self).__init__()
        self._behavior = None

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        self._behavior = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAgentBehaviorQueryResponse, self).parse_response_content(response_content)
        if 'behavior' in response:
            self.behavior = response['behavior']

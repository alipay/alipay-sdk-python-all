#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseHttpaccessSwitchGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessSwitchGetResponse, self).__init__()
        self._enabled = None

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessSwitchGetResponse, self).parse_response_content(response_content)
        if 'enabled' in response:
            self.enabled = response['enabled']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseQuotacontrolSwitchGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseQuotacontrolSwitchGetResponse, self).__init__()
        self._enable = None

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseQuotacontrolSwitchGetResponse, self).parse_response_content(response_content)
        if 'enable' in response:
            self.enable = response['enable']

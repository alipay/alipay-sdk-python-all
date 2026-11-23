#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDeviceAuthorizationNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDeviceAuthorizationNotifyResponse, self).__init__()
        self._bind_id = None

    @property
    def bind_id(self):
        return self._bind_id

    @bind_id.setter
    def bind_id(self, value):
        self._bind_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDeviceAuthorizationNotifyResponse, self).parse_response_content(response_content)
        if 'bind_id' in response:
            self.bind_id = response['bind_id']

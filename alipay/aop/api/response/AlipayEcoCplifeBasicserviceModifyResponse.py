#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCplifeBasicserviceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeBasicserviceModifyResponse, self).__init__()
        self._next_action = None
        self._status = None

    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, value):
        self._next_action = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeBasicserviceModifyResponse, self).parse_response_content(response_content)
        if 'next_action' in response:
            self.next_action = response['next_action']
        if 'status' in response:
            self.status = response['status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceMessageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceMessageQueryResponse, self).__init__()
        self._send_status = None
        self._uuid = None

    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceMessageQueryResponse, self).parse_response_content(response_content)
        if 'send_status' in response:
            self.send_status = response['send_status']
        if 'uuid' in response:
            self.uuid = response['uuid']

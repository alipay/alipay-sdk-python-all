#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfSmsSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfSmsSendResponse, self).__init__()
        self._send_status = None

    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfSmsSendResponse, self).parse_response_content(response_content)
        if 'send_status' in response:
            self.send_status = response['send_status']

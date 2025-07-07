#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterStopscheduleNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterStopscheduleNotifyResponse, self).__init__()
        self._register_ids = None

    @property
    def register_ids(self):
        return self._register_ids

    @register_ids.setter
    def register_ids(self, value):
        self._register_ids = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterStopscheduleNotifyResponse, self).parse_response_content(response_content)
        if 'register_ids' in response:
            self.register_ids = response['register_ids']

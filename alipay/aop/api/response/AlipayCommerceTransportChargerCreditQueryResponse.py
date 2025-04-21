#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportChargerCreditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerCreditQueryResponse, self).__init__()
        self._invalid_time = None
        self._status = None
        self._valid_time = None

    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerCreditQueryResponse, self).parse_response_content(response_content)
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'status' in response:
            self.status = response['status']
        if 'valid_time' in response:
            self.valid_time = response['valid_time']

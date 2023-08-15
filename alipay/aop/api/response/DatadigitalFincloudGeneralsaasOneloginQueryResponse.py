#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasOneloginQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasOneloginQueryResponse, self).__init__()
        self._phone = None
        self._status = None

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasOneloginQueryResponse, self).parse_response_content(response_content)
        if 'phone' in response:
            self.phone = response['phone']
        if 'status' in response:
            self.status = response['status']

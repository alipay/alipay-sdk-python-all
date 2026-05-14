#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotManufacturerUrlModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotManufacturerUrlModifyResponse, self).__init__()
        self._flow_no = None
        self._status = None

    @property
    def flow_no(self):
        return self._flow_no

    @flow_no.setter
    def flow_no(self, value):
        self._flow_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotManufacturerUrlModifyResponse, self).parse_response_content(response_content)
        if 'flow_no' in response:
            self.flow_no = response['flow_no']
        if 'status' in response:
            self.status = response['status']

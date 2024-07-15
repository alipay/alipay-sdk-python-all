#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdIifaadidCertInvalidResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdIifaadidCertInvalidResponse, self).__init__()
        self._bsn = None
        self._data = None
        self._time_stamp = None

    @property
    def bsn(self):
        return self._bsn

    @bsn.setter
    def bsn(self, value):
        self._bsn = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdIifaadidCertInvalidResponse, self).parse_response_content(response_content)
        if 'bsn' in response:
            self.bsn = response['bsn']
        if 'data' in response:
            self.data = response['data']
        if 'time_stamp' in response:
            self.time_stamp = response['time_stamp']

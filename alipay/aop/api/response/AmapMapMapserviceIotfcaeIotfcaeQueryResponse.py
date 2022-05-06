#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AmapMapMapserviceIotfcaeIotfcaeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AmapMapMapserviceIotfcaeIotfcaeQueryResponse, self).__init__()
        self._cert_no = None
        self._data_list = None
        self._expire_date = None
        self._name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                self._data_list.append(i)
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AmapMapMapserviceIotfcaeIotfcaeQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'name' in response:
            self.name = response['name']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechQqqCccQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechQqqCccQueryResponse, self).__init__()
        self._cert_no = None
        self._city_code_open_id = None
        self._city_cppp_open_id = None
        self._province_code_open_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def city_code_open_id(self):
        return self._city_code_open_id

    @city_code_open_id.setter
    def city_code_open_id(self, value):
        if isinstance(value, list):
            self._city_code_open_id = list()
            for i in value:
                self._city_code_open_id.append(i)
    @property
    def city_cppp_open_id(self):
        return self._city_cppp_open_id

    @city_cppp_open_id.setter
    def city_cppp_open_id(self, value):
        self._city_cppp_open_id = value
    @property
    def province_code_open_id(self):
        return self._province_code_open_id

    @province_code_open_id.setter
    def province_code_open_id(self, value):
        self._province_code_open_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechQqqCccQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'city_code_open_id' in response:
            self.city_code_open_id = response['city_code_open_id']
        if 'city_cppp_open_id' in response:
            self.city_cppp_open_id = response['city_cppp_open_id']
        if 'province_code_open_id' in response:
            self.province_code_open_id = response['province_code_open_id']

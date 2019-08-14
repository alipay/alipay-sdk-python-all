#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotWifiStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotWifiStatusQueryResponse, self).__init__()
        self._cur_ssid = None
        self._ssid_list = None
        self._wifi_type = None

    @property
    def cur_ssid(self):
        return self._cur_ssid

    @cur_ssid.setter
    def cur_ssid(self, value):
        self._cur_ssid = value
    @property
    def ssid_list(self):
        return self._ssid_list

    @ssid_list.setter
    def ssid_list(self, value):
        if isinstance(value, list):
            self._ssid_list = list()
            for i in value:
                self._ssid_list.append(i)
    @property
    def wifi_type(self):
        return self._wifi_type

    @wifi_type.setter
    def wifi_type(self, value):
        self._wifi_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotWifiStatusQueryResponse, self).parse_response_content(response_content)
        if 'cur_ssid' in response:
            self.cur_ssid = response['cur_ssid']
        if 'ssid_list' in response:
            self.ssid_list = response['ssid_list']
        if 'wifi_type' in response:
            self.wifi_type = response['wifi_type']

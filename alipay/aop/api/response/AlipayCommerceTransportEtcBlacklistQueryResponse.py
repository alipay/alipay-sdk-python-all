#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcBlacklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcBlacklistQueryResponse, self).__init__()
        self._blacklist_code = None
        self._blacklist_desc = None
        self._blacklist_status = None
        self._in_time = None
        self._out_time = None
        self._plate_color = None
        self._plate_no = None

    @property
    def blacklist_code(self):
        return self._blacklist_code

    @blacklist_code.setter
    def blacklist_code(self, value):
        self._blacklist_code = value
    @property
    def blacklist_desc(self):
        return self._blacklist_desc

    @blacklist_desc.setter
    def blacklist_desc(self, value):
        self._blacklist_desc = value
    @property
    def blacklist_status(self):
        return self._blacklist_status

    @blacklist_status.setter
    def blacklist_status(self, value):
        self._blacklist_status = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcBlacklistQueryResponse, self).parse_response_content(response_content)
        if 'blacklist_code' in response:
            self.blacklist_code = response['blacklist_code']
        if 'blacklist_desc' in response:
            self.blacklist_desc = response['blacklist_desc']
        if 'blacklist_status' in response:
            self.blacklist_status = response['blacklist_status']
        if 'in_time' in response:
            self.in_time = response['in_time']
        if 'out_time' in response:
            self.out_time = response['out_time']
        if 'plate_color' in response:
            self.plate_color = response['plate_color']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']

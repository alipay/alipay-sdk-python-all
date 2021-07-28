#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AliosOpenAutoInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AliosOpenAutoInfoQueryResponse, self).__init__()
        self._engine_no = None
        self._license_no = None
        self._user_activation_time = None
        self._vehicle_type = None
        self._vin = None

    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def user_activation_time(self):
        return self._user_activation_time

    @user_activation_time.setter
    def user_activation_time(self, value):
        self._user_activation_time = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value

    def parse_response_content(self, response_content):
        response = super(AliosOpenAutoInfoQueryResponse, self).parse_response_content(response_content)
        if 'engine_no' in response:
            self.engine_no = response['engine_no']
        if 'license_no' in response:
            self.license_no = response['license_no']
        if 'user_activation_time' in response:
            self.user_activation_time = response['user_activation_time']
        if 'vehicle_type' in response:
            self.vehicle_type = response['vehicle_type']
        if 'vin' in response:
            self.vin = response['vin']

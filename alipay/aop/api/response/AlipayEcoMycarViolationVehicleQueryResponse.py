#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarViolationVehicleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarViolationVehicleQueryResponse, self).__init__()
        self._engine_no = None
        self._vi_id = None
        self._vi_number = None
        self._vin_no = None

    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value
    @property
    def vin_no(self):
        return self._vin_no

    @vin_no.setter
    def vin_no(self, value):
        self._vin_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarViolationVehicleQueryResponse, self).parse_response_content(response_content)
        if 'engine_no' in response:
            self.engine_no = response['engine_no']
        if 'vi_id' in response:
            self.vi_id = response['vi_id']
        if 'vi_number' in response:
            self.vi_number = response['vi_number']
        if 'vin_no' in response:
            self.vin_no = response['vin_no']

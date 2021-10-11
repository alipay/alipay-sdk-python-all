#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiOrderpriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiOrderpriceQueryResponse, self).__init__()
        self._dispatch_amount = None
        self._end_time = None
        self._error_code = None
        self._error_msg = None
        self._mileage = None
        self._oil_amount = None
        self._plate_no = None
        self._start_time = None
        self._trip_amount = None

    @property
    def dispatch_amount(self):
        return self._dispatch_amount

    @dispatch_amount.setter
    def dispatch_amount(self, value):
        self._dispatch_amount = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage = value
    @property
    def oil_amount(self):
        return self._oil_amount

    @oil_amount.setter
    def oil_amount(self, value):
        self._oil_amount = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def trip_amount(self):
        return self._trip_amount

    @trip_amount.setter
    def trip_amount(self, value):
        self._trip_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiOrderpriceQueryResponse, self).parse_response_content(response_content)
        if 'dispatch_amount' in response:
            self.dispatch_amount = response['dispatch_amount']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'mileage' in response:
            self.mileage = response['mileage']
        if 'oil_amount' in response:
            self.oil_amount = response['oil_amount']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'trip_amount' in response:
            self.trip_amount = response['trip_amount']

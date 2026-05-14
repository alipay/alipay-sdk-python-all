#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinValuationQueryResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinValuationQueryResponse, self).__init__()
        self._car_license = None
        self._excellent_valuation_amt = None
        self._good_valuation_amt = None
        self._valuation_time = None

    @property
    def car_license(self):
        return self._car_license

    @car_license.setter
    def car_license(self, value):
        self._car_license = value
    @property
    def excellent_valuation_amt(self):
        return self._excellent_valuation_amt

    @excellent_valuation_amt.setter
    def excellent_valuation_amt(self, value):
        self._excellent_valuation_amt = value
    @property
    def good_valuation_amt(self):
        return self._good_valuation_amt

    @good_valuation_amt.setter
    def good_valuation_amt(self, value):
        self._good_valuation_amt = value
    @property
    def valuation_time(self):
        return self._valuation_time

    @valuation_time.setter
    def valuation_time(self, value):
        self._valuation_time = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinValuationQueryResponse, self).parse_response_content(response_content)
        if 'car_license' in response:
            self.car_license = response['car_license']
        if 'excellent_valuation_amt' in response:
            self.excellent_valuation_amt = response['excellent_valuation_amt']
        if 'good_valuation_amt' in response:
            self.good_valuation_amt = response['good_valuation_amt']
        if 'valuation_time' in response:
            self.valuation_time = response['valuation_time']

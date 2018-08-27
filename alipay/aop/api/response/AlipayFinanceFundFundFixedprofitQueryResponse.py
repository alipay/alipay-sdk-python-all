#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceFundFundFixedprofitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundFundFixedprofitQueryResponse, self).__init__()
        self._last_five_year = None
        self._last_one_year = None
        self._last_three_year = None
        self._last_two_year = None
        self._since_establish = None

    @property
    def last_five_year(self):
        return self._last_five_year

    @last_five_year.setter
    def last_five_year(self, value):
        self._last_five_year = value
    @property
    def last_one_year(self):
        return self._last_one_year

    @last_one_year.setter
    def last_one_year(self, value):
        self._last_one_year = value
    @property
    def last_three_year(self):
        return self._last_three_year

    @last_three_year.setter
    def last_three_year(self, value):
        self._last_three_year = value
    @property
    def last_two_year(self):
        return self._last_two_year

    @last_two_year.setter
    def last_two_year(self, value):
        self._last_two_year = value
    @property
    def since_establish(self):
        return self._since_establish

    @since_establish.setter
    def since_establish(self, value):
        self._since_establish = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundFundFixedprofitQueryResponse, self).parse_response_content(response_content)
        if 'last_five_year' in response:
            self.last_five_year = response['last_five_year']
        if 'last_one_year' in response:
            self.last_one_year = response['last_one_year']
        if 'last_three_year' in response:
            self.last_three_year = response['last_three_year']
        if 'last_two_year' in response:
            self.last_two_year = response['last_two_year']
        if 'since_establish' in response:
            self.since_establish = response['since_establish']

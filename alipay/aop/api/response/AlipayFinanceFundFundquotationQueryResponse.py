#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceFundFundquotationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundFundquotationQueryResponse, self).__init__()
        self._last_half_year = None
        self._last_month = None
        self._last_quarter = None
        self._last_week = None
        self._last_year = None
        self._report_date = None
        self._since_establishment = None
        self._this_year = None
        self._yield_3_year = None
        self._yield_5_year = None

    @property
    def last_half_year(self):
        return self._last_half_year

    @last_half_year.setter
    def last_half_year(self, value):
        self._last_half_year = value
    @property
    def last_month(self):
        return self._last_month

    @last_month.setter
    def last_month(self, value):
        self._last_month = value
    @property
    def last_quarter(self):
        return self._last_quarter

    @last_quarter.setter
    def last_quarter(self, value):
        self._last_quarter = value
    @property
    def last_week(self):
        return self._last_week

    @last_week.setter
    def last_week(self, value):
        self._last_week = value
    @property
    def last_year(self):
        return self._last_year

    @last_year.setter
    def last_year(self, value):
        self._last_year = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def since_establishment(self):
        return self._since_establishment

    @since_establishment.setter
    def since_establishment(self, value):
        self._since_establishment = value
    @property
    def this_year(self):
        return self._this_year

    @this_year.setter
    def this_year(self, value):
        self._this_year = value
    @property
    def yield_3_year(self):
        return self._yield_3_year

    @yield_3_year.setter
    def yield_3_year(self, value):
        self._yield_3_year = value
    @property
    def yield_5_year(self):
        return self._yield_5_year

    @yield_5_year.setter
    def yield_5_year(self, value):
        self._yield_5_year = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundFundquotationQueryResponse, self).parse_response_content(response_content)
        if 'last_half_year' in response:
            self.last_half_year = response['last_half_year']
        if 'last_month' in response:
            self.last_month = response['last_month']
        if 'last_quarter' in response:
            self.last_quarter = response['last_quarter']
        if 'last_week' in response:
            self.last_week = response['last_week']
        if 'last_year' in response:
            self.last_year = response['last_year']
        if 'report_date' in response:
            self.report_date = response['report_date']
        if 'since_establishment' in response:
            self.since_establishment = response['since_establishment']
        if 'this_year' in response:
            self.this_year = response['this_year']
        if 'yield_3_year' in response:
            self.yield_3_year = response['yield_3_year']
        if 'yield_5_year' in response:
            self.yield_5_year = response['yield_5_year']

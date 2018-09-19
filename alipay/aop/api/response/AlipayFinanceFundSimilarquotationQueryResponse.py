#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceFundSimilarquotationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundSimilarquotationQueryResponse, self).__init__()
        self._last_half_year_count = None
        self._last_half_year_order = None
        self._last_half_year_similar = None
        self._last_month_count = None
        self._last_month_order = None
        self._last_month_similar = None
        self._last_quarter_count = None
        self._last_quarter_order = None
        self._last_quarter_similar = None
        self._last_year_count = None
        self._last_year_order = None
        self._last_year_similar = None
        self._report_date = None
        self._yield_three_year_count = None
        self._yield_three_year_order = None
        self._yield_three_year_similar = None

    @property
    def last_half_year_count(self):
        return self._last_half_year_count

    @last_half_year_count.setter
    def last_half_year_count(self, value):
        self._last_half_year_count = value
    @property
    def last_half_year_order(self):
        return self._last_half_year_order

    @last_half_year_order.setter
    def last_half_year_order(self, value):
        self._last_half_year_order = value
    @property
    def last_half_year_similar(self):
        return self._last_half_year_similar

    @last_half_year_similar.setter
    def last_half_year_similar(self, value):
        self._last_half_year_similar = value
    @property
    def last_month_count(self):
        return self._last_month_count

    @last_month_count.setter
    def last_month_count(self, value):
        self._last_month_count = value
    @property
    def last_month_order(self):
        return self._last_month_order

    @last_month_order.setter
    def last_month_order(self, value):
        self._last_month_order = value
    @property
    def last_month_similar(self):
        return self._last_month_similar

    @last_month_similar.setter
    def last_month_similar(self, value):
        self._last_month_similar = value
    @property
    def last_quarter_count(self):
        return self._last_quarter_count

    @last_quarter_count.setter
    def last_quarter_count(self, value):
        self._last_quarter_count = value
    @property
    def last_quarter_order(self):
        return self._last_quarter_order

    @last_quarter_order.setter
    def last_quarter_order(self, value):
        self._last_quarter_order = value
    @property
    def last_quarter_similar(self):
        return self._last_quarter_similar

    @last_quarter_similar.setter
    def last_quarter_similar(self, value):
        self._last_quarter_similar = value
    @property
    def last_year_count(self):
        return self._last_year_count

    @last_year_count.setter
    def last_year_count(self, value):
        self._last_year_count = value
    @property
    def last_year_order(self):
        return self._last_year_order

    @last_year_order.setter
    def last_year_order(self, value):
        self._last_year_order = value
    @property
    def last_year_similar(self):
        return self._last_year_similar

    @last_year_similar.setter
    def last_year_similar(self, value):
        self._last_year_similar = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def yield_three_year_count(self):
        return self._yield_three_year_count

    @yield_three_year_count.setter
    def yield_three_year_count(self, value):
        self._yield_three_year_count = value
    @property
    def yield_three_year_order(self):
        return self._yield_three_year_order

    @yield_three_year_order.setter
    def yield_three_year_order(self, value):
        self._yield_three_year_order = value
    @property
    def yield_three_year_similar(self):
        return self._yield_three_year_similar

    @yield_three_year_similar.setter
    def yield_three_year_similar(self, value):
        self._yield_three_year_similar = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundSimilarquotationQueryResponse, self).parse_response_content(response_content)
        if 'last_half_year_count' in response:
            self.last_half_year_count = response['last_half_year_count']
        if 'last_half_year_order' in response:
            self.last_half_year_order = response['last_half_year_order']
        if 'last_half_year_similar' in response:
            self.last_half_year_similar = response['last_half_year_similar']
        if 'last_month_count' in response:
            self.last_month_count = response['last_month_count']
        if 'last_month_order' in response:
            self.last_month_order = response['last_month_order']
        if 'last_month_similar' in response:
            self.last_month_similar = response['last_month_similar']
        if 'last_quarter_count' in response:
            self.last_quarter_count = response['last_quarter_count']
        if 'last_quarter_order' in response:
            self.last_quarter_order = response['last_quarter_order']
        if 'last_quarter_similar' in response:
            self.last_quarter_similar = response['last_quarter_similar']
        if 'last_year_count' in response:
            self.last_year_count = response['last_year_count']
        if 'last_year_order' in response:
            self.last_year_order = response['last_year_order']
        if 'last_year_similar' in response:
            self.last_year_similar = response['last_year_similar']
        if 'report_date' in response:
            self.report_date = response['report_date']
        if 'yield_three_year_count' in response:
            self.yield_three_year_count = response['yield_three_year_count']
        if 'yield_three_year_order' in response:
            self.yield_three_year_order = response['yield_three_year_order']
        if 'yield_three_year_similar' in response:
            self.yield_three_year_similar = response['yield_three_year_similar']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CarbonTrans import CarbonTrans


class AlipaySocialAntforestCarbonmonthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestCarbonmonthQueryResponse, self).__init__()
        self._forest_open = None
        self._month_trans_list = None
        self._year = None

    @property
    def forest_open(self):
        return self._forest_open

    @forest_open.setter
    def forest_open(self, value):
        self._forest_open = value
    @property
    def month_trans_list(self):
        return self._month_trans_list

    @month_trans_list.setter
    def month_trans_list(self, value):
        if isinstance(value, list):
            self._month_trans_list = list()
            for i in value:
                if isinstance(i, CarbonTrans):
                    self._month_trans_list.append(i)
                else:
                    self._month_trans_list.append(CarbonTrans.from_alipay_dict(i))
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestCarbonmonthQueryResponse, self).parse_response_content(response_content)
        if 'forest_open' in response:
            self.forest_open = response['forest_open']
        if 'month_trans_list' in response:
            self.month_trans_list = response['month_trans_list']
        if 'year' in response:
            self.year = response['year']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CarbonTrans import CarbonTrans


class AlipaySocialAntforestCarbondayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestCarbondayQueryResponse, self).__init__()
        self._day_trans_list = None
        self._forest_open = None
        self._year = None

    @property
    def day_trans_list(self):
        return self._day_trans_list

    @day_trans_list.setter
    def day_trans_list(self, value):
        if isinstance(value, list):
            self._day_trans_list = list()
            for i in value:
                if isinstance(i, CarbonTrans):
                    self._day_trans_list.append(i)
                else:
                    self._day_trans_list.append(CarbonTrans.from_alipay_dict(i))
    @property
    def forest_open(self):
        return self._forest_open

    @forest_open.setter
    def forest_open(self, value):
        self._forest_open = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestCarbondayQueryResponse, self).parse_response_content(response_content)
        if 'day_trans_list' in response:
            self.day_trans_list = response['day_trans_list']
        if 'forest_open' in response:
            self.forest_open = response['forest_open']
        if 'year' in response:
            self.year = response['year']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntProdpaasArrangementRebateRateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasArrangementRebateRateQueryResponse, self).__init__()
        self._category_1_id = None
        self._category_1_name = None
        self._gmt_end = None
        self._gmt_start = None
        self._rate = None

    @property
    def category_1_id(self):
        return self._category_1_id

    @category_1_id.setter
    def category_1_id(self, value):
        self._category_1_id = value
    @property
    def category_1_name(self):
        return self._category_1_name

    @category_1_name.setter
    def category_1_name(self, value):
        self._category_1_name = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value

    def parse_response_content(self, response_content):
        response = super(AntProdpaasArrangementRebateRateQueryResponse, self).parse_response_content(response_content)
        if 'category_1_id' in response:
            self.category_1_id = response['category_1_id']
        if 'category_1_name' in response:
            self.category_1_name = response['category_1_name']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'rate' in response:
            self.rate = response['rate']

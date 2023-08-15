#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubOrderResult import SubOrderResult


class AlipayTradeMergeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeMergeCreateResponse, self).__init__()
        self._merge_no = None
        self._order_detail_results = None
        self._out_merge_no = None

    @property
    def merge_no(self):
        return self._merge_no

    @merge_no.setter
    def merge_no(self, value):
        self._merge_no = value
    @property
    def order_detail_results(self):
        return self._order_detail_results

    @order_detail_results.setter
    def order_detail_results(self, value):
        if isinstance(value, list):
            self._order_detail_results = list()
            for i in value:
                if isinstance(i, SubOrderResult):
                    self._order_detail_results.append(i)
                else:
                    self._order_detail_results.append(SubOrderResult.from_alipay_dict(i))
    @property
    def out_merge_no(self):
        return self._out_merge_no

    @out_merge_no.setter
    def out_merge_no(self, value):
        self._out_merge_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeMergeCreateResponse, self).parse_response_content(response_content)
        if 'merge_no' in response:
            self.merge_no = response['merge_no']
        if 'order_detail_results' in response:
            self.order_detail_results = response['order_detail_results']
        if 'out_merge_no' in response:
            self.out_merge_no = response['out_merge_no']

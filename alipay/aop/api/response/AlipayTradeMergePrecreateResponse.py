#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PreOrderResult import PreOrderResult


class AlipayTradeMergePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeMergePrecreateResponse, self).__init__()
        self._order_detail_results = None
        self._out_merge_no = None
        self._pre_order_no = None

    @property
    def order_detail_results(self):
        return self._order_detail_results

    @order_detail_results.setter
    def order_detail_results(self, value):
        if isinstance(value, list):
            self._order_detail_results = list()
            for i in value:
                if isinstance(i, PreOrderResult):
                    self._order_detail_results.append(i)
                else:
                    self._order_detail_results.append(PreOrderResult.from_alipay_dict(i))
    @property
    def out_merge_no(self):
        return self._out_merge_no

    @out_merge_no.setter
    def out_merge_no(self, value):
        self._out_merge_no = value
    @property
    def pre_order_no(self):
        return self._pre_order_no

    @pre_order_no.setter
    def pre_order_no(self, value):
        self._pre_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeMergePrecreateResponse, self).parse_response_content(response_content)
        if 'order_detail_results' in response:
            self.order_detail_results = response['order_detail_results']
        if 'out_merge_no' in response:
            self.out_merge_no = response['out_merge_no']
        if 'pre_order_no' in response:
            self.pre_order_no = response['pre_order_no']

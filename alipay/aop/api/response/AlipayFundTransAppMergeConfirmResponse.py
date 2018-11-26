#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransOrderResult import TransOrderResult


class AlipayFundTransAppMergeConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAppMergeConfirmResponse, self).__init__()
        self._merge_order_id = None
        self._trans_order_results = None

    @property
    def merge_order_id(self):
        return self._merge_order_id

    @merge_order_id.setter
    def merge_order_id(self, value):
        self._merge_order_id = value
    @property
    def trans_order_results(self):
        return self._trans_order_results

    @trans_order_results.setter
    def trans_order_results(self, value):
        if isinstance(value, list):
            self._trans_order_results = list()
            for i in value:
                if isinstance(i, TransOrderResult):
                    self._trans_order_results.append(i)
                else:
                    self._trans_order_results.append(TransOrderResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAppMergeConfirmResponse, self).parse_response_content(response_content)
        if 'merge_order_id' in response:
            self.merge_order_id = response['merge_order_id']
        if 'trans_order_results' in response:
            self.trans_order_results = response['trans_order_results']

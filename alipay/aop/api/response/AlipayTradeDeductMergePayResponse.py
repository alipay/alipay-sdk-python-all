#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubOrderResult import SubOrderResult


class AlipayTradeDeductMergePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeDeductMergePayResponse, self).__init__()
        self._buyer_user_id = None
        self._order_detail_results = None
        self._out_merge_no = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
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
        response = super(AlipayTradeDeductMergePayResponse, self).parse_response_content(response_content)
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'order_detail_results' in response:
            self.order_detail_results = response['order_detail_results']
        if 'out_merge_no' in response:
            self.out_merge_no = response['out_merge_no']

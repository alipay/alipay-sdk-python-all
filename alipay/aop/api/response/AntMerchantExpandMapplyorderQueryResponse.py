#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantApplyResultRecord import MerchantApplyResultRecord


class AntMerchantExpandMapplyorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMapplyorderQueryResponse, self).__init__()
        self._order_no = None
        self._order_status = None
        self._out_biz_no = None
        self._result_info = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def result_info(self):
        return self._result_info

    @result_info.setter
    def result_info(self, value):
        if isinstance(value, list):
            self._result_info = list()
            for i in value:
                if isinstance(i, MerchantApplyResultRecord):
                    self._result_info.append(i)
                else:
                    self._result_info.append(MerchantApplyResultRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMapplyorderQueryResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'result_info' in response:
            self.result_info = response['result_info']

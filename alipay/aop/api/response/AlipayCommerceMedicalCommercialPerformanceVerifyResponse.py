#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialPerformanceVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialPerformanceVerifyResponse, self).__init__()
        self._biz_order_id = None
        self._out_biz_no = None
        self._out_product_id = None
        self._verify_result = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialPerformanceVerifyResponse, self).parse_response_content(response_content)
        if 'biz_order_id' in response:
            self.biz_order_id = response['biz_order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_product_id' in response:
            self.out_product_id = response['out_product_id']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']

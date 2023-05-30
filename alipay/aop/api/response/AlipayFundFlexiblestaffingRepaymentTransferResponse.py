#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingRepaymentTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingRepaymentTransferResponse, self).__init__()
        self._biz_scene = None
        self._fund_order_id = None
        self._out_biz_no = None
        self._product_code = None
        self._status = None
        self._trans_date = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def fund_order_id(self):
        return self._fund_order_id

    @fund_order_id.setter
    def fund_order_id(self, value):
        self._fund_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingRepaymentTransferResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'fund_order_id' in response:
            self.fund_order_id = response['fund_order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
        if 'trans_date' in response:
            self.trans_date = response['trans_date']

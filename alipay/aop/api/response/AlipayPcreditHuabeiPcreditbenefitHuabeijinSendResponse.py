#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditbenefitHuabeijinSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitHuabeijinSendResponse, self).__init__()
        self._activity_order_id = None
        self._calculated_amount = None
        self._hb_biz_code = None
        self._out_biz_no = None
        self._product_id = None

    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def calculated_amount(self):
        return self._calculated_amount

    @calculated_amount.setter
    def calculated_amount(self, value):
        self._calculated_amount = value
    @property
    def hb_biz_code(self):
        return self._hb_biz_code

    @hb_biz_code.setter
    def hb_biz_code(self, value):
        self._hb_biz_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitHuabeijinSendResponse, self).parse_response_content(response_content)
        if 'activity_order_id' in response:
            self.activity_order_id = response['activity_order_id']
        if 'calculated_amount' in response:
            self.calculated_amount = response['calculated_amount']
        if 'hb_biz_code' in response:
            self.hb_biz_code = response['hb_biz_code']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_id' in response:
            self.product_id = response['product_id']

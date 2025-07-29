#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditGoodsConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditGoodsConfirmResponse, self).__init__()
        self._credit_biz_order_id = None
        self._credit_confirm_receive_goods_time = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def credit_confirm_receive_goods_time(self):
        return self._credit_confirm_receive_goods_time

    @credit_confirm_receive_goods_time.setter
    def credit_confirm_receive_goods_time(self, value):
        self._credit_confirm_receive_goods_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditGoodsConfirmResponse, self).parse_response_content(response_content)
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'credit_confirm_receive_goods_time' in response:
            self.credit_confirm_receive_goods_time = response['credit_confirm_receive_goods_time']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderRentCompleteResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderRentCompleteResponse, self).__init__()
        self._alipay_fund_order_no = None
        self._order_no = None
        self._user_id = None

    @property
    def alipay_fund_order_no(self):
        return self._alipay_fund_order_no

    @alipay_fund_order_no.setter
    def alipay_fund_order_no(self, value):
        self._alipay_fund_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderRentCompleteResponse, self).parse_response_content(response_content)
        if 'alipay_fund_order_no' in response:
            self.alipay_fund_order_no = response['alipay_fund_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'user_id' in response:
            self.user_id = response['user_id']

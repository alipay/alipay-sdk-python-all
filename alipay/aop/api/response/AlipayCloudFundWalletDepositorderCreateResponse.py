#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundWalletDepositorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundWalletDepositorderCreateResponse, self).__init__()
        self._fund_order_id = None
        self._out_biz_no = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundWalletDepositorderCreateResponse, self).parse_response_content(response_content)
        if 'fund_order_id' in response:
            self.fund_order_id = response['fund_order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']

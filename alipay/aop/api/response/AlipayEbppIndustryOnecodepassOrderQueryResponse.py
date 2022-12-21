#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryOnecodepassOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryOnecodepassOrderQueryResponse, self).__init__()
        self._buyer_pay_amount = None
        self._org_buyer_openid = None
        self._org_buyer_unionid = None
        self._out_trade_no = None
        self._status = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def org_buyer_openid(self):
        return self._org_buyer_openid

    @org_buyer_openid.setter
    def org_buyer_openid(self, value):
        self._org_buyer_openid = value
    @property
    def org_buyer_unionid(self):
        return self._org_buyer_unionid

    @org_buyer_unionid.setter
    def org_buyer_unionid(self, value):
        self._org_buyer_unionid = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryOnecodepassOrderQueryResponse, self).parse_response_content(response_content)
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'org_buyer_openid' in response:
            self.org_buyer_openid = response['org_buyer_openid']
        if 'org_buyer_unionid' in response:
            self.org_buyer_unionid = response['org_buyer_unionid']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']

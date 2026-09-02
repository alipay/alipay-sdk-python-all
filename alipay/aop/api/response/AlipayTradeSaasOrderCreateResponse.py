#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasAccountInfo import SaasAccountInfo


class AlipayTradeSaasOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasOrderCreateResponse, self).__init__()
        self._cashier_url = None
        self._order_no = None
        self._out_trade_no = None
        self._saas_account_info = None
        self._trade_no = None
        self._trade_status = None

    @property
    def cashier_url(self):
        return self._cashier_url

    @cashier_url.setter
    def cashier_url(self, value):
        self._cashier_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def saas_account_info(self):
        return self._saas_account_info

    @saas_account_info.setter
    def saas_account_info(self, value):
        if isinstance(value, SaasAccountInfo):
            self._saas_account_info = value
        else:
            self._saas_account_info = SaasAccountInfo.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasOrderCreateResponse, self).parse_response_content(response_content)
        if 'cashier_url' in response:
            self.cashier_url = response['cashier_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'saas_account_info' in response:
            self.saas_account_info = response['saas_account_info']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']

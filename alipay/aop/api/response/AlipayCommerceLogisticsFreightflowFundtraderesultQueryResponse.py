#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowFundtraderesultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowFundtraderesultQueryResponse, self).__init__()
        self._currency = None
        self._pay_asset_type = None
        self._pay_status = None
        self._payee_id = None
        self._payer_name = None
        self._total_amount = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def pay_asset_type(self):
        return self._pay_asset_type

    @pay_asset_type.setter
    def pay_asset_type(self, value):
        self._pay_asset_type = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def payee_id(self):
        return self._payee_id

    @payee_id.setter
    def payee_id(self, value):
        self._payee_id = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowFundtraderesultQueryResponse, self).parse_response_content(response_content)
        if 'currency' in response:
            self.currency = response['currency']
        if 'pay_asset_type' in response:
            self.pay_asset_type = response['pay_asset_type']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'payee_id' in response:
            self.payee_id = response['payee_id']
        if 'payer_name' in response:
            self.payer_name = response['payer_name']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']

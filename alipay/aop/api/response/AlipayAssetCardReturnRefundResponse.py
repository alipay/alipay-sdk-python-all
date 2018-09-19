#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetCardReturnRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetCardReturnRefundResponse, self).__init__()
        self._account_dt = None
        self._order_no = None
        self._return_amount = None
        self._return_asset_amont = None
        self._return_fee_amount = None
        self._return_fee_asset_amount = None

    @property
    def account_dt(self):
        return self._account_dt

    @account_dt.setter
    def account_dt(self, value):
        self._account_dt = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def return_amount(self):
        return self._return_amount

    @return_amount.setter
    def return_amount(self, value):
        self._return_amount = value
    @property
    def return_asset_amont(self):
        return self._return_asset_amont

    @return_asset_amont.setter
    def return_asset_amont(self, value):
        self._return_asset_amont = value
    @property
    def return_fee_amount(self):
        return self._return_fee_amount

    @return_fee_amount.setter
    def return_fee_amount(self, value):
        self._return_fee_amount = value
    @property
    def return_fee_asset_amount(self):
        return self._return_fee_asset_amount

    @return_fee_asset_amount.setter
    def return_fee_asset_amount(self, value):
        self._return_fee_asset_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetCardReturnRefundResponse, self).parse_response_content(response_content)
        if 'account_dt' in response:
            self.account_dt = response['account_dt']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'return_amount' in response:
            self.return_amount = response['return_amount']
        if 'return_asset_amont' in response:
            self.return_asset_amont = response['return_asset_amont']
        if 'return_fee_amount' in response:
            self.return_fee_amount = response['return_fee_amount']
        if 'return_fee_asset_amount' in response:
            self.return_fee_asset_amount = response['return_fee_asset_amount']

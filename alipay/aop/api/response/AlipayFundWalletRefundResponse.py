#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletRefundResponse, self).__init__()
        self._actual_amount = None
        self._amount = None
        self._batch_bill_no = None
        self._biz_scene = None
        self._user_wallet_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def batch_bill_no(self):
        return self._batch_bill_no

    @batch_bill_no.setter
    def batch_bill_no(self, value):
        self._batch_bill_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletRefundResponse, self).parse_response_content(response_content)
        if 'actual_amount' in response:
            self.actual_amount = response['actual_amount']
        if 'amount' in response:
            self.amount = response['amount']
        if 'batch_bill_no' in response:
            self.batch_bill_no = response['batch_bill_no']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']

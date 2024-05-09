#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundWalletConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundWalletConsultResponse, self).__init__()
        self._actual_available_amount = None
        self._asset_no = None
        self._available_amount = None
        self._total_amount = None
        self._user_wallet_id = None

    @property
    def actual_available_amount(self):
        return self._actual_available_amount

    @actual_available_amount.setter
    def actual_available_amount(self, value):
        self._actual_available_amount = value
    @property
    def asset_no(self):
        return self._asset_no

    @asset_no.setter
    def asset_no(self, value):
        self._asset_no = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundWalletConsultResponse, self).parse_response_content(response_content)
        if 'actual_available_amount' in response:
            self.actual_available_amount = response['actual_available_amount']
        if 'asset_no' in response:
            self.asset_no = response['asset_no']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']

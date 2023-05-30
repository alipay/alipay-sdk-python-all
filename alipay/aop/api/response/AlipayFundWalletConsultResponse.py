#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletConsultResponse, self).__init__()
        self._actual_available_amount = None
        self._amount_details = None
        self._available_amount = None
        self._error_code = None
        self._error_msg = None
        self._total_amount = None
        self._user_wallet_id = None
        self._user_wallet_status = None
        self._wallet_owner_status = None

    @property
    def actual_available_amount(self):
        return self._actual_available_amount

    @actual_available_amount.setter
    def actual_available_amount(self, value):
        self._actual_available_amount = value
    @property
    def amount_details(self):
        return self._amount_details

    @amount_details.setter
    def amount_details(self, value):
        self._amount_details = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
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
    @property
    def user_wallet_status(self):
        return self._user_wallet_status

    @user_wallet_status.setter
    def user_wallet_status(self, value):
        self._user_wallet_status = value
    @property
    def wallet_owner_status(self):
        return self._wallet_owner_status

    @wallet_owner_status.setter
    def wallet_owner_status(self, value):
        self._wallet_owner_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletConsultResponse, self).parse_response_content(response_content)
        if 'actual_available_amount' in response:
            self.actual_available_amount = response['actual_available_amount']
        if 'amount_details' in response:
            self.amount_details = response['amount_details']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
        if 'user_wallet_status' in response:
            self.user_wallet_status = response['user_wallet_status']
        if 'wallet_owner_status' in response:
            self.wallet_owner_status = response['wallet_owner_status']

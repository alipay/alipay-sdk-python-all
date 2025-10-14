#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsWalletAutodepositstatusGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsWalletAutodepositstatusGetResponse, self).__init__()
        self._auto_deposit_status = None
        self._user_operation_time = None
        self._user_wallet_id = None
        self._wallet_partner_id = None

    @property
    def auto_deposit_status(self):
        return self._auto_deposit_status

    @auto_deposit_status.setter
    def auto_deposit_status(self, value):
        self._auto_deposit_status = value
    @property
    def user_operation_time(self):
        return self._user_operation_time

    @user_operation_time.setter
    def user_operation_time(self, value):
        self._user_operation_time = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value
    @property
    def wallet_partner_id(self):
        return self._wallet_partner_id

    @wallet_partner_id.setter
    def wallet_partner_id(self, value):
        self._wallet_partner_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsWalletAutodepositstatusGetResponse, self).parse_response_content(response_content)
        if 'auto_deposit_status' in response:
            self.auto_deposit_status = response['auto_deposit_status']
        if 'user_operation_time' in response:
            self.user_operation_time = response['user_operation_time']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
        if 'wallet_partner_id' in response:
            self.wallet_partner_id = response['wallet_partner_id']

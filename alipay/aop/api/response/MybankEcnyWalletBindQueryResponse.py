#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyWalletBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyWalletBindQueryResponse, self).__init__()
        self._bind_ar_no = None
        self._bind_time = None
        self._freeze_type = None
        self._has_bound = None
        self._identify_token = None
        self._quota_control_flag = None
        self._role_type = None
        self._wallet_id = None
        self._wallet_level = None
        self._wallet_status = None

    @property
    def bind_ar_no(self):
        return self._bind_ar_no

    @bind_ar_no.setter
    def bind_ar_no(self, value):
        self._bind_ar_no = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def freeze_type(self):
        return self._freeze_type

    @freeze_type.setter
    def freeze_type(self, value):
        self._freeze_type = value
    @property
    def has_bound(self):
        return self._has_bound

    @has_bound.setter
    def has_bound(self, value):
        self._has_bound = value
    @property
    def identify_token(self):
        return self._identify_token

    @identify_token.setter
    def identify_token(self, value):
        self._identify_token = value
    @property
    def quota_control_flag(self):
        return self._quota_control_flag

    @quota_control_flag.setter
    def quota_control_flag(self, value):
        self._quota_control_flag = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value
    @property
    def wallet_level(self):
        return self._wallet_level

    @wallet_level.setter
    def wallet_level(self, value):
        self._wallet_level = value
    @property
    def wallet_status(self):
        return self._wallet_status

    @wallet_status.setter
    def wallet_status(self, value):
        self._wallet_status = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyWalletBindQueryResponse, self).parse_response_content(response_content)
        if 'bind_ar_no' in response:
            self.bind_ar_no = response['bind_ar_no']
        if 'bind_time' in response:
            self.bind_time = response['bind_time']
        if 'freeze_type' in response:
            self.freeze_type = response['freeze_type']
        if 'has_bound' in response:
            self.has_bound = response['has_bound']
        if 'identify_token' in response:
            self.identify_token = response['identify_token']
        if 'quota_control_flag' in response:
            self.quota_control_flag = response['quota_control_flag']
        if 'role_type' in response:
            self.role_type = response['role_type']
        if 'wallet_id' in response:
            self.wallet_id = response['wallet_id']
        if 'wallet_level' in response:
            self.wallet_level = response['wallet_level']
        if 'wallet_status' in response:
            self.wallet_status = response['wallet_status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalletInfo(object):

    def __init__(self):
        self._user_wallet_id = None
        self._user_wallet_status = None
        self._wallet_template_id = None

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
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        if self.user_wallet_status:
            if hasattr(self.user_wallet_status, 'to_alipay_dict'):
                params['user_wallet_status'] = self.user_wallet_status.to_alipay_dict()
            else:
                params['user_wallet_status'] = self.user_wallet_status
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletInfo()
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        if 'user_wallet_status' in d:
            o.user_wallet_status = d['user_wallet_status']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        return o



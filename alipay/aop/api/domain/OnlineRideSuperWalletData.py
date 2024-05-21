#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OnlineRideSuperWalletData(object):

    def __init__(self):
        self._super_wallet_status = None

    @property
    def super_wallet_status(self):
        return self._super_wallet_status

    @super_wallet_status.setter
    def super_wallet_status(self, value):
        self._super_wallet_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.super_wallet_status:
            if hasattr(self.super_wallet_status, 'to_alipay_dict'):
                params['super_wallet_status'] = self.super_wallet_status.to_alipay_dict()
            else:
                params['super_wallet_status'] = self.super_wallet_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineRideSuperWalletData()
        if 'super_wallet_status' in d:
            o.super_wallet_status = d['super_wallet_status']
        return o



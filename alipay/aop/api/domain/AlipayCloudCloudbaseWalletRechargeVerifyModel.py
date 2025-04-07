#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseWalletRechargeVerifyModel(object):

    def __init__(self):
        self._recharge_app_id = None

    @property
    def recharge_app_id(self):
        return self._recharge_app_id

    @recharge_app_id.setter
    def recharge_app_id(self, value):
        self._recharge_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.recharge_app_id:
            if hasattr(self.recharge_app_id, 'to_alipay_dict'):
                params['recharge_app_id'] = self.recharge_app_id.to_alipay_dict()
            else:
                params['recharge_app_id'] = self.recharge_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseWalletRechargeVerifyModel()
        if 'recharge_app_id' in d:
            o.recharge_app_id = d['recharge_app_id']
        return o



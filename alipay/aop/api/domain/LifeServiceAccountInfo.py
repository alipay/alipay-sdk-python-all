#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceAccountInfo(object):

    def __init__(self):
        self._account_status = None
        self._settle_account_id = None
        self._shop_id = None

    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def settle_account_id(self):
        return self._settle_account_id

    @settle_account_id.setter
    def settle_account_id(self, value):
        self._settle_account_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_status:
            if hasattr(self.account_status, 'to_alipay_dict'):
                params['account_status'] = self.account_status.to_alipay_dict()
            else:
                params['account_status'] = self.account_status
        if self.settle_account_id:
            if hasattr(self.settle_account_id, 'to_alipay_dict'):
                params['settle_account_id'] = self.settle_account_id.to_alipay_dict()
            else:
                params['settle_account_id'] = self.settle_account_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceAccountInfo()
        if 'account_status' in d:
            o.account_status = d['account_status']
        if 'settle_account_id' in d:
            o.settle_account_id = d['settle_account_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o



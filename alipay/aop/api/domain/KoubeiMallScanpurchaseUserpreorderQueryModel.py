#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMallScanpurchaseUserpreorderQueryModel(object):

    def __init__(self):
        self._advance_order_id = None
        self._user_id = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_order_id:
            if hasattr(self.advance_order_id, 'to_alipay_dict'):
                params['advance_order_id'] = self.advance_order_id.to_alipay_dict()
            else:
                params['advance_order_id'] = self.advance_order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMallScanpurchaseUserpreorderQueryModel()
        if 'advance_order_id' in d:
            o.advance_order_id = d['advance_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



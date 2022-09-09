#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceZhimaSubmerchantSyncModel(object):

    def __init__(self):
        self._settle_alipay_login_id = None

    @property
    def settle_alipay_login_id(self):
        return self._settle_alipay_login_id

    @settle_alipay_login_id.setter
    def settle_alipay_login_id(self, value):
        self._settle_alipay_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_alipay_login_id:
            if hasattr(self.settle_alipay_login_id, 'to_alipay_dict'):
                params['settle_alipay_login_id'] = self.settle_alipay_login_id.to_alipay_dict()
            else:
                params['settle_alipay_login_id'] = self.settle_alipay_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceZhimaSubmerchantSyncModel()
        if 'settle_alipay_login_id' in d:
            o.settle_alipay_login_id = d['settle_alipay_login_id']
        return o



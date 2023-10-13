#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationDcsMerchantQueryModel(object):

    def __init__(self):
        self._brander_id = None

    @property
    def brander_id(self):
        return self._brander_id

    @brander_id.setter
    def brander_id(self, value):
        self._brander_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brander_id:
            if hasattr(self.brander_id, 'to_alipay_dict'):
                params['brander_id'] = self.brander_id.to_alipay_dict()
            else:
                params['brander_id'] = self.brander_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationDcsMerchantQueryModel()
        if 'brander_id' in d:
            o.brander_id = d['brander_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillBalanceQueryModel(object):

    def __init__(self):
        self._bill_user_id = None

    @property
    def bill_user_id(self):
        return self._bill_user_id

    @bill_user_id.setter
    def bill_user_id(self, value):
        self._bill_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_user_id:
            if hasattr(self.bill_user_id, 'to_alipay_dict'):
                params['bill_user_id'] = self.bill_user_id.to_alipay_dict()
            else:
                params['bill_user_id'] = self.bill_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillBalanceQueryModel()
        if 'bill_user_id' in d:
            o.bill_user_id = d['bill_user_id']
        return o



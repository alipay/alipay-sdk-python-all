#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankDailybillQueryModel(object):

    def __init__(self):
        self._bill_id = None

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_id:
            if hasattr(self.bill_id, 'to_alipay_dict'):
                params['bill_id'] = self.bill_id.to_alipay_dict()
            else:
                params['bill_id'] = self.bill_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankDailybillQueryModel()
        if 'bill_id' in d:
            o.bill_id = d['bill_id']
        return o



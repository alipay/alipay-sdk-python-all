#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillFreezebalanceQueryModel(object):

    def __init__(self):
        self._bill_user_id = None
        self._freeze_type = None

    @property
    def bill_user_id(self):
        return self._bill_user_id

    @bill_user_id.setter
    def bill_user_id(self, value):
        self._bill_user_id = value
    @property
    def freeze_type(self):
        return self._freeze_type

    @freeze_type.setter
    def freeze_type(self, value):
        self._freeze_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_user_id:
            if hasattr(self.bill_user_id, 'to_alipay_dict'):
                params['bill_user_id'] = self.bill_user_id.to_alipay_dict()
            else:
                params['bill_user_id'] = self.bill_user_id
        if self.freeze_type:
            if hasattr(self.freeze_type, 'to_alipay_dict'):
                params['freeze_type'] = self.freeze_type.to_alipay_dict()
            else:
                params['freeze_type'] = self.freeze_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillFreezebalanceQueryModel()
        if 'bill_user_id' in d:
            o.bill_user_id = d['bill_user_id']
        if 'freeze_type' in d:
            o.freeze_type = d['freeze_type']
        return o



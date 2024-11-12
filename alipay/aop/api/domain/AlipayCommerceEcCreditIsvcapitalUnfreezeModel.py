#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditIsvcapitalUnfreezeModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._out_freeze_no = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def out_freeze_no(self):
        return self._out_freeze_no

    @out_freeze_no.setter
    def out_freeze_no(self, value):
        self._out_freeze_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.out_freeze_no:
            if hasattr(self.out_freeze_no, 'to_alipay_dict'):
                params['out_freeze_no'] = self.out_freeze_no.to_alipay_dict()
            else:
                params['out_freeze_no'] = self.out_freeze_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditIsvcapitalUnfreezeModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'out_freeze_no' in d:
            o.out_freeze_no = d['out_freeze_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetPromotionApplyQueryModel(object):

    def __init__(self):
        self._apply_no = None
        self._apply_user_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_user_id(self):
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, value):
        self._apply_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_user_id:
            if hasattr(self.apply_user_id, 'to_alipay_dict'):
                params['apply_user_id'] = self.apply_user_id.to_alipay_dict()
            else:
                params['apply_user_id'] = self.apply_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetPromotionApplyQueryModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_user_id' in d:
            o.apply_user_id = d['apply_user_id']
        return o



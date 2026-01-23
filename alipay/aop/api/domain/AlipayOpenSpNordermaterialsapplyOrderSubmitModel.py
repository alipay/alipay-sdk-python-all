#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsapplyOrderSubmitModel(object):

    def __init__(self):
        self._apply_id = None
        self._combined_order_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def combined_order_no(self):
        return self._combined_order_no

    @combined_order_no.setter
    def combined_order_no(self, value):
        self._combined_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.combined_order_no:
            if hasattr(self.combined_order_no, 'to_alipay_dict'):
                params['combined_order_no'] = self.combined_order_no.to_alipay_dict()
            else:
                params['combined_order_no'] = self.combined_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyOrderSubmitModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'combined_order_no' in d:
            o.combined_order_no = d['combined_order_no']
        return o



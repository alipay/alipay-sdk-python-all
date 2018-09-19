#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceApplyTemplate(object):

    def __init__(self):
        self._apply_amount = None
        self._template_id = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceApplyTemplate()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o



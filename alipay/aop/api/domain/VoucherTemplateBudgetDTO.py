#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherTemplateBudgetDTO(object):

    def __init__(self):
        self._current_amount = None
        self._mode = None
        self._template_id = None
        self._total_amount = None

    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, value):
        self._current_amount = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_amount:
            if hasattr(self.current_amount, 'to_alipay_dict'):
                params['current_amount'] = self.current_amount.to_alipay_dict()
            else:
                params['current_amount'] = self.current_amount
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherTemplateBudgetDTO()
        if 'current_amount' in d:
            o.current_amount = d['current_amount']
        if 'mode' in d:
            o.mode = d['mode']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



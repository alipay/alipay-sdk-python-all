#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Credit import Credit


class XingheLendassistCarfinCreditchangeNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._credit_list = None
        self._out_apply_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def credit_list(self):
        return self._credit_list

    @credit_list.setter
    def credit_list(self, value):
        if isinstance(value, list):
            self._credit_list = list()
            for i in value:
                if isinstance(i, Credit):
                    self._credit_list.append(i)
                else:
                    self._credit_list.append(Credit.from_alipay_dict(i))
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.credit_list:
            if isinstance(self.credit_list, list):
                for i in range(0, len(self.credit_list)):
                    element = self.credit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_list, 'to_alipay_dict'):
                params['credit_list'] = self.credit_list.to_alipay_dict()
            else:
                params['credit_list'] = self.credit_list
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinCreditchangeNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'credit_list' in d:
            o.credit_list = d['credit_list']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        return o



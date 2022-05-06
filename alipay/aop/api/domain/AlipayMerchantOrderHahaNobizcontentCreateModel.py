#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantOrderHahaNobizcontentCreateModel(object):

    def __init__(self):
        self._delete = None
        self._input = None

    @property
    def delete(self):
        return self._delete

    @delete.setter
    def delete(self, value):
        self._delete = value
    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete:
            if hasattr(self.delete, 'to_alipay_dict'):
                params['delete'] = self.delete.to_alipay_dict()
            else:
                params['delete'] = self.delete
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderHahaNobizcontentCreateModel()
        if 'delete' in d:
            o.delete = d['delete']
        if 'input' in d:
            o.input = d['input']
        return o



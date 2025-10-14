#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyProdInfoModel(object):

    def __init__(self):
        self._prod_name = None
        self._prod_no = None

    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyProdInfoModel()
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        return o



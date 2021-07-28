#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneSellerDataQueryModel(object):

    def __init__(self):
        self._dx_name = None
        self._extra_data = None
        self._prod_no = None
        self._sp_no = None

    @property
    def dx_name(self):
        return self._dx_name

    @dx_name.setter
    def dx_name(self, value):
        self._dx_name = value
    @property
    def extra_data(self):
        return self._extra_data

    @extra_data.setter
    def extra_data(self, value):
        self._extra_data = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def sp_no(self):
        return self._sp_no

    @sp_no.setter
    def sp_no(self, value):
        self._sp_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.dx_name:
            if hasattr(self.dx_name, 'to_alipay_dict'):
                params['dx_name'] = self.dx_name.to_alipay_dict()
            else:
                params['dx_name'] = self.dx_name
        if self.extra_data:
            if hasattr(self.extra_data, 'to_alipay_dict'):
                params['extra_data'] = self.extra_data.to_alipay_dict()
            else:
                params['extra_data'] = self.extra_data
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        if self.sp_no:
            if hasattr(self.sp_no, 'to_alipay_dict'):
                params['sp_no'] = self.sp_no.to_alipay_dict()
            else:
                params['sp_no'] = self.sp_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneSellerDataQueryModel()
        if 'dx_name' in d:
            o.dx_name = d['dx_name']
        if 'extra_data' in d:
            o.extra_data = d['extra_data']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'sp_no' in d:
            o.sp_no = d['sp_no']
        return o



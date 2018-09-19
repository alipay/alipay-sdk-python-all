#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserUnicomMobileSyncModel(object):

    def __init__(self):
        self._gmt_status_change = None
        self._mobile = None
        self._operation_type = None
        self._out_biz_no = None
        self._product_name = None

    @property
    def gmt_status_change(self):
        return self._gmt_status_change

    @gmt_status_change.setter
    def gmt_status_change(self, value):
        self._gmt_status_change = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_status_change:
            if hasattr(self.gmt_status_change, 'to_alipay_dict'):
                params['gmt_status_change'] = self.gmt_status_change.to_alipay_dict()
            else:
                params['gmt_status_change'] = self.gmt_status_change
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserUnicomMobileSyncModel()
        if 'gmt_status_change' in d:
            o.gmt_status_change = d['gmt_status_change']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o



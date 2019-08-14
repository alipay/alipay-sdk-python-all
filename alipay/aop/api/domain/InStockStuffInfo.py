#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InStockStuffInfo(object):

    def __init__(self):
        self._actual_qty = None
        self._ext_info = None
        self._plan_qty = None
        self._sku_no = None

    @property
    def actual_qty(self):
        return self._actual_qty

    @actual_qty.setter
    def actual_qty(self, value):
        self._actual_qty = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def plan_qty(self):
        return self._plan_qty

    @plan_qty.setter
    def plan_qty(self, value):
        self._plan_qty = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_qty:
            if hasattr(self.actual_qty, 'to_alipay_dict'):
                params['actual_qty'] = self.actual_qty.to_alipay_dict()
            else:
                params['actual_qty'] = self.actual_qty
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.plan_qty:
            if hasattr(self.plan_qty, 'to_alipay_dict'):
                params['plan_qty'] = self.plan_qty.to_alipay_dict()
            else:
                params['plan_qty'] = self.plan_qty
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InStockStuffInfo()
        if 'actual_qty' in d:
            o.actual_qty = d['actual_qty']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'plan_qty' in d:
            o.plan_qty = d['plan_qty']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        return o



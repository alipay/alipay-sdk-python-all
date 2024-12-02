#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppPocketmoneyRedpacketBatchqueryModel(object):

    def __init__(self):
        self._red_pocket_out_nos = None
        self._vendor_name = None

    @property
    def red_pocket_out_nos(self):
        return self._red_pocket_out_nos

    @red_pocket_out_nos.setter
    def red_pocket_out_nos(self, value):
        if isinstance(value, list):
            self._red_pocket_out_nos = list()
            for i in value:
                self._red_pocket_out_nos.append(i)
    @property
    def vendor_name(self):
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, value):
        self._vendor_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.red_pocket_out_nos:
            if isinstance(self.red_pocket_out_nos, list):
                for i in range(0, len(self.red_pocket_out_nos)):
                    element = self.red_pocket_out_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.red_pocket_out_nos[i] = element.to_alipay_dict()
            if hasattr(self.red_pocket_out_nos, 'to_alipay_dict'):
                params['red_pocket_out_nos'] = self.red_pocket_out_nos.to_alipay_dict()
            else:
                params['red_pocket_out_nos'] = self.red_pocket_out_nos
        if self.vendor_name:
            if hasattr(self.vendor_name, 'to_alipay_dict'):
                params['vendor_name'] = self.vendor_name.to_alipay_dict()
            else:
                params['vendor_name'] = self.vendor_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppPocketmoneyRedpacketBatchqueryModel()
        if 'red_pocket_out_nos' in d:
            o.red_pocket_out_nos = d['red_pocket_out_nos']
        if 'vendor_name' in d:
            o.vendor_name = d['vendor_name']
        return o



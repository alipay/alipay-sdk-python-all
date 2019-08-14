#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotOrderPrintSyncModel(object):

    def __init__(self):
        self._biz_tid = None
        self._print_data = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def print_data(self):
        return self._print_data

    @print_data.setter
    def print_data(self, value):
        self._print_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.print_data:
            if hasattr(self.print_data, 'to_alipay_dict'):
                params['print_data'] = self.print_data.to_alipay_dict()
            else:
                params['print_data'] = self.print_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotOrderPrintSyncModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'print_data' in d:
            o.print_data = d['print_data']
        return o



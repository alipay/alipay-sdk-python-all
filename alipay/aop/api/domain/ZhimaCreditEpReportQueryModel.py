#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpReportQueryModel(object):

    def __init__(self):
        self._order_no = None
        self._report_type = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpReportQueryModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'report_type' in d:
            o.report_type = d['report_type']
        return o



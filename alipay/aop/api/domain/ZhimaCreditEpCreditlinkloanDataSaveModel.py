#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditlinkloanDataSaveModel(object):

    def __init__(self):
        self._collect_data_content = None
        self._collect_data_type = None
        self._merchant_biz_no = None
        self._order_type = None

    @property
    def collect_data_content(self):
        return self._collect_data_content

    @collect_data_content.setter
    def collect_data_content(self, value):
        self._collect_data_content = value
    @property
    def collect_data_type(self):
        return self._collect_data_type

    @collect_data_type.setter
    def collect_data_type(self, value):
        self._collect_data_type = value
    @property
    def merchant_biz_no(self):
        return self._merchant_biz_no

    @merchant_biz_no.setter
    def merchant_biz_no(self, value):
        self._merchant_biz_no = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.collect_data_content:
            if hasattr(self.collect_data_content, 'to_alipay_dict'):
                params['collect_data_content'] = self.collect_data_content.to_alipay_dict()
            else:
                params['collect_data_content'] = self.collect_data_content
        if self.collect_data_type:
            if hasattr(self.collect_data_type, 'to_alipay_dict'):
                params['collect_data_type'] = self.collect_data_type.to_alipay_dict()
            else:
                params['collect_data_type'] = self.collect_data_type
        if self.merchant_biz_no:
            if hasattr(self.merchant_biz_no, 'to_alipay_dict'):
                params['merchant_biz_no'] = self.merchant_biz_no.to_alipay_dict()
            else:
                params['merchant_biz_no'] = self.merchant_biz_no
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkloanDataSaveModel()
        if 'collect_data_content' in d:
            o.collect_data_content = d['collect_data_content']
        if 'collect_data_type' in d:
            o.collect_data_type = d['collect_data_type']
        if 'merchant_biz_no' in d:
            o.merchant_biz_no = d['merchant_biz_no']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceMerchantApplylistQueryModel(object):

    def __init__(self):
        self._apply_status = None
        self._biz_end_time = None
        self._biz_start_time = None
        self._brand_name = None
        self._merchant_id = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        if isinstance(value, list):
            self._apply_status = list()
            for i in value:
                self._apply_status.append(i)
    @property
    def biz_end_time(self):
        return self._biz_end_time

    @biz_end_time.setter
    def biz_end_time(self, value):
        self._biz_end_time = value
    @property
    def biz_start_time(self):
        return self._biz_start_time

    @biz_start_time.setter
    def biz_start_time(self, value):
        self._biz_start_time = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        if isinstance(value, list):
            self._merchant_id = list()
            for i in value:
                self._merchant_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_status:
            if isinstance(self.apply_status, list):
                for i in range(0, len(self.apply_status)):
                    element = self.apply_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_status[i] = element.to_alipay_dict()
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.biz_end_time:
            if hasattr(self.biz_end_time, 'to_alipay_dict'):
                params['biz_end_time'] = self.biz_end_time.to_alipay_dict()
            else:
                params['biz_end_time'] = self.biz_end_time
        if self.biz_start_time:
            if hasattr(self.biz_start_time, 'to_alipay_dict'):
                params['biz_start_time'] = self.biz_start_time.to_alipay_dict()
            else:
                params['biz_start_time'] = self.biz_start_time
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.merchant_id:
            if isinstance(self.merchant_id, list):
                for i in range(0, len(self.merchant_id)):
                    element = self.merchant_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_id[i] = element.to_alipay_dict()
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceMerchantApplylistQueryModel()
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'biz_end_time' in d:
            o.biz_end_time = d['biz_end_time']
        if 'biz_start_time' in d:
            o.biz_start_time = d['biz_start_time']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o



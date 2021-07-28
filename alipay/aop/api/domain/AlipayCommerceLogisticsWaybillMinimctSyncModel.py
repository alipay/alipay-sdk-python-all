#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParamExtInfo import ParamExtInfo


class AlipayCommerceLogisticsWaybillMinimctSyncModel(object):

    def __init__(self):
        self._logistics_code = None
        self._merchant_ext_info = None
        self._waybill_no = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def merchant_ext_info(self):
        return self._merchant_ext_info

    @merchant_ext_info.setter
    def merchant_ext_info(self, value):
        if isinstance(value, list):
            self._merchant_ext_info = list()
            for i in value:
                if isinstance(i, ParamExtInfo):
                    self._merchant_ext_info.append(i)
                else:
                    self._merchant_ext_info.append(ParamExtInfo.from_alipay_dict(i))
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.merchant_ext_info:
            if isinstance(self.merchant_ext_info, list):
                for i in range(0, len(self.merchant_ext_info)):
                    element = self.merchant_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.merchant_ext_info, 'to_alipay_dict'):
                params['merchant_ext_info'] = self.merchant_ext_info.to_alipay_dict()
            else:
                params['merchant_ext_info'] = self.merchant_ext_info
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsWaybillMinimctSyncModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'merchant_ext_info' in d:
            o.merchant_ext_info = d['merchant_ext_info']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o



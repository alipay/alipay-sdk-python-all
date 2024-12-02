#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillNotifyInfo import BillNotifyInfo


class AlipayEbppEbppBillNotifyUploadModel(object):

    def __init__(self):
        self._bill_notify_info = None
        self._province_code = None
        self._type = None

    @property
    def bill_notify_info(self):
        return self._bill_notify_info

    @bill_notify_info.setter
    def bill_notify_info(self, value):
        if isinstance(value, list):
            self._bill_notify_info = list()
            for i in value:
                if isinstance(i, BillNotifyInfo):
                    self._bill_notify_info.append(i)
                else:
                    self._bill_notify_info.append(BillNotifyInfo.from_alipay_dict(i))
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_notify_info:
            if isinstance(self.bill_notify_info, list):
                for i in range(0, len(self.bill_notify_info)):
                    element = self.bill_notify_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_notify_info[i] = element.to_alipay_dict()
            if hasattr(self.bill_notify_info, 'to_alipay_dict'):
                params['bill_notify_info'] = self.bill_notify_info.to_alipay_dict()
            else:
                params['bill_notify_info'] = self.bill_notify_info
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppBillNotifyUploadModel()
        if 'bill_notify_info' in d:
            o.bill_notify_info = d['bill_notify_info']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'type' in d:
            o.type = d['type']
        return o



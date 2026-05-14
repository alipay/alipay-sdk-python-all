#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResaleDeliveryVO(object):

    def __init__(self):
        self._logistics_bill_no = None
        self._logistics_platform = None

    @property
    def logistics_bill_no(self):
        return self._logistics_bill_no

    @logistics_bill_no.setter
    def logistics_bill_no(self, value):
        self._logistics_bill_no = value
    @property
    def logistics_platform(self):
        return self._logistics_platform

    @logistics_platform.setter
    def logistics_platform(self, value):
        self._logistics_platform = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_bill_no:
            if hasattr(self.logistics_bill_no, 'to_alipay_dict'):
                params['logistics_bill_no'] = self.logistics_bill_no.to_alipay_dict()
            else:
                params['logistics_bill_no'] = self.logistics_bill_no
        if self.logistics_platform:
            if hasattr(self.logistics_platform, 'to_alipay_dict'):
                params['logistics_platform'] = self.logistics_platform.to_alipay_dict()
            else:
                params['logistics_platform'] = self.logistics_platform
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResaleDeliveryVO()
        if 'logistics_bill_no' in d:
            o.logistics_bill_no = d['logistics_bill_no']
        if 'logistics_platform' in d:
            o.logistics_platform = d['logistics_platform']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopDeliveryInfo(object):

    def __init__(self):
        self._delivery_status = None
        self._logistics_code = None
        self._logistics_name = None
        self._materials_num = None
        self._waybill_no = None

    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def materials_num(self):
        return self._materials_num

    @materials_num.setter
    def materials_num(self, value):
        self._materials_num = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.materials_num:
            if hasattr(self.materials_num, 'to_alipay_dict'):
                params['materials_num'] = self.materials_num.to_alipay_dict()
            else:
                params['materials_num'] = self.materials_num
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
        o = ShopDeliveryInfo()
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'materials_num' in d:
            o.materials_num = d['materials_num']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o



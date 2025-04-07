#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopTaskDeliveryInfo(object):

    def __init__(self):
        self._delivery_status = None
        self._logistics_name = None
        self._way_bill_no = None

    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def way_bill_no(self):
        return self._way_bill_no

    @way_bill_no.setter
    def way_bill_no(self, value):
        self._way_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.way_bill_no:
            if hasattr(self.way_bill_no, 'to_alipay_dict'):
                params['way_bill_no'] = self.way_bill_no.to_alipay_dict()
            else:
                params['way_bill_no'] = self.way_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopTaskDeliveryInfo()
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'way_bill_no' in d:
            o.way_bill_no = d['way_bill_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceTechnicianDeleteModel(object):

    def __init__(self):
        self._out_technician_id = None
        self._shop_id = None
        self._technician_id = None

    @property
    def out_technician_id(self):
        return self._out_technician_id

    @out_technician_id.setter
    def out_technician_id(self, value):
        self._out_technician_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_technician_id:
            if hasattr(self.out_technician_id, 'to_alipay_dict'):
                params['out_technician_id'] = self.out_technician_id.to_alipay_dict()
            else:
                params['out_technician_id'] = self.out_technician_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.technician_id:
            if hasattr(self.technician_id, 'to_alipay_dict'):
                params['technician_id'] = self.technician_id.to_alipay_dict()
            else:
                params['technician_id'] = self.technician_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceTechnicianDeleteModel()
        if 'out_technician_id' in d:
            o.out_technician_id = d['out_technician_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'technician_id' in d:
            o.technician_id = d['technician_id']
        return o



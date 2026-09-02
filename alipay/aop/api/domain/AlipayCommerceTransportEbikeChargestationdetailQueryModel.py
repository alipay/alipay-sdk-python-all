#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEbikeChargestationdetailQueryModel(object):

    def __init__(self):
        self._brand_code = None
        self._device_no = None
        self._partner_code = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def partner_code(self):
        return self._partner_code

    @partner_code.setter
    def partner_code(self, value):
        self._partner_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.partner_code:
            if hasattr(self.partner_code, 'to_alipay_dict'):
                params['partner_code'] = self.partner_code.to_alipay_dict()
            else:
                params['partner_code'] = self.partner_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEbikeChargestationdetailQueryModel()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'partner_code' in d:
            o.partner_code = d['partner_code']
        return o



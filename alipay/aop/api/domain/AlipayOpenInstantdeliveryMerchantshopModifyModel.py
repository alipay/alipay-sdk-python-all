#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInstantdeliveryMerchantshopModifyModel(object):

    def __init__(self):
        self._contact_name = None
        self._logistics_codes = None
        self._out_biz_no = None
        self._phone = None
        self._shop_no = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def logistics_codes(self):
        return self._logistics_codes

    @logistics_codes.setter
    def logistics_codes(self, value):
        if isinstance(value, list):
            self._logistics_codes = list()
            for i in value:
                self._logistics_codes.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.logistics_codes:
            if isinstance(self.logistics_codes, list):
                for i in range(0, len(self.logistics_codes)):
                    element = self.logistics_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_codes[i] = element.to_alipay_dict()
            if hasattr(self.logistics_codes, 'to_alipay_dict'):
                params['logistics_codes'] = self.logistics_codes.to_alipay_dict()
            else:
                params['logistics_codes'] = self.logistics_codes
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryMerchantshopModifyModel()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'logistics_codes' in d:
            o.logistics_codes = d['logistics_codes']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        return o



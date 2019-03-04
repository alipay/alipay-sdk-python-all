#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallConsumeVoucher(object):

    def __init__(self):
        self._brand_name = None
        self._source_camp = None
        self._voucher_type = None
        self._worth_value = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def source_camp(self):
        return self._source_camp

    @source_camp.setter
    def source_camp(self, value):
        self._source_camp = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def worth_value(self):
        return self._worth_value

    @worth_value.setter
    def worth_value(self, value):
        self._worth_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.source_camp:
            if hasattr(self.source_camp, 'to_alipay_dict'):
                params['source_camp'] = self.source_camp.to_alipay_dict()
            else:
                params['source_camp'] = self.source_camp
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.worth_value:
            if hasattr(self.worth_value, 'to_alipay_dict'):
                params['worth_value'] = self.worth_value.to_alipay_dict()
            else:
                params['worth_value'] = self.worth_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallConsumeVoucher()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'source_camp' in d:
            o.source_camp = d['source_camp']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'worth_value' in d:
            o.worth_value = d['worth_value']
        return o



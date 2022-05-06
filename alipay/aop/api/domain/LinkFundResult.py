#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChargeRateDTO import ChargeRateDTO


class LinkFundResult(object):

    def __init__(self):
        self._fund_code = None
        self._fund_name = None
        self._product_id = None
        self._rate_list = None

    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value
    @property
    def fund_name(self):
        return self._fund_name

    @fund_name.setter
    def fund_name(self, value):
        self._fund_name = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def rate_list(self):
        return self._rate_list

    @rate_list.setter
    def rate_list(self, value):
        if isinstance(value, ChargeRateDTO):
            self._rate_list = value
        else:
            self._rate_list = ChargeRateDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fund_code:
            if hasattr(self.fund_code, 'to_alipay_dict'):
                params['fund_code'] = self.fund_code.to_alipay_dict()
            else:
                params['fund_code'] = self.fund_code
        if self.fund_name:
            if hasattr(self.fund_name, 'to_alipay_dict'):
                params['fund_name'] = self.fund_name.to_alipay_dict()
            else:
                params['fund_name'] = self.fund_name
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.rate_list:
            if hasattr(self.rate_list, 'to_alipay_dict'):
                params['rate_list'] = self.rate_list.to_alipay_dict()
            else:
                params['rate_list'] = self.rate_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkFundResult()
        if 'fund_code' in d:
            o.fund_code = d['fund_code']
        if 'fund_name' in d:
            o.fund_name = d['fund_name']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'rate_list' in d:
            o.rate_list = d['rate_list']
        return o



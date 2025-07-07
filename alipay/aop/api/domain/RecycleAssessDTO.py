#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleMerchantInfo import RecycleMerchantInfo
from alipay.aop.api.domain.RecyclePriceInfo import RecyclePriceInfo


class RecycleAssessDTO(object):

    def __init__(self):
        self._estimate_bill_id = None
        self._estimate_result_id = None
        self._merchant_info = None
        self._price_info_list = None
        self._price_type = None

    @property
    def estimate_bill_id(self):
        return self._estimate_bill_id

    @estimate_bill_id.setter
    def estimate_bill_id(self, value):
        self._estimate_bill_id = value
    @property
    def estimate_result_id(self):
        return self._estimate_result_id

    @estimate_result_id.setter
    def estimate_result_id(self, value):
        self._estimate_result_id = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, RecycleMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = RecycleMerchantInfo.from_alipay_dict(value)
    @property
    def price_info_list(self):
        return self._price_info_list

    @price_info_list.setter
    def price_info_list(self, value):
        if isinstance(value, list):
            self._price_info_list = list()
            for i in value:
                if isinstance(i, RecyclePriceInfo):
                    self._price_info_list.append(i)
                else:
                    self._price_info_list.append(RecyclePriceInfo.from_alipay_dict(i))
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimate_bill_id:
            if hasattr(self.estimate_bill_id, 'to_alipay_dict'):
                params['estimate_bill_id'] = self.estimate_bill_id.to_alipay_dict()
            else:
                params['estimate_bill_id'] = self.estimate_bill_id
        if self.estimate_result_id:
            if hasattr(self.estimate_result_id, 'to_alipay_dict'):
                params['estimate_result_id'] = self.estimate_result_id.to_alipay_dict()
            else:
                params['estimate_result_id'] = self.estimate_result_id
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.price_info_list:
            if isinstance(self.price_info_list, list):
                for i in range(0, len(self.price_info_list)):
                    element = self.price_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_info_list[i] = element.to_alipay_dict()
            if hasattr(self.price_info_list, 'to_alipay_dict'):
                params['price_info_list'] = self.price_info_list.to_alipay_dict()
            else:
                params['price_info_list'] = self.price_info_list
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAssessDTO()
        if 'estimate_bill_id' in d:
            o.estimate_bill_id = d['estimate_bill_id']
        if 'estimate_result_id' in d:
            o.estimate_result_id = d['estimate_result_id']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'price_info_list' in d:
            o.price_info_list = d['price_info_list']
        if 'price_type' in d:
            o.price_type = d['price_type']
        return o



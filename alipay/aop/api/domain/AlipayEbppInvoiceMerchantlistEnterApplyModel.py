#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantBaseEnterOpenModel import MerchantBaseEnterOpenModel
from alipay.aop.api.domain.SubMerchantCommonEnterOpenModel import SubMerchantCommonEnterOpenModel
from alipay.aop.api.domain.SubMerchantEnterOpenModel import SubMerchantEnterOpenModel


class AlipayEbppInvoiceMerchantlistEnterApplyModel(object):

    def __init__(self):
        self._merchant_base = None
        self._sub_merchant_common_info = None
        self._sub_merchant_list = None

    @property
    def merchant_base(self):
        return self._merchant_base

    @merchant_base.setter
    def merchant_base(self, value):
        if isinstance(value, MerchantBaseEnterOpenModel):
            self._merchant_base = value
        else:
            self._merchant_base = MerchantBaseEnterOpenModel.from_alipay_dict(value)
    @property
    def sub_merchant_common_info(self):
        return self._sub_merchant_common_info

    @sub_merchant_common_info.setter
    def sub_merchant_common_info(self, value):
        if isinstance(value, SubMerchantCommonEnterOpenModel):
            self._sub_merchant_common_info = value
        else:
            self._sub_merchant_common_info = SubMerchantCommonEnterOpenModel.from_alipay_dict(value)
    @property
    def sub_merchant_list(self):
        return self._sub_merchant_list

    @sub_merchant_list.setter
    def sub_merchant_list(self, value):
        if isinstance(value, list):
            self._sub_merchant_list = list()
            for i in value:
                if isinstance(i, SubMerchantEnterOpenModel):
                    self._sub_merchant_list.append(i)
                else:
                    self._sub_merchant_list.append(SubMerchantEnterOpenModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_base:
            if hasattr(self.merchant_base, 'to_alipay_dict'):
                params['merchant_base'] = self.merchant_base.to_alipay_dict()
            else:
                params['merchant_base'] = self.merchant_base
        if self.sub_merchant_common_info:
            if hasattr(self.sub_merchant_common_info, 'to_alipay_dict'):
                params['sub_merchant_common_info'] = self.sub_merchant_common_info.to_alipay_dict()
            else:
                params['sub_merchant_common_info'] = self.sub_merchant_common_info
        if self.sub_merchant_list:
            if isinstance(self.sub_merchant_list, list):
                for i in range(0, len(self.sub_merchant_list)):
                    element = self.sub_merchant_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_merchant_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_merchant_list, 'to_alipay_dict'):
                params['sub_merchant_list'] = self.sub_merchant_list.to_alipay_dict()
            else:
                params['sub_merchant_list'] = self.sub_merchant_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceMerchantlistEnterApplyModel()
        if 'merchant_base' in d:
            o.merchant_base = d['merchant_base']
        if 'sub_merchant_common_info' in d:
            o.sub_merchant_common_info = d['sub_merchant_common_info']
        if 'sub_merchant_list' in d:
            o.sub_merchant_list = d['sub_merchant_list']
        return o



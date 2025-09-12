#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantBriefInfo import MerchantBriefInfo


class AlipayMerchantNpromoIndirectQueryModel(object):

    def __init__(self):
        self._merchant_brief_list = None

    @property
    def merchant_brief_list(self):
        return self._merchant_brief_list

    @merchant_brief_list.setter
    def merchant_brief_list(self, value):
        if isinstance(value, list):
            self._merchant_brief_list = list()
            for i in value:
                if isinstance(i, MerchantBriefInfo):
                    self._merchant_brief_list.append(i)
                else:
                    self._merchant_brief_list.append(MerchantBriefInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_brief_list:
            if isinstance(self.merchant_brief_list, list):
                for i in range(0, len(self.merchant_brief_list)):
                    element = self.merchant_brief_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_brief_list[i] = element.to_alipay_dict()
            if hasattr(self.merchant_brief_list, 'to_alipay_dict'):
                params['merchant_brief_list'] = self.merchant_brief_list.to_alipay_dict()
            else:
                params['merchant_brief_list'] = self.merchant_brief_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantNpromoIndirectQueryModel()
        if 'merchant_brief_list' in d:
            o.merchant_brief_list = d['merchant_brief_list']
        return o



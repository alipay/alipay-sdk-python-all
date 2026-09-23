#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineSmddMerchantJobinfoBatchqueryModel(object):

    def __init__(self):
        self._merchant_id_list = None

    @property
    def merchant_id_list(self):
        return self._merchant_id_list

    @merchant_id_list.setter
    def merchant_id_list(self, value):
        if isinstance(value, list):
            self._merchant_id_list = list()
            for i in value:
                self._merchant_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_id_list:
            if isinstance(self.merchant_id_list, list):
                for i in range(0, len(self.merchant_id_list)):
                    element = self.merchant_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_id_list[i] = element.to_alipay_dict()
            if hasattr(self.merchant_id_list, 'to_alipay_dict'):
                params['merchant_id_list'] = self.merchant_id_list.to_alipay_dict()
            else:
                params['merchant_id_list'] = self.merchant_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddMerchantJobinfoBatchqueryModel()
        if 'merchant_id_list' in d:
            o.merchant_id_list = d['merchant_id_list']
        return o



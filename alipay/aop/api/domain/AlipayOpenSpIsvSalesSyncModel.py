#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IsvMerchantSalesDetailRequest import IsvMerchantSalesDetailRequest


class AlipayOpenSpIsvSalesSyncModel(object):

    def __init__(self):
        self._merchant_sales_detail = None

    @property
    def merchant_sales_detail(self):
        return self._merchant_sales_detail

    @merchant_sales_detail.setter
    def merchant_sales_detail(self, value):
        if isinstance(value, list):
            self._merchant_sales_detail = list()
            for i in value:
                if isinstance(i, IsvMerchantSalesDetailRequest):
                    self._merchant_sales_detail.append(i)
                else:
                    self._merchant_sales_detail.append(IsvMerchantSalesDetailRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_sales_detail:
            if isinstance(self.merchant_sales_detail, list):
                for i in range(0, len(self.merchant_sales_detail)):
                    element = self.merchant_sales_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_sales_detail[i] = element.to_alipay_dict()
            if hasattr(self.merchant_sales_detail, 'to_alipay_dict'):
                params['merchant_sales_detail'] = self.merchant_sales_detail.to_alipay_dict()
            else:
                params['merchant_sales_detail'] = self.merchant_sales_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpIsvSalesSyncModel()
        if 'merchant_sales_detail' in d:
            o.merchant_sales_detail = d['merchant_sales_detail']
        return o



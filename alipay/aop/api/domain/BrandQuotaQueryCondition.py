#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO


class BrandQuotaQueryCondition(object):

    def __init__(self):
        self._is_query_seller_list = None
        self._seller_info = None

    @property
    def is_query_seller_list(self):
        return self._is_query_seller_list

    @is_query_seller_list.setter
    def is_query_seller_list(self, value):
        self._is_query_seller_list = value
    @property
    def seller_info(self):
        return self._seller_info

    @seller_info.setter
    def seller_info(self, value):
        if isinstance(value, CreditPayUserVO):
            self._seller_info = value
        else:
            self._seller_info = CreditPayUserVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.is_query_seller_list:
            if hasattr(self.is_query_seller_list, 'to_alipay_dict'):
                params['is_query_seller_list'] = self.is_query_seller_list.to_alipay_dict()
            else:
                params['is_query_seller_list'] = self.is_query_seller_list
        if self.seller_info:
            if hasattr(self.seller_info, 'to_alipay_dict'):
                params['seller_info'] = self.seller_info.to_alipay_dict()
            else:
                params['seller_info'] = self.seller_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandQuotaQueryCondition()
        if 'is_query_seller_list' in d:
            o.is_query_seller_list = d['is_query_seller_list']
        if 'seller_info' in d:
            o.seller_info = d['seller_info']
        return o



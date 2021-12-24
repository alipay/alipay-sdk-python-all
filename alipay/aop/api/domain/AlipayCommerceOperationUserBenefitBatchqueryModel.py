#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationUserBenefitBatchqueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._product_type_list = None
        self._user_id = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_type_list(self):
        return self._product_type_list

    @product_type_list.setter
    def product_type_list(self, value):
        if isinstance(value, list):
            self._product_type_list = list()
            for i in value:
                self._product_type_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_type_list:
            if isinstance(self.product_type_list, list):
                for i in range(0, len(self.product_type_list)):
                    element = self.product_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_type_list, 'to_alipay_dict'):
                params['product_type_list'] = self.product_type_list.to_alipay_dict()
            else:
                params['product_type_list'] = self.product_type_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationUserBenefitBatchqueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_type_list' in d:
            o.product_type_list = d['product_type_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



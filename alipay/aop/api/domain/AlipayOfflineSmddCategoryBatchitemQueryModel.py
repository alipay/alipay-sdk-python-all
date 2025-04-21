#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeExtBean import CodeExtBean


class AlipayOfflineSmddCategoryBatchitemQueryModel(object):

    def __init__(self):
        self._buyer_id = None
        self._category_id_list = None
        self._code_ext = None
        self._shop_id = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def category_id_list(self):
        return self._category_id_list

    @category_id_list.setter
    def category_id_list(self, value):
        if isinstance(value, list):
            self._category_id_list = list()
            for i in value:
                self._category_id_list.append(i)
    @property
    def code_ext(self):
        return self._code_ext

    @code_ext.setter
    def code_ext(self, value):
        if isinstance(value, CodeExtBean):
            self._code_ext = value
        else:
            self._code_ext = CodeExtBean.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.category_id_list:
            if isinstance(self.category_id_list, list):
                for i in range(0, len(self.category_id_list)):
                    element = self.category_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_id_list[i] = element.to_alipay_dict()
            if hasattr(self.category_id_list, 'to_alipay_dict'):
                params['category_id_list'] = self.category_id_list.to_alipay_dict()
            else:
                params['category_id_list'] = self.category_id_list
        if self.code_ext:
            if hasattr(self.code_ext, 'to_alipay_dict'):
                params['code_ext'] = self.code_ext.to_alipay_dict()
            else:
                params['code_ext'] = self.code_ext
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddCategoryBatchitemQueryModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'category_id_list' in d:
            o.category_id_list = d['category_id_list']
        if 'code_ext' in d:
            o.code_ext = d['code_ext']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o



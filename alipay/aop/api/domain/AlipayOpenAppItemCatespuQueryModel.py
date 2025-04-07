#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyAttributeQueryRequest import KeyAttributeQueryRequest


class AlipayOpenAppItemCatespuQueryModel(object):

    def __init__(self):
        self._category_id = None
        self._key_attrs = None
        self._page_num = None
        self._page_size = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def key_attrs(self):
        return self._key_attrs

    @key_attrs.setter
    def key_attrs(self, value):
        if isinstance(value, list):
            self._key_attrs = list()
            for i in value:
                if isinstance(i, KeyAttributeQueryRequest):
                    self._key_attrs.append(i)
                else:
                    self._key_attrs.append(KeyAttributeQueryRequest.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.key_attrs:
            if isinstance(self.key_attrs, list):
                for i in range(0, len(self.key_attrs)):
                    element = self.key_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_attrs[i] = element.to_alipay_dict()
            if hasattr(self.key_attrs, 'to_alipay_dict'):
                params['key_attrs'] = self.key_attrs.to_alipay_dict()
            else:
                params['key_attrs'] = self.key_attrs
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItemCatespuQueryModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'key_attrs' in d:
            o.key_attrs = d['key_attrs']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallAttrValue import MallAttrValue


class AlipayDigitalmgmtPunchoutGoodsattrQueryModel(object):

    def __init__(self):
        self._attr_value_list = None
        self._is_valid = None
        self._page_num = None
        self._page_size = None

    @property
    def attr_value_list(self):
        return self._attr_value_list

    @attr_value_list.setter
    def attr_value_list(self, value):
        if isinstance(value, list):
            self._attr_value_list = list()
            for i in value:
                if isinstance(i, MallAttrValue):
                    self._attr_value_list.append(i)
                else:
                    self._attr_value_list.append(MallAttrValue.from_alipay_dict(i))
    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
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
        if self.attr_value_list:
            if isinstance(self.attr_value_list, list):
                for i in range(0, len(self.attr_value_list)):
                    element = self.attr_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_value_list, 'to_alipay_dict'):
                params['attr_value_list'] = self.attr_value_list.to_alipay_dict()
            else:
                params['attr_value_list'] = self.attr_value_list
        if self.is_valid:
            if hasattr(self.is_valid, 'to_alipay_dict'):
                params['is_valid'] = self.is_valid.to_alipay_dict()
            else:
                params['is_valid'] = self.is_valid
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
        o = AlipayDigitalmgmtPunchoutGoodsattrQueryModel()
        if 'attr_value_list' in d:
            o.attr_value_list = d['attr_value_list']
        if 'is_valid' in d:
            o.is_valid = d['is_valid']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



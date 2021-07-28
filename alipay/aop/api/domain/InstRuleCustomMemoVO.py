#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemoElement import MemoElement


class InstRuleCustomMemoVO(object):

    def __init__(self):
        self._element_list = None
        self._split_str = None

    @property
    def element_list(self):
        return self._element_list

    @element_list.setter
    def element_list(self, value):
        if isinstance(value, list):
            self._element_list = list()
            for i in value:
                if isinstance(i, MemoElement):
                    self._element_list.append(i)
                else:
                    self._element_list.append(MemoElement.from_alipay_dict(i))
    @property
    def split_str(self):
        return self._split_str

    @split_str.setter
    def split_str(self, value):
        self._split_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.element_list:
            if isinstance(self.element_list, list):
                for i in range(0, len(self.element_list)):
                    element = self.element_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.element_list[i] = element.to_alipay_dict()
            if hasattr(self.element_list, 'to_alipay_dict'):
                params['element_list'] = self.element_list.to_alipay_dict()
            else:
                params['element_list'] = self.element_list
        if self.split_str:
            if hasattr(self.split_str, 'to_alipay_dict'):
                params['split_str'] = self.split_str.to_alipay_dict()
            else:
                params['split_str'] = self.split_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstRuleCustomMemoVO()
        if 'element_list' in d:
            o.element_list = d['element_list']
        if 'split_str' in d:
            o.split_str = d['split_str']
        return o



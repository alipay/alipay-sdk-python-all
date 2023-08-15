#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TextSource import TextSource
from alipay.aop.api.domain.TextSource import TextSource
from alipay.aop.api.domain.TextSource import TextSource


class TextGroup(object):

    def __init__(self):
        self._discount_text = None
        self._main_text_list = None
        self._sub_text_list = None

    @property
    def discount_text(self):
        return self._discount_text

    @discount_text.setter
    def discount_text(self, value):
        if isinstance(value, TextSource):
            self._discount_text = value
        else:
            self._discount_text = TextSource.from_alipay_dict(value)
    @property
    def main_text_list(self):
        return self._main_text_list

    @main_text_list.setter
    def main_text_list(self, value):
        if isinstance(value, list):
            self._main_text_list = list()
            for i in value:
                if isinstance(i, TextSource):
                    self._main_text_list.append(i)
                else:
                    self._main_text_list.append(TextSource.from_alipay_dict(i))
    @property
    def sub_text_list(self):
        return self._sub_text_list

    @sub_text_list.setter
    def sub_text_list(self, value):
        if isinstance(value, list):
            self._sub_text_list = list()
            for i in value:
                if isinstance(i, TextSource):
                    self._sub_text_list.append(i)
                else:
                    self._sub_text_list.append(TextSource.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.discount_text:
            if hasattr(self.discount_text, 'to_alipay_dict'):
                params['discount_text'] = self.discount_text.to_alipay_dict()
            else:
                params['discount_text'] = self.discount_text
        if self.main_text_list:
            if isinstance(self.main_text_list, list):
                for i in range(0, len(self.main_text_list)):
                    element = self.main_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.main_text_list[i] = element.to_alipay_dict()
            if hasattr(self.main_text_list, 'to_alipay_dict'):
                params['main_text_list'] = self.main_text_list.to_alipay_dict()
            else:
                params['main_text_list'] = self.main_text_list
        if self.sub_text_list:
            if isinstance(self.sub_text_list, list):
                for i in range(0, len(self.sub_text_list)):
                    element = self.sub_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_text_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_text_list, 'to_alipay_dict'):
                params['sub_text_list'] = self.sub_text_list.to_alipay_dict()
            else:
                params['sub_text_list'] = self.sub_text_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TextGroup()
        if 'discount_text' in d:
            o.discount_text = d['discount_text']
        if 'main_text_list' in d:
            o.main_text_list = d['main_text_list']
        if 'sub_text_list' in d:
            o.sub_text_list = d['sub_text_list']
        return o



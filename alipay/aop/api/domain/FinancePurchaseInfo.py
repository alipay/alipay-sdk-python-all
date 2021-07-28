#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceFileInfo import FinanceFileInfo


class FinancePurchaseInfo(object):

    def __init__(self):
        self._content = None
        self._file_list = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, FinanceFileInfo):
                    self._file_list.append(i)
                else:
                    self._file_list.append(FinanceFileInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinancePurchaseInfo()
        if 'content' in d:
            o.content = d['content']
        if 'file_list' in d:
            o.file_list = d['file_list']
        return o



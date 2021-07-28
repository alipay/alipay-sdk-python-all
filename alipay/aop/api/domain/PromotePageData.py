#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotePagePropertyInstance import PromotePagePropertyInstance


class PromotePageData(object):

    def __init__(self):
        self._biz_no = None
        self._property_list = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, PromotePagePropertyInstance):
                    self._property_list.append(i)
                else:
                    self._property_list.append(PromotePagePropertyInstance.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotePageData()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'property_list' in d:
            o.property_list = d['property_list']
        return o



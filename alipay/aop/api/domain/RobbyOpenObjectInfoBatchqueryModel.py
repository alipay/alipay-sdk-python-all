#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RobbyOpenObjectInfoBatchqueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_object_no_list = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_object_no_list(self):
        return self._biz_object_no_list

    @biz_object_no_list.setter
    def biz_object_no_list(self, value):
        if isinstance(value, list):
            self._biz_object_no_list = list()
            for i in value:
                self._biz_object_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_object_no_list:
            if isinstance(self.biz_object_no_list, list):
                for i in range(0, len(self.biz_object_no_list)):
                    element = self.biz_object_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_object_no_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_object_no_list, 'to_alipay_dict'):
                params['biz_object_no_list'] = self.biz_object_no_list.to_alipay_dict()
            else:
                params['biz_object_no_list'] = self.biz_object_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RobbyOpenObjectInfoBatchqueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_object_no_list' in d:
            o.biz_object_no_list = d['biz_object_no_list']
        return o



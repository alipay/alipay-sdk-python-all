#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RobbyOpenObjectInfoBatchqueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_object_no_list = None
        self._object_library_id = None

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
    @property
    def object_library_id(self):
        return self._object_library_id

    @object_library_id.setter
    def object_library_id(self, value):
        self._object_library_id = value


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
        if self.object_library_id:
            if hasattr(self.object_library_id, 'to_alipay_dict'):
                params['object_library_id'] = self.object_library_id.to_alipay_dict()
            else:
                params['object_library_id'] = self.object_library_id
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
        if 'object_library_id' in d:
            o.object_library_id = d['object_library_id']
        return o



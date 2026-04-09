#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizInfoMap(object):

    def __init__(self):
        self._biz_count = None
        self._biz_object_no = None
        self._object_library_id = None

    @property
    def biz_count(self):
        return self._biz_count

    @biz_count.setter
    def biz_count(self, value):
        self._biz_count = value
    @property
    def biz_object_no(self):
        return self._biz_object_no

    @biz_object_no.setter
    def biz_object_no(self, value):
        self._biz_object_no = value
    @property
    def object_library_id(self):
        return self._object_library_id

    @object_library_id.setter
    def object_library_id(self, value):
        self._object_library_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_count:
            if hasattr(self.biz_count, 'to_alipay_dict'):
                params['biz_count'] = self.biz_count.to_alipay_dict()
            else:
                params['biz_count'] = self.biz_count
        if self.biz_object_no:
            if hasattr(self.biz_object_no, 'to_alipay_dict'):
                params['biz_object_no'] = self.biz_object_no.to_alipay_dict()
            else:
                params['biz_object_no'] = self.biz_object_no
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
        o = BizInfoMap()
        if 'biz_count' in d:
            o.biz_count = d['biz_count']
        if 'biz_object_no' in d:
            o.biz_object_no = d['biz_object_no']
        if 'object_library_id' in d:
            o.object_library_id = d['object_library_id']
        return o



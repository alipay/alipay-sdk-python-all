#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RobbyOpenObjectInfoQueryModel(object):

    def __init__(self):
        self._biz_object_name = None
        self._biz_object_no = None
        self._object_library_id = None
        self._page_num = None
        self._page_size = None

    @property
    def biz_object_name(self):
        return self._biz_object_name

    @biz_object_name.setter
    def biz_object_name(self, value):
        self._biz_object_name = value
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
        if self.biz_object_name:
            if hasattr(self.biz_object_name, 'to_alipay_dict'):
                params['biz_object_name'] = self.biz_object_name.to_alipay_dict()
            else:
                params['biz_object_name'] = self.biz_object_name
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
        o = RobbyOpenObjectInfoQueryModel()
        if 'biz_object_name' in d:
            o.biz_object_name = d['biz_object_name']
        if 'biz_object_no' in d:
            o.biz_object_no = d['biz_object_no']
        if 'object_library_id' in d:
            o.object_library_id = d['object_library_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



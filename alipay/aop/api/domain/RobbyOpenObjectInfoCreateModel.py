#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObjectFieldInfo import ObjectFieldInfo


class RobbyOpenObjectInfoCreateModel(object):

    def __init__(self):
        self._biz_object_field_info = None
        self._biz_object_library_no = None
        self._biz_object_name = None
        self._biz_object_no = None

    @property
    def biz_object_field_info(self):
        return self._biz_object_field_info

    @biz_object_field_info.setter
    def biz_object_field_info(self, value):
        if isinstance(value, list):
            self._biz_object_field_info = list()
            for i in value:
                if isinstance(i, ObjectFieldInfo):
                    self._biz_object_field_info.append(i)
                else:
                    self._biz_object_field_info.append(ObjectFieldInfo.from_alipay_dict(i))
    @property
    def biz_object_library_no(self):
        return self._biz_object_library_no

    @biz_object_library_no.setter
    def biz_object_library_no(self, value):
        self._biz_object_library_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_object_field_info:
            if isinstance(self.biz_object_field_info, list):
                for i in range(0, len(self.biz_object_field_info)):
                    element = self.biz_object_field_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_object_field_info[i] = element.to_alipay_dict()
            if hasattr(self.biz_object_field_info, 'to_alipay_dict'):
                params['biz_object_field_info'] = self.biz_object_field_info.to_alipay_dict()
            else:
                params['biz_object_field_info'] = self.biz_object_field_info
        if self.biz_object_library_no:
            if hasattr(self.biz_object_library_no, 'to_alipay_dict'):
                params['biz_object_library_no'] = self.biz_object_library_no.to_alipay_dict()
            else:
                params['biz_object_library_no'] = self.biz_object_library_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RobbyOpenObjectInfoCreateModel()
        if 'biz_object_field_info' in d:
            o.biz_object_field_info = d['biz_object_field_info']
        if 'biz_object_library_no' in d:
            o.biz_object_library_no = d['biz_object_library_no']
        if 'biz_object_name' in d:
            o.biz_object_name = d['biz_object_name']
        if 'biz_object_no' in d:
            o.biz_object_no = d['biz_object_no']
        return o



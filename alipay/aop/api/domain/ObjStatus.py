#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObjStatus(object):

    def __init__(self):
        self._biz_object_no = None
        self._completed_info = None
        self._mapping = None
        self._sorting = None

    @property
    def biz_object_no(self):
        return self._biz_object_no

    @biz_object_no.setter
    def biz_object_no(self, value):
        self._biz_object_no = value
    @property
    def completed_info(self):
        return self._completed_info

    @completed_info.setter
    def completed_info(self, value):
        self._completed_info = value
    @property
    def mapping(self):
        return self._mapping

    @mapping.setter
    def mapping(self, value):
        self._mapping = value
    @property
    def sorting(self):
        return self._sorting

    @sorting.setter
    def sorting(self, value):
        self._sorting = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_object_no:
            if hasattr(self.biz_object_no, 'to_alipay_dict'):
                params['biz_object_no'] = self.biz_object_no.to_alipay_dict()
            else:
                params['biz_object_no'] = self.biz_object_no
        if self.completed_info:
            if hasattr(self.completed_info, 'to_alipay_dict'):
                params['completed_info'] = self.completed_info.to_alipay_dict()
            else:
                params['completed_info'] = self.completed_info
        if self.mapping:
            if hasattr(self.mapping, 'to_alipay_dict'):
                params['mapping'] = self.mapping.to_alipay_dict()
            else:
                params['mapping'] = self.mapping
        if self.sorting:
            if hasattr(self.sorting, 'to_alipay_dict'):
                params['sorting'] = self.sorting.to_alipay_dict()
            else:
                params['sorting'] = self.sorting
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjStatus()
        if 'biz_object_no' in d:
            o.biz_object_no = d['biz_object_no']
        if 'completed_info' in d:
            o.completed_info = d['completed_info']
        if 'mapping' in d:
            o.mapping = d['mapping']
        if 'sorting' in d:
            o.sorting = d['sorting']
        return o



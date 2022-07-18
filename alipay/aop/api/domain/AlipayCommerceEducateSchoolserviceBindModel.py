#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchoolserviceBindModel(object):

    def __init__(self):
        self._biz_type = None
        self._school_name = None
        self._service_ids = None
        self._source_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def service_ids(self):
        return self._service_ids

    @service_ids.setter
    def service_ids(self, value):
        if isinstance(value, list):
            self._service_ids = list()
            for i in value:
                self._service_ids.append(i)
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.service_ids:
            if isinstance(self.service_ids, list):
                for i in range(0, len(self.service_ids)):
                    element = self.service_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_ids[i] = element.to_alipay_dict()
            if hasattr(self.service_ids, 'to_alipay_dict'):
                params['service_ids'] = self.service_ids.to_alipay_dict()
            else:
                params['service_ids'] = self.service_ids
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchoolserviceBindModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'service_ids' in d:
            o.service_ids = d['service_ids']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o



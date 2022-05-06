#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeDataItem import ApeDataItem


class AlipayDigitalopUcdpApedataSyncModel(object):

    def __init__(self):
        self._data_list = None
        self._data_type = None
        self._project_id = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, ApeDataItem):
                    self._data_list.append(i)
                else:
                    self._data_list.append(ApeDataItem.from_alipay_dict(i))
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApedataSyncModel()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o



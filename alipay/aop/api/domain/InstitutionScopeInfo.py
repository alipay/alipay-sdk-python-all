#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstitutionScopeInfo(object):

    def __init__(self):
        self._adapter_type = None
        self._owner_id_list = None
        self._owner_type = None

    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def owner_id_list(self):
        return self._owner_id_list

    @owner_id_list.setter
    def owner_id_list(self, value):
        if isinstance(value, list):
            self._owner_id_list = list()
            for i in value:
                self._owner_id_list.append(i)
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adapter_type:
            if hasattr(self.adapter_type, 'to_alipay_dict'):
                params['adapter_type'] = self.adapter_type.to_alipay_dict()
            else:
                params['adapter_type'] = self.adapter_type
        if self.owner_id_list:
            if isinstance(self.owner_id_list, list):
                for i in range(0, len(self.owner_id_list)):
                    element = self.owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.owner_id_list, 'to_alipay_dict'):
                params['owner_id_list'] = self.owner_id_list.to_alipay_dict()
            else:
                params['owner_id_list'] = self.owner_id_list
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstitutionScopeInfo()
        if 'adapter_type' in d:
            o.adapter_type = d['adapter_type']
        if 'owner_id_list' in d:
            o.owner_id_list = d['owner_id_list']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        return o



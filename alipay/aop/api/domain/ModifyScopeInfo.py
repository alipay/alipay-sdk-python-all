#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ModifyScopeInfo(object):

    def __init__(self):
        self._adapter_type = None
        self._add_owner_id_list = None
        self._delete_owner_id_list = None
        self._owner_type = None

    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def add_owner_id_list(self):
        return self._add_owner_id_list

    @add_owner_id_list.setter
    def add_owner_id_list(self, value):
        if isinstance(value, list):
            self._add_owner_id_list = list()
            for i in value:
                self._add_owner_id_list.append(i)
    @property
    def delete_owner_id_list(self):
        return self._delete_owner_id_list

    @delete_owner_id_list.setter
    def delete_owner_id_list(self, value):
        if isinstance(value, list):
            self._delete_owner_id_list = list()
            for i in value:
                self._delete_owner_id_list.append(i)
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
        if self.add_owner_id_list:
            if isinstance(self.add_owner_id_list, list):
                for i in range(0, len(self.add_owner_id_list)):
                    element = self.add_owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.add_owner_id_list, 'to_alipay_dict'):
                params['add_owner_id_list'] = self.add_owner_id_list.to_alipay_dict()
            else:
                params['add_owner_id_list'] = self.add_owner_id_list
        if self.delete_owner_id_list:
            if isinstance(self.delete_owner_id_list, list):
                for i in range(0, len(self.delete_owner_id_list)):
                    element = self.delete_owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_owner_id_list, 'to_alipay_dict'):
                params['delete_owner_id_list'] = self.delete_owner_id_list.to_alipay_dict()
            else:
                params['delete_owner_id_list'] = self.delete_owner_id_list
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
        o = ModifyScopeInfo()
        if 'adapter_type' in d:
            o.adapter_type = d['adapter_type']
        if 'add_owner_id_list' in d:
            o.add_owner_id_list = d['add_owner_id_list']
        if 'delete_owner_id_list' in d:
            o.delete_owner_id_list = d['delete_owner_id_list']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        return o



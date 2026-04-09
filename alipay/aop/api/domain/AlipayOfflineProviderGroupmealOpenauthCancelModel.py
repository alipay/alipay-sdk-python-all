#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderGroupmealOpenauthCancelModel(object):

    def __init__(self):
        self._logic_group_id = None
        self._open_id_list = None
        self._uid_list = None

    @property
    def logic_group_id(self):
        return self._logic_group_id

    @logic_group_id.setter
    def logic_group_id(self, value):
        self._logic_group_id = value
    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                self._uid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.logic_group_id:
            if hasattr(self.logic_group_id, 'to_alipay_dict'):
                params['logic_group_id'] = self.logic_group_id.to_alipay_dict()
            else:
                params['logic_group_id'] = self.logic_group_id
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        if self.uid_list:
            if isinstance(self.uid_list, list):
                for i in range(0, len(self.uid_list)):
                    element = self.uid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid_list[i] = element.to_alipay_dict()
            if hasattr(self.uid_list, 'to_alipay_dict'):
                params['uid_list'] = self.uid_list.to_alipay_dict()
            else:
                params['uid_list'] = self.uid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderGroupmealOpenauthCancelModel()
        if 'logic_group_id' in d:
            o.logic_group_id = d['logic_group_id']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'uid_list' in d:
            o.uid_list = d['uid_list']
        return o



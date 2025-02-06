#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StandardInfo import StandardInfo
from alipay.aop.api.domain.ModifyStandardInfo import ModifyStandardInfo


class ModifyStandardDetailInfo(object):

    def __init__(self):
        self._add_standard_list = None
        self._delete_standard_id_list = None
        self._modify_standard_list = None

    @property
    def add_standard_list(self):
        return self._add_standard_list

    @add_standard_list.setter
    def add_standard_list(self, value):
        if isinstance(value, list):
            self._add_standard_list = list()
            for i in value:
                if isinstance(i, StandardInfo):
                    self._add_standard_list.append(i)
                else:
                    self._add_standard_list.append(StandardInfo.from_alipay_dict(i))
    @property
    def delete_standard_id_list(self):
        return self._delete_standard_id_list

    @delete_standard_id_list.setter
    def delete_standard_id_list(self, value):
        if isinstance(value, list):
            self._delete_standard_id_list = list()
            for i in value:
                self._delete_standard_id_list.append(i)
    @property
    def modify_standard_list(self):
        return self._modify_standard_list

    @modify_standard_list.setter
    def modify_standard_list(self, value):
        if isinstance(value, list):
            self._modify_standard_list = list()
            for i in value:
                if isinstance(i, ModifyStandardInfo):
                    self._modify_standard_list.append(i)
                else:
                    self._modify_standard_list.append(ModifyStandardInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.add_standard_list:
            if isinstance(self.add_standard_list, list):
                for i in range(0, len(self.add_standard_list)):
                    element = self.add_standard_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_standard_list[i] = element.to_alipay_dict()
            if hasattr(self.add_standard_list, 'to_alipay_dict'):
                params['add_standard_list'] = self.add_standard_list.to_alipay_dict()
            else:
                params['add_standard_list'] = self.add_standard_list
        if self.delete_standard_id_list:
            if isinstance(self.delete_standard_id_list, list):
                for i in range(0, len(self.delete_standard_id_list)):
                    element = self.delete_standard_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_standard_id_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_standard_id_list, 'to_alipay_dict'):
                params['delete_standard_id_list'] = self.delete_standard_id_list.to_alipay_dict()
            else:
                params['delete_standard_id_list'] = self.delete_standard_id_list
        if self.modify_standard_list:
            if isinstance(self.modify_standard_list, list):
                for i in range(0, len(self.modify_standard_list)):
                    element = self.modify_standard_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.modify_standard_list[i] = element.to_alipay_dict()
            if hasattr(self.modify_standard_list, 'to_alipay_dict'):
                params['modify_standard_list'] = self.modify_standard_list.to_alipay_dict()
            else:
                params['modify_standard_list'] = self.modify_standard_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModifyStandardDetailInfo()
        if 'add_standard_list' in d:
            o.add_standard_list = d['add_standard_list']
        if 'delete_standard_id_list' in d:
            o.delete_standard_id_list = d['delete_standard_id_list']
        if 'modify_standard_list' in d:
            o.modify_standard_list = d['modify_standard_list']
        return o



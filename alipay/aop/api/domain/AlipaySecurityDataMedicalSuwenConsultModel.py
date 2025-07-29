#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultItem import ConsultItem
from alipay.aop.api.domain.ConsultItem import ConsultItem


class AlipaySecurityDataMedicalSuwenConsultModel(object):

    def __init__(self):
        self._data_type = None
        self._scene_code = None
        self._search_list = None
        self._target_list = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def search_list(self):
        return self._search_list

    @search_list.setter
    def search_list(self, value):
        if isinstance(value, list):
            self._search_list = list()
            for i in value:
                if isinstance(i, ConsultItem):
                    self._search_list.append(i)
                else:
                    self._search_list.append(ConsultItem.from_alipay_dict(i))
    @property
    def target_list(self):
        return self._target_list

    @target_list.setter
    def target_list(self, value):
        if isinstance(value, list):
            self._target_list = list()
            for i in value:
                if isinstance(i, ConsultItem):
                    self._target_list.append(i)
                else:
                    self._target_list.append(ConsultItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.search_list:
            if isinstance(self.search_list, list):
                for i in range(0, len(self.search_list)):
                    element = self.search_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.search_list[i] = element.to_alipay_dict()
            if hasattr(self.search_list, 'to_alipay_dict'):
                params['search_list'] = self.search_list.to_alipay_dict()
            else:
                params['search_list'] = self.search_list
        if self.target_list:
            if isinstance(self.target_list, list):
                for i in range(0, len(self.target_list)):
                    element = self.target_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_list[i] = element.to_alipay_dict()
            if hasattr(self.target_list, 'to_alipay_dict'):
                params['target_list'] = self.target_list.to_alipay_dict()
            else:
                params['target_list'] = self.target_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataMedicalSuwenConsultModel()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'search_list' in d:
            o.search_list = d['search_list']
        if 'target_list' in d:
            o.target_list = d['target_list']
        return o



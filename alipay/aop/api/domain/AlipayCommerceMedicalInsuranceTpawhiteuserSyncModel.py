#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuredInfo import InsuredInfo


class AlipayCommerceMedicalInsuranceTpawhiteuserSyncModel(object):

    def __init__(self):
        self._data_encryption_type = None
        self._entity_id = None
        self._entity_type = None
        self._ext_info = None
        self._insured_list = None
        self._source = None

    @property
    def data_encryption_type(self):
        return self._data_encryption_type

    @data_encryption_type.setter
    def data_encryption_type(self, value):
        self._data_encryption_type = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def insured_list(self):
        return self._insured_list

    @insured_list.setter
    def insured_list(self, value):
        if isinstance(value, list):
            self._insured_list = list()
            for i in value:
                if isinstance(i, InsuredInfo):
                    self._insured_list.append(i)
                else:
                    self._insured_list.append(InsuredInfo.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_encryption_type:
            if hasattr(self.data_encryption_type, 'to_alipay_dict'):
                params['data_encryption_type'] = self.data_encryption_type.to_alipay_dict()
            else:
                params['data_encryption_type'] = self.data_encryption_type
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.insured_list:
            if isinstance(self.insured_list, list):
                for i in range(0, len(self.insured_list)):
                    element = self.insured_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insured_list[i] = element.to_alipay_dict()
            if hasattr(self.insured_list, 'to_alipay_dict'):
                params['insured_list'] = self.insured_list.to_alipay_dict()
            else:
                params['insured_list'] = self.insured_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpawhiteuserSyncModel()
        if 'data_encryption_type' in d:
            o.data_encryption_type = d['data_encryption_type']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'insured_list' in d:
            o.insured_list = d['insured_list']
        if 'source' in d:
            o.source = d['source']
        return o



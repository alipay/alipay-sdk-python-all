#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeviceModel import IotDeviceModel


class AlipayCommerceIotModellistCreateModel(object):

    def __init__(self):
        self._model_list = None
        self._protocol_supplier_id = None

    @property
    def model_list(self):
        return self._model_list

    @model_list.setter
    def model_list(self, value):
        if isinstance(value, list):
            self._model_list = list()
            for i in value:
                if isinstance(i, IotDeviceModel):
                    self._model_list.append(i)
                else:
                    self._model_list.append(IotDeviceModel.from_alipay_dict(i))
    @property
    def protocol_supplier_id(self):
        return self._protocol_supplier_id

    @protocol_supplier_id.setter
    def protocol_supplier_id(self, value):
        self._protocol_supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_list:
            if isinstance(self.model_list, list):
                for i in range(0, len(self.model_list)):
                    element = self.model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.model_list[i] = element.to_alipay_dict()
            if hasattr(self.model_list, 'to_alipay_dict'):
                params['model_list'] = self.model_list.to_alipay_dict()
            else:
                params['model_list'] = self.model_list
        if self.protocol_supplier_id:
            if hasattr(self.protocol_supplier_id, 'to_alipay_dict'):
                params['protocol_supplier_id'] = self.protocol_supplier_id.to_alipay_dict()
            else:
                params['protocol_supplier_id'] = self.protocol_supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotModellistCreateModel()
        if 'model_list' in d:
            o.model_list = d['model_list']
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        return o



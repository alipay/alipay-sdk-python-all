#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeDeviceAddModel(object):

    def __init__(self):
        self._device_id_list = None
        self._model_id = None
        self._product_id = None

    @property
    def device_id_list(self):
        return self._device_id_list

    @device_id_list.setter
    def device_id_list(self, value):
        if isinstance(value, list):
            self._device_id_list = list()
            for i in value:
                self._device_id_list.append(i)
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id_list:
            if isinstance(self.device_id_list, list):
                for i in range(0, len(self.device_id_list)):
                    element = self.device_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_id_list[i] = element.to_alipay_dict()
            if hasattr(self.device_id_list, 'to_alipay_dict'):
                params['device_id_list'] = self.device_id_list.to_alipay_dict()
            else:
                params['device_id_list'] = self.device_id_list
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeDeviceAddModel()
        if 'device_id_list' in d:
            o.device_id_list = d['device_id_list']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        return o



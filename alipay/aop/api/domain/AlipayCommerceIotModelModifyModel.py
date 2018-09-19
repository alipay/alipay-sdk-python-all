#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeviceModel import IotDeviceModel


class AlipayCommerceIotModelModifyModel(object):

    def __init__(self):
        self._model = None
        self._protocol_supplier_id = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, IotDeviceModel):
            self._model = value
        else:
            self._model = IotDeviceModel.from_alipay_dict(value)
    @property
    def protocol_supplier_id(self):
        return self._protocol_supplier_id

    @protocol_supplier_id.setter
    def protocol_supplier_id(self, value):
        self._protocol_supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
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
        o = AlipayCommerceIotModelModifyModel()
        if 'model' in d:
            o.model = d['model']
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        return o



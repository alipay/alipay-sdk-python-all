#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDeviceAuthorizationNotifyModel(object):

    def __init__(self):
        self._aq_user_id = None
        self._change_at = None
        self._device_category = None
        self._device_id = None
        self._device_model = None
        self._device_name = None
        self._imei = None
        self._operation_type = None

    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value
    @property
    def change_at(self):
        return self._change_at

    @change_at.setter
    def change_at(self, value):
        self._change_at = value
    @property
    def device_category(self):
        return self._device_category

    @device_category.setter
    def device_category(self, value):
        self._device_category = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_model(self):
        return self._device_model

    @device_model.setter
    def device_model(self, value):
        self._device_model = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_user_id:
            if hasattr(self.aq_user_id, 'to_alipay_dict'):
                params['aq_user_id'] = self.aq_user_id.to_alipay_dict()
            else:
                params['aq_user_id'] = self.aq_user_id
        if self.change_at:
            if hasattr(self.change_at, 'to_alipay_dict'):
                params['change_at'] = self.change_at.to_alipay_dict()
            else:
                params['change_at'] = self.change_at
        if self.device_category:
            if hasattr(self.device_category, 'to_alipay_dict'):
                params['device_category'] = self.device_category.to_alipay_dict()
            else:
                params['device_category'] = self.device_category
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_model:
            if hasattr(self.device_model, 'to_alipay_dict'):
                params['device_model'] = self.device_model.to_alipay_dict()
            else:
                params['device_model'] = self.device_model
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDeviceAuthorizationNotifyModel()
        if 'aq_user_id' in d:
            o.aq_user_id = d['aq_user_id']
        if 'change_at' in d:
            o.change_at = d['change_at']
        if 'device_category' in d:
            o.device_category = d['device_category']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_model' in d:
            o.device_model = d['device_model']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'imei' in d:
            o.imei = d['imei']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        return o



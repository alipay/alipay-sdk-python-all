#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitQueryComponents import BenefitQueryComponents
from alipay.aop.api.domain.BenefitDeviceInfo import BenefitDeviceInfo


class AlipayCommerceTransportVehownerbaseBenefitQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._components = None
        self._device_info = None
        self._open_id = None
        self._operation_param_identify = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, BenefitQueryComponents):
            self._components = value
        else:
            self._components = BenefitQueryComponents.from_alipay_dict(value)
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, BenefitDeviceInfo):
            self._device_info = value
        else:
            self._device_info = BenefitDeviceInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_param_identify(self):
        return self._operation_param_identify

    @operation_param_identify.setter
    def operation_param_identify(self, value):
        self._operation_param_identify = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.components:
            if hasattr(self.components, 'to_alipay_dict'):
                params['components'] = self.components.to_alipay_dict()
            else:
                params['components'] = self.components
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_param_identify:
            if hasattr(self.operation_param_identify, 'to_alipay_dict'):
                params['operation_param_identify'] = self.operation_param_identify.to_alipay_dict()
            else:
                params['operation_param_identify'] = self.operation_param_identify
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehownerbaseBenefitQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'components' in d:
            o.components = d['components']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_param_identify' in d:
            o.operation_param_identify = d['operation_param_identify']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



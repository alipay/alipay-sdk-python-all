#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurancePayExtendParams(object):

    def __init__(self):
        self._channel_code = None
        self._medical_card_id = None
        self._medical_card_inst_id = None
        self._sys_service_provider_id = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_card_inst_id(self):
        return self._medical_card_inst_id

    @medical_card_inst_id.setter
    def medical_card_inst_id(self, value):
        self._medical_card_inst_id = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.medical_card_inst_id:
            if hasattr(self.medical_card_inst_id, 'to_alipay_dict'):
                params['medical_card_inst_id'] = self.medical_card_inst_id.to_alipay_dict()
            else:
                params['medical_card_inst_id'] = self.medical_card_inst_id
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurancePayExtendParams()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'medical_card_inst_id' in d:
            o.medical_card_inst_id = d['medical_card_inst_id']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o



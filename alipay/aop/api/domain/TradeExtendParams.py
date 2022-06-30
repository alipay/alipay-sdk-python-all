#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeExtendParams(object):

    def __init__(self):
        self._chinfo = None
        self._insurance_subsidy_amount = None
        self._insurance_subsidy_mode = None
        self._insurance_subsidy_type = None
        self._medical_card_id = None
        self._medical_ins_card_id = None
        self._request_content = None
        self._scene = None
        self._sys_service_provider_id = None

    @property
    def chinfo(self):
        return self._chinfo

    @chinfo.setter
    def chinfo(self, value):
        self._chinfo = value
    @property
    def insurance_subsidy_amount(self):
        return self._insurance_subsidy_amount

    @insurance_subsidy_amount.setter
    def insurance_subsidy_amount(self, value):
        self._insurance_subsidy_amount = value
    @property
    def insurance_subsidy_mode(self):
        return self._insurance_subsidy_mode

    @insurance_subsidy_mode.setter
    def insurance_subsidy_mode(self, value):
        self._insurance_subsidy_mode = value
    @property
    def insurance_subsidy_type(self):
        return self._insurance_subsidy_type

    @insurance_subsidy_type.setter
    def insurance_subsidy_type(self, value):
        self._insurance_subsidy_type = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_ins_card_id(self):
        return self._medical_ins_card_id

    @medical_ins_card_id.setter
    def medical_ins_card_id(self, value):
        self._medical_ins_card_id = value
    @property
    def request_content(self):
        return self._request_content

    @request_content.setter
    def request_content(self, value):
        self._request_content = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chinfo:
            if hasattr(self.chinfo, 'to_alipay_dict'):
                params['chinfo'] = self.chinfo.to_alipay_dict()
            else:
                params['chinfo'] = self.chinfo
        if self.insurance_subsidy_amount:
            if hasattr(self.insurance_subsidy_amount, 'to_alipay_dict'):
                params['insurance_subsidy_amount'] = self.insurance_subsidy_amount.to_alipay_dict()
            else:
                params['insurance_subsidy_amount'] = self.insurance_subsidy_amount
        if self.insurance_subsidy_mode:
            if hasattr(self.insurance_subsidy_mode, 'to_alipay_dict'):
                params['insurance_subsidy_mode'] = self.insurance_subsidy_mode.to_alipay_dict()
            else:
                params['insurance_subsidy_mode'] = self.insurance_subsidy_mode
        if self.insurance_subsidy_type:
            if hasattr(self.insurance_subsidy_type, 'to_alipay_dict'):
                params['insurance_subsidy_type'] = self.insurance_subsidy_type.to_alipay_dict()
            else:
                params['insurance_subsidy_type'] = self.insurance_subsidy_type
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.medical_ins_card_id:
            if hasattr(self.medical_ins_card_id, 'to_alipay_dict'):
                params['medical_ins_card_id'] = self.medical_ins_card_id.to_alipay_dict()
            else:
                params['medical_ins_card_id'] = self.medical_ins_card_id
        if self.request_content:
            if hasattr(self.request_content, 'to_alipay_dict'):
                params['request_content'] = self.request_content.to_alipay_dict()
            else:
                params['request_content'] = self.request_content
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = TradeExtendParams()
        if 'chinfo' in d:
            o.chinfo = d['chinfo']
        if 'insurance_subsidy_amount' in d:
            o.insurance_subsidy_amount = d['insurance_subsidy_amount']
        if 'insurance_subsidy_mode' in d:
            o.insurance_subsidy_mode = d['insurance_subsidy_mode']
        if 'insurance_subsidy_type' in d:
            o.insurance_subsidy_type = d['insurance_subsidy_type']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'medical_ins_card_id' in d:
            o.medical_ins_card_id = d['medical_ins_card_id']
        if 'request_content' in d:
            o.request_content = d['request_content']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o



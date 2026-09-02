#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterRuleQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel = None
        self._doctor_id = None
        self._isv_code = None
        self._isv_hos_dept_no = None
        self._isv_hos_no = None
        self._isv_user_id = None
        self._open_id = None
        self._patient_prop = None
        self._platform_code = None
        self._rule_ext_info = None
        self._scene_code = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def isv_hos_dept_no(self):
        return self._isv_hos_dept_no

    @isv_hos_dept_no.setter
    def isv_hos_dept_no(self, value):
        self._isv_hos_dept_no = value
    @property
    def isv_hos_no(self):
        return self._isv_hos_no

    @isv_hos_no.setter
    def isv_hos_no(self, value):
        self._isv_hos_no = value
    @property
    def isv_user_id(self):
        return self._isv_user_id

    @isv_user_id.setter
    def isv_user_id(self, value):
        self._isv_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def patient_prop(self):
        return self._patient_prop

    @patient_prop.setter
    def patient_prop(self, value):
        self._patient_prop = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def rule_ext_info(self):
        return self._rule_ext_info

    @rule_ext_info.setter
    def rule_ext_info(self, value):
        self._rule_ext_info = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.isv_hos_dept_no:
            if hasattr(self.isv_hos_dept_no, 'to_alipay_dict'):
                params['isv_hos_dept_no'] = self.isv_hos_dept_no.to_alipay_dict()
            else:
                params['isv_hos_dept_no'] = self.isv_hos_dept_no
        if self.isv_hos_no:
            if hasattr(self.isv_hos_no, 'to_alipay_dict'):
                params['isv_hos_no'] = self.isv_hos_no.to_alipay_dict()
            else:
                params['isv_hos_no'] = self.isv_hos_no
        if self.isv_user_id:
            if hasattr(self.isv_user_id, 'to_alipay_dict'):
                params['isv_user_id'] = self.isv_user_id.to_alipay_dict()
            else:
                params['isv_user_id'] = self.isv_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.patient_prop:
            if hasattr(self.patient_prop, 'to_alipay_dict'):
                params['patient_prop'] = self.patient_prop.to_alipay_dict()
            else:
                params['patient_prop'] = self.patient_prop
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.rule_ext_info:
            if hasattr(self.rule_ext_info, 'to_alipay_dict'):
                params['rule_ext_info'] = self.rule_ext_info.to_alipay_dict()
            else:
                params['rule_ext_info'] = self.rule_ext_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterRuleQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'isv_hos_dept_no' in d:
            o.isv_hos_dept_no = d['isv_hos_dept_no']
        if 'isv_hos_no' in d:
            o.isv_hos_no = d['isv_hos_no']
        if 'isv_user_id' in d:
            o.isv_user_id = d['isv_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'patient_prop' in d:
            o.patient_prop = d['patient_prop']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'rule_ext_info' in d:
            o.rule_ext_info = d['rule_ext_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o



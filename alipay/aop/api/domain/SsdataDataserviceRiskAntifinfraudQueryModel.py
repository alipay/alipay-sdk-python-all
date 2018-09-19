#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAntifinfraudQueryModel(object):

    def __init__(self):
        self._apdid = None
        self._ip = None
        self._partner_id = None
        self._phone = None
        self._risk_code = None
        self._scene_code = None
        self._sys_version = None
        self._umid = None

    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sys_version(self):
        return self._sys_version

    @sys_version.setter
    def sys_version(self, value):
        self._sys_version = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid:
            if hasattr(self.apdid, 'to_alipay_dict'):
                params['apdid'] = self.apdid.to_alipay_dict()
            else:
                params['apdid'] = self.apdid
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sys_version:
            if hasattr(self.sys_version, 'to_alipay_dict'):
                params['sys_version'] = self.sys_version.to_alipay_dict()
            else:
                params['sys_version'] = self.sys_version
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = self.umid.to_alipay_dict()
            else:
                params['umid'] = self.umid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAntifinfraudQueryModel()
        if 'apdid' in d:
            o.apdid = d['apdid']
        if 'ip' in d:
            o.ip = d['ip']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sys_version' in d:
            o.sys_version = d['sys_version']
        if 'umid' in d:
            o.umid = d['umid']
        return o



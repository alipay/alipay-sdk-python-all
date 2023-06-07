#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskMiniprogramFarmingQueryModel(object):

    def __init__(self):
        self._bank_card_no = None
        self._business_code = None
        self._cert_no = None
        self._channel = None
        self._company_name = None
        self._env_id = None
        self._ip = None
        self._isv_pid = None
        self._mer_pid = None
        self._merchant_scene = None
        self._mobile_no = None
        self._open_id = None
        self._outlet_address = None
        self._risk_type = None
        self._role = None
        self._scene = None
        self._service = None
        self._store_mcc_desc = None
        self._store_name = None
        self._user_id = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def mer_pid(self):
        return self._mer_pid

    @mer_pid.setter
    def mer_pid(self, value):
        self._mer_pid = value
    @property
    def merchant_scene(self):
        return self._merchant_scene

    @merchant_scene.setter
    def merchant_scene(self, value):
        self._merchant_scene = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outlet_address(self):
        return self._outlet_address

    @outlet_address.setter
    def outlet_address(self, value):
        self._outlet_address = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value
    @property
    def store_mcc_desc(self):
        return self._store_mcc_desc

    @store_mcc_desc.setter
    def store_mcc_desc(self, value):
        self._store_mcc_desc = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.mer_pid:
            if hasattr(self.mer_pid, 'to_alipay_dict'):
                params['mer_pid'] = self.mer_pid.to_alipay_dict()
            else:
                params['mer_pid'] = self.mer_pid
        if self.merchant_scene:
            if hasattr(self.merchant_scene, 'to_alipay_dict'):
                params['merchant_scene'] = self.merchant_scene.to_alipay_dict()
            else:
                params['merchant_scene'] = self.merchant_scene
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outlet_address:
            if hasattr(self.outlet_address, 'to_alipay_dict'):
                params['outlet_address'] = self.outlet_address.to_alipay_dict()
            else:
                params['outlet_address'] = self.outlet_address
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.store_mcc_desc:
            if hasattr(self.store_mcc_desc, 'to_alipay_dict'):
                params['store_mcc_desc'] = self.store_mcc_desc.to_alipay_dict()
            else:
                params['store_mcc_desc'] = self.store_mcc_desc
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
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
        o = AlipaySecurityRiskMiniprogramFarmingQueryModel()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'channel' in d:
            o.channel = d['channel']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'ip' in d:
            o.ip = d['ip']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'mer_pid' in d:
            o.mer_pid = d['mer_pid']
        if 'merchant_scene' in d:
            o.merchant_scene = d['merchant_scene']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outlet_address' in d:
            o.outlet_address = d['outlet_address']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'role' in d:
            o.role = d['role']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service' in d:
            o.service = d['service']
        if 'store_mcc_desc' in d:
            o.store_mcc_desc = d['store_mcc_desc']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



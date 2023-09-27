#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudTraasRiskgoBaddebtQueryModel(object):

    def __init__(self):
        self._activity_info = None
        self._apdid = None
        self._business_code = None
        self._cert_no = None
        self._env_id = None
        self._industry = None
        self._ip = None
        self._isv_pid = None
        self._lbs = None
        self._mer_pid = None
        self._mobile_no = None
        self._open_id = None
        self._risk_type = None
        self._role = None
        self._scene = None
        self._service = None
        self._service_category = None
        self._total_amount = None
        self._total_quantity = None
        self._user_id = None
        self._user_name = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        self._activity_info = value
    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
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
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
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
    def lbs(self):
        return self._lbs

    @lbs.setter
    def lbs(self, value):
        self._lbs = value
    @property
    def mer_pid(self):
        return self._mer_pid

    @mer_pid.setter
    def mer_pid(self, value):
        self._mer_pid = value
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
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_info:
            if hasattr(self.activity_info, 'to_alipay_dict'):
                params['activity_info'] = self.activity_info.to_alipay_dict()
            else:
                params['activity_info'] = self.activity_info
        if self.apdid:
            if hasattr(self.apdid, 'to_alipay_dict'):
                params['apdid'] = self.apdid.to_alipay_dict()
            else:
                params['apdid'] = self.apdid
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
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
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
        if self.lbs:
            if hasattr(self.lbs, 'to_alipay_dict'):
                params['lbs'] = self.lbs.to_alipay_dict()
            else:
                params['lbs'] = self.lbs
        if self.mer_pid:
            if hasattr(self.mer_pid, 'to_alipay_dict'):
                params['mer_pid'] = self.mer_pid.to_alipay_dict()
            else:
                params['mer_pid'] = self.mer_pid
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
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_quantity:
            if hasattr(self.total_quantity, 'to_alipay_dict'):
                params['total_quantity'] = self.total_quantity.to_alipay_dict()
            else:
                params['total_quantity'] = self.total_quantity
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudTraasRiskgoBaddebtQueryModel()
        if 'activity_info' in d:
            o.activity_info = d['activity_info']
        if 'apdid' in d:
            o.apdid = d['apdid']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'industry' in d:
            o.industry = d['industry']
        if 'ip' in d:
            o.ip = d['ip']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'lbs' in d:
            o.lbs = d['lbs']
        if 'mer_pid' in d:
            o.mer_pid = d['mer_pid']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'role' in d:
            o.role = d['role']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service' in d:
            o.service = d['service']
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_quantity' in d:
            o.total_quantity = d['total_quantity']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



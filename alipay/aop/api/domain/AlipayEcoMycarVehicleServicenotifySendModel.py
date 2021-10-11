#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleToken import VehicleToken


class AlipayEcoMycarVehicleServicenotifySendModel(object):

    def __init__(self):
        self._merchant_status_code = None
        self._merchant_status_desc = None
        self._service_operate_timestamp = None
        self._service_status = None
        self._service_type = None
        self._system_timestamp = None
        self._user_id = None
        self._vehicle_open_id = None
        self._vehicle_token = None
        self._vi_id = None

    @property
    def merchant_status_code(self):
        return self._merchant_status_code

    @merchant_status_code.setter
    def merchant_status_code(self, value):
        self._merchant_status_code = value
    @property
    def merchant_status_desc(self):
        return self._merchant_status_desc

    @merchant_status_desc.setter
    def merchant_status_desc(self, value):
        self._merchant_status_desc = value
    @property
    def service_operate_timestamp(self):
        return self._service_operate_timestamp

    @service_operate_timestamp.setter
    def service_operate_timestamp(self, value):
        self._service_operate_timestamp = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def system_timestamp(self):
        return self._system_timestamp

    @system_timestamp.setter
    def system_timestamp(self, value):
        self._system_timestamp = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vehicle_open_id(self):
        return self._vehicle_open_id

    @vehicle_open_id.setter
    def vehicle_open_id(self, value):
        self._vehicle_open_id = value
    @property
    def vehicle_token(self):
        return self._vehicle_token

    @vehicle_token.setter
    def vehicle_token(self, value):
        if isinstance(value, VehicleToken):
            self._vehicle_token = value
        else:
            self._vehicle_token = VehicleToken.from_alipay_dict(value)
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_status_code:
            if hasattr(self.merchant_status_code, 'to_alipay_dict'):
                params['merchant_status_code'] = self.merchant_status_code.to_alipay_dict()
            else:
                params['merchant_status_code'] = self.merchant_status_code
        if self.merchant_status_desc:
            if hasattr(self.merchant_status_desc, 'to_alipay_dict'):
                params['merchant_status_desc'] = self.merchant_status_desc.to_alipay_dict()
            else:
                params['merchant_status_desc'] = self.merchant_status_desc
        if self.service_operate_timestamp:
            if hasattr(self.service_operate_timestamp, 'to_alipay_dict'):
                params['service_operate_timestamp'] = self.service_operate_timestamp.to_alipay_dict()
            else:
                params['service_operate_timestamp'] = self.service_operate_timestamp
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.system_timestamp:
            if hasattr(self.system_timestamp, 'to_alipay_dict'):
                params['system_timestamp'] = self.system_timestamp.to_alipay_dict()
            else:
                params['system_timestamp'] = self.system_timestamp
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vehicle_open_id:
            if hasattr(self.vehicle_open_id, 'to_alipay_dict'):
                params['vehicle_open_id'] = self.vehicle_open_id.to_alipay_dict()
            else:
                params['vehicle_open_id'] = self.vehicle_open_id
        if self.vehicle_token:
            if hasattr(self.vehicle_token, 'to_alipay_dict'):
                params['vehicle_token'] = self.vehicle_token.to_alipay_dict()
            else:
                params['vehicle_token'] = self.vehicle_token
        if self.vi_id:
            if hasattr(self.vi_id, 'to_alipay_dict'):
                params['vi_id'] = self.vi_id.to_alipay_dict()
            else:
                params['vi_id'] = self.vi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarVehicleServicenotifySendModel()
        if 'merchant_status_code' in d:
            o.merchant_status_code = d['merchant_status_code']
        if 'merchant_status_desc' in d:
            o.merchant_status_desc = d['merchant_status_desc']
        if 'service_operate_timestamp' in d:
            o.service_operate_timestamp = d['service_operate_timestamp']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'system_timestamp' in d:
            o.system_timestamp = d['system_timestamp']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_open_id' in d:
            o.vehicle_open_id = d['vehicle_open_id']
        if 'vehicle_token' in d:
            o.vehicle_token = d['vehicle_token']
        if 'vi_id' in d:
            o.vi_id = d['vi_id']
        return o



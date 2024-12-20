#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrivateChargingEquipment import PrivateChargingEquipment


class AlipayCommerceTransportChargerPrivatebindSyncModel(object):

    def __init__(self):
        self._bind_status = None
        self._equipment_info = None
        self._open_id = None
        self._operate_time = None
        self._operator_uid = None
        self._phone_num = None
        self._user_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def equipment_info(self):
        return self._equipment_info

    @equipment_info.setter
    def equipment_info(self, value):
        if isinstance(value, PrivateChargingEquipment):
            self._equipment_info = value
        else:
            self._equipment_info = PrivateChargingEquipment.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
        if self.equipment_info:
            if hasattr(self.equipment_info, 'to_alipay_dict'):
                params['equipment_info'] = self.equipment_info.to_alipay_dict()
            else:
                params['equipment_info'] = self.equipment_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.phone_num:
            if hasattr(self.phone_num, 'to_alipay_dict'):
                params['phone_num'] = self.phone_num.to_alipay_dict()
            else:
                params['phone_num'] = self.phone_num
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
        o = AlipayCommerceTransportChargerPrivatebindSyncModel()
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'equipment_info' in d:
            o.equipment_info = d['equipment_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrivateChargingSetting import PrivateChargingSetting


class AlipayCommerceTransportChargerPrivatemodeSyncModel(object):

    def __init__(self):
        self._equip_id = None
        self._open_id = None
        self._operator_uid = None
        self._setting = None
        self._sync_timestamp = None
        self._user_id = None

    @property
    def equip_id(self):
        return self._equip_id

    @equip_id.setter
    def equip_id(self, value):
        self._equip_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def setting(self):
        return self._setting

    @setting.setter
    def setting(self, value):
        if isinstance(value, PrivateChargingSetting):
            self._setting = value
        else:
            self._setting = PrivateChargingSetting.from_alipay_dict(value)
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.equip_id:
            if hasattr(self.equip_id, 'to_alipay_dict'):
                params['equip_id'] = self.equip_id.to_alipay_dict()
            else:
                params['equip_id'] = self.equip_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.setting:
            if hasattr(self.setting, 'to_alipay_dict'):
                params['setting'] = self.setting.to_alipay_dict()
            else:
                params['setting'] = self.setting
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
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
        o = AlipayCommerceTransportChargerPrivatemodeSyncModel()
        if 'equip_id' in d:
            o.equip_id = d['equip_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'setting' in d:
            o.setting = d['setting']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterVerifyQueryModel(object):

    def __init__(self):
        self._mac_address = None
        self._minutes_ago = None
        self._open_id = None
        self._phone_number = None
        self._project_id = None
        self._user_id = None

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value
    @property
    def minutes_ago(self):
        return self._minutes_ago

    @minutes_ago.setter
    def minutes_ago(self, value):
        self._minutes_ago = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mac_address:
            if hasattr(self.mac_address, 'to_alipay_dict'):
                params['mac_address'] = self.mac_address.to_alipay_dict()
            else:
                params['mac_address'] = self.mac_address
        if self.minutes_ago:
            if hasattr(self.minutes_ago, 'to_alipay_dict'):
                params['minutes_ago'] = self.minutes_ago.to_alipay_dict()
            else:
                params['minutes_ago'] = self.minutes_ago
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
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
        o = AlipayOfflineProviderNpassporterVerifyQueryModel()
        if 'mac_address' in d:
            o.mac_address = d['mac_address']
        if 'minutes_ago' in d:
            o.minutes_ago = d['minutes_ago']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



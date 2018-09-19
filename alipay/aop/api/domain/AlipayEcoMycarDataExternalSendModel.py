#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDataExternalSendModel(object):

    def __init__(self):
        self._external_system_name = None
        self._is_transfer_uid = None
        self._operate_type = None
        self._send_data = None

    @property
    def external_system_name(self):
        return self._external_system_name

    @external_system_name.setter
    def external_system_name(self, value):
        self._external_system_name = value
    @property
    def is_transfer_uid(self):
        return self._is_transfer_uid

    @is_transfer_uid.setter
    def is_transfer_uid(self, value):
        self._is_transfer_uid = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def send_data(self):
        return self._send_data

    @send_data.setter
    def send_data(self, value):
        self._send_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_system_name:
            if hasattr(self.external_system_name, 'to_alipay_dict'):
                params['external_system_name'] = self.external_system_name.to_alipay_dict()
            else:
                params['external_system_name'] = self.external_system_name
        if self.is_transfer_uid:
            if hasattr(self.is_transfer_uid, 'to_alipay_dict'):
                params['is_transfer_uid'] = self.is_transfer_uid.to_alipay_dict()
            else:
                params['is_transfer_uid'] = self.is_transfer_uid
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.send_data:
            if hasattr(self.send_data, 'to_alipay_dict'):
                params['send_data'] = self.send_data.to_alipay_dict()
            else:
                params['send_data'] = self.send_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDataExternalSendModel()
        if 'external_system_name' in d:
            o.external_system_name = d['external_system_name']
        if 'is_transfer_uid' in d:
            o.is_transfer_uid = d['is_transfer_uid']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'send_data' in d:
            o.send_data = d['send_data']
        return o



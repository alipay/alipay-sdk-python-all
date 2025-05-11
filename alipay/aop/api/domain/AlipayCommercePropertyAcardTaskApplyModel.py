#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GateDeviceInfo import GateDeviceInfo
from alipay.aop.api.domain.GateDeviceInfo import GateDeviceInfo


class AlipayCommercePropertyAcardTaskApplyModel(object):

    def __init__(self):
        self._action_type = None
        self._auth_devices = None
        self._card_no = None
        self._card_template_code = None
        self._forbid_devices = None
        self._open_id = None
        self._out_biz_id = None
        self._transparent_data = None
        self._user_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def auth_devices(self):
        return self._auth_devices

    @auth_devices.setter
    def auth_devices(self, value):
        if isinstance(value, list):
            self._auth_devices = list()
            for i in value:
                if isinstance(i, GateDeviceInfo):
                    self._auth_devices.append(i)
                else:
                    self._auth_devices.append(GateDeviceInfo.from_alipay_dict(i))
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_template_code(self):
        return self._card_template_code

    @card_template_code.setter
    def card_template_code(self, value):
        self._card_template_code = value
    @property
    def forbid_devices(self):
        return self._forbid_devices

    @forbid_devices.setter
    def forbid_devices(self, value):
        if isinstance(value, list):
            self._forbid_devices = list()
            for i in value:
                if isinstance(i, GateDeviceInfo):
                    self._forbid_devices.append(i)
                else:
                    self._forbid_devices.append(GateDeviceInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def transparent_data(self):
        return self._transparent_data

    @transparent_data.setter
    def transparent_data(self, value):
        self._transparent_data = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.auth_devices:
            if isinstance(self.auth_devices, list):
                for i in range(0, len(self.auth_devices)):
                    element = self.auth_devices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auth_devices[i] = element.to_alipay_dict()
            if hasattr(self.auth_devices, 'to_alipay_dict'):
                params['auth_devices'] = self.auth_devices.to_alipay_dict()
            else:
                params['auth_devices'] = self.auth_devices
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_template_code:
            if hasattr(self.card_template_code, 'to_alipay_dict'):
                params['card_template_code'] = self.card_template_code.to_alipay_dict()
            else:
                params['card_template_code'] = self.card_template_code
        if self.forbid_devices:
            if isinstance(self.forbid_devices, list):
                for i in range(0, len(self.forbid_devices)):
                    element = self.forbid_devices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.forbid_devices[i] = element.to_alipay_dict()
            if hasattr(self.forbid_devices, 'to_alipay_dict'):
                params['forbid_devices'] = self.forbid_devices.to_alipay_dict()
            else:
                params['forbid_devices'] = self.forbid_devices
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.transparent_data:
            if hasattr(self.transparent_data, 'to_alipay_dict'):
                params['transparent_data'] = self.transparent_data.to_alipay_dict()
            else:
                params['transparent_data'] = self.transparent_data
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
        o = AlipayCommercePropertyAcardTaskApplyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'auth_devices' in d:
            o.auth_devices = d['auth_devices']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_template_code' in d:
            o.card_template_code = d['card_template_code']
        if 'forbid_devices' in d:
            o.forbid_devices = d['forbid_devices']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'transparent_data' in d:
            o.transparent_data = d['transparent_data']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionDevicegrayModifyModel(object):

    def __init__(self):
        self._action_type = None
        self._app_origin = None
        self._bundle_id = None
        self._device_no_list = None
        self._gray_code = None
        self._name = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def device_no_list(self):
        return self._device_no_list

    @device_no_list.setter
    def device_no_list(self, value):
        if isinstance(value, list):
            self._device_no_list = list()
            for i in value:
                self._device_no_list.append(i)
    @property
    def gray_code(self):
        return self._gray_code

    @gray_code.setter
    def gray_code(self, value):
        self._gray_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.device_no_list:
            if isinstance(self.device_no_list, list):
                for i in range(0, len(self.device_no_list)):
                    element = self.device_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_no_list[i] = element.to_alipay_dict()
            if hasattr(self.device_no_list, 'to_alipay_dict'):
                params['device_no_list'] = self.device_no_list.to_alipay_dict()
            else:
                params['device_no_list'] = self.device_no_list
        if self.gray_code:
            if hasattr(self.gray_code, 'to_alipay_dict'):
                params['gray_code'] = self.gray_code.to_alipay_dict()
            else:
                params['gray_code'] = self.gray_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionDevicegrayModifyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'device_no_list' in d:
            o.device_no_list = d['device_no_list']
        if 'gray_code' in d:
            o.gray_code = d['gray_code']
        if 'name' in d:
            o.name = d['name']
        return o



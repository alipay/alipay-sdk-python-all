#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDeviceInfo(object):

    def __init__(self):
        self._apd_id = None
        self._app_version = None
        self._mobile_brand = None
        self._mobile_model = None
        self._os_type = None
        self._screen_height = None
        self._screen_width = None
        self._system_type = None
        self._system_version = None
        self._utd_id = None

    @property
    def apd_id(self):
        return self._apd_id

    @apd_id.setter
    def apd_id(self, value):
        self._apd_id = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def mobile_brand(self):
        return self._mobile_brand

    @mobile_brand.setter
    def mobile_brand(self, value):
        self._mobile_brand = value
    @property
    def mobile_model(self):
        return self._mobile_model

    @mobile_model.setter
    def mobile_model(self, value):
        self._mobile_model = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def screen_height(self):
        return self._screen_height

    @screen_height.setter
    def screen_height(self, value):
        self._screen_height = value
    @property
    def screen_width(self):
        return self._screen_width

    @screen_width.setter
    def screen_width(self, value):
        self._screen_width = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value
    @property
    def system_version(self):
        return self._system_version

    @system_version.setter
    def system_version(self, value):
        self._system_version = value
    @property
    def utd_id(self):
        return self._utd_id

    @utd_id.setter
    def utd_id(self, value):
        self._utd_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apd_id:
            if hasattr(self.apd_id, 'to_alipay_dict'):
                params['apd_id'] = self.apd_id.to_alipay_dict()
            else:
                params['apd_id'] = self.apd_id
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.mobile_brand:
            if hasattr(self.mobile_brand, 'to_alipay_dict'):
                params['mobile_brand'] = self.mobile_brand.to_alipay_dict()
            else:
                params['mobile_brand'] = self.mobile_brand
        if self.mobile_model:
            if hasattr(self.mobile_model, 'to_alipay_dict'):
                params['mobile_model'] = self.mobile_model.to_alipay_dict()
            else:
                params['mobile_model'] = self.mobile_model
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.screen_height:
            if hasattr(self.screen_height, 'to_alipay_dict'):
                params['screen_height'] = self.screen_height.to_alipay_dict()
            else:
                params['screen_height'] = self.screen_height
        if self.screen_width:
            if hasattr(self.screen_width, 'to_alipay_dict'):
                params['screen_width'] = self.screen_width.to_alipay_dict()
            else:
                params['screen_width'] = self.screen_width
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        if self.system_version:
            if hasattr(self.system_version, 'to_alipay_dict'):
                params['system_version'] = self.system_version.to_alipay_dict()
            else:
                params['system_version'] = self.system_version
        if self.utd_id:
            if hasattr(self.utd_id, 'to_alipay_dict'):
                params['utd_id'] = self.utd_id.to_alipay_dict()
            else:
                params['utd_id'] = self.utd_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDeviceInfo()
        if 'apd_id' in d:
            o.apd_id = d['apd_id']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'mobile_brand' in d:
            o.mobile_brand = d['mobile_brand']
        if 'mobile_model' in d:
            o.mobile_model = d['mobile_model']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'screen_height' in d:
            o.screen_height = d['screen_height']
        if 'screen_width' in d:
            o.screen_width = d['screen_width']
        if 'system_type' in d:
            o.system_type = d['system_type']
        if 'system_version' in d:
            o.system_version = d['system_version']
        if 'utd_id' in d:
            o.utd_id = d['utd_id']
        return o



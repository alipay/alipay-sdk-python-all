#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpdateContentExtAttribute(object):

    def __init__(self):
        self._accessory_sn = None
        self._isv_access_token = None
        self._isv_device_version_tag = None

    @property
    def accessory_sn(self):
        return self._accessory_sn

    @accessory_sn.setter
    def accessory_sn(self, value):
        self._accessory_sn = value
    @property
    def isv_access_token(self):
        return self._isv_access_token

    @isv_access_token.setter
    def isv_access_token(self, value):
        self._isv_access_token = value
    @property
    def isv_device_version_tag(self):
        return self._isv_device_version_tag

    @isv_device_version_tag.setter
    def isv_device_version_tag(self, value):
        self._isv_device_version_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.accessory_sn:
            if hasattr(self.accessory_sn, 'to_alipay_dict'):
                params['accessory_sn'] = self.accessory_sn.to_alipay_dict()
            else:
                params['accessory_sn'] = self.accessory_sn
        if self.isv_access_token:
            if hasattr(self.isv_access_token, 'to_alipay_dict'):
                params['isv_access_token'] = self.isv_access_token.to_alipay_dict()
            else:
                params['isv_access_token'] = self.isv_access_token
        if self.isv_device_version_tag:
            if hasattr(self.isv_device_version_tag, 'to_alipay_dict'):
                params['isv_device_version_tag'] = self.isv_device_version_tag.to_alipay_dict()
            else:
                params['isv_device_version_tag'] = self.isv_device_version_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpdateContentExtAttribute()
        if 'accessory_sn' in d:
            o.accessory_sn = d['accessory_sn']
        if 'isv_access_token' in d:
            o.isv_access_token = d['isv_access_token']
        if 'isv_device_version_tag' in d:
            o.isv_device_version_tag = d['isv_device_version_tag']
        return o



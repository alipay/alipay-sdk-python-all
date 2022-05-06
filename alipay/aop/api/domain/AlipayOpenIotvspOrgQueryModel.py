#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotvspOrgQueryModel(object):

    def __init__(self):
        self._entity_id = None
        self._entity_type = None
        self._isv_app_id = None
        self._isv_name = None
        self._isv_pid = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotvspOrgQueryModel()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        return o



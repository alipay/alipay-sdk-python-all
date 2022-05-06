#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotvspOrguserCreateModel(object):

    def __init__(self):
        self._authorize_app_id = None
        self._authorize_app_pid = None
        self._biz_id = None
        self._cert_no = None
        self._cert_type = None
        self._entity_id = None
        self._entity_type = None
        self._ext = None
        self._isv_name = None
        self._name = None

    @property
    def authorize_app_id(self):
        return self._authorize_app_id

    @authorize_app_id.setter
    def authorize_app_id(self, value):
        self._authorize_app_id = value
    @property
    def authorize_app_pid(self):
        return self._authorize_app_pid

    @authorize_app_pid.setter
    def authorize_app_pid(self, value):
        self._authorize_app_pid = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
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
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorize_app_id:
            if hasattr(self.authorize_app_id, 'to_alipay_dict'):
                params['authorize_app_id'] = self.authorize_app_id.to_alipay_dict()
            else:
                params['authorize_app_id'] = self.authorize_app_id
        if self.authorize_app_pid:
            if hasattr(self.authorize_app_pid, 'to_alipay_dict'):
                params['authorize_app_pid'] = self.authorize_app_pid.to_alipay_dict()
            else:
                params['authorize_app_pid'] = self.authorize_app_pid
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
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
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
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
        o = AlipayOpenIotvspOrguserCreateModel()
        if 'authorize_app_id' in d:
            o.authorize_app_id = d['authorize_app_id']
        if 'authorize_app_pid' in d:
            o.authorize_app_pid = d['authorize_app_pid']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'ext' in d:
            o.ext = d['ext']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'name' in d:
            o.name = d['name']
        return o



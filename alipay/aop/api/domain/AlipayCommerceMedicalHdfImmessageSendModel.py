#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfImmessageSendModel(object):

    def __init__(self):
        self._action = None
        self._app_msg_id = None
        self._app_version = None
        self._business = None
        self._business_type = None
        self._device = None
        self._device_key = None
        self._from_connection_id = None
        self._from_source_id = None
        self._from_source_type = None
        self._method_action = None
        self._msg_body = None
        self._msg_id = None
        self._need_xss = None
        self._sdk_version = None
        self._to_detail_id_list = None
        self._to_source_id = None
        self._to_source_type = None
        self._type = None
        self._user_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def app_msg_id(self):
        return self._app_msg_id

    @app_msg_id.setter
    def app_msg_id(self, value):
        self._app_msg_id = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        self._device = value
    @property
    def device_key(self):
        return self._device_key

    @device_key.setter
    def device_key(self, value):
        self._device_key = value
    @property
    def from_connection_id(self):
        return self._from_connection_id

    @from_connection_id.setter
    def from_connection_id(self, value):
        self._from_connection_id = value
    @property
    def from_source_id(self):
        return self._from_source_id

    @from_source_id.setter
    def from_source_id(self, value):
        self._from_source_id = value
    @property
    def from_source_type(self):
        return self._from_source_type

    @from_source_type.setter
    def from_source_type(self, value):
        self._from_source_type = value
    @property
    def method_action(self):
        return self._method_action

    @method_action.setter
    def method_action(self, value):
        self._method_action = value
    @property
    def msg_body(self):
        return self._msg_body

    @msg_body.setter
    def msg_body(self, value):
        self._msg_body = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def need_xss(self):
        return self._need_xss

    @need_xss.setter
    def need_xss(self, value):
        self._need_xss = value
    @property
    def sdk_version(self):
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, value):
        self._sdk_version = value
    @property
    def to_detail_id_list(self):
        return self._to_detail_id_list

    @to_detail_id_list.setter
    def to_detail_id_list(self, value):
        self._to_detail_id_list = value
    @property
    def to_source_id(self):
        return self._to_source_id

    @to_source_id.setter
    def to_source_id(self, value):
        self._to_source_id = value
    @property
    def to_source_type(self):
        return self._to_source_type

    @to_source_type.setter
    def to_source_type(self, value):
        self._to_source_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.app_msg_id:
            if hasattr(self.app_msg_id, 'to_alipay_dict'):
                params['app_msg_id'] = self.app_msg_id.to_alipay_dict()
            else:
                params['app_msg_id'] = self.app_msg_id
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.business:
            if hasattr(self.business, 'to_alipay_dict'):
                params['business'] = self.business.to_alipay_dict()
            else:
                params['business'] = self.business
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.device:
            if hasattr(self.device, 'to_alipay_dict'):
                params['device'] = self.device.to_alipay_dict()
            else:
                params['device'] = self.device
        if self.device_key:
            if hasattr(self.device_key, 'to_alipay_dict'):
                params['device_key'] = self.device_key.to_alipay_dict()
            else:
                params['device_key'] = self.device_key
        if self.from_connection_id:
            if hasattr(self.from_connection_id, 'to_alipay_dict'):
                params['from_connection_id'] = self.from_connection_id.to_alipay_dict()
            else:
                params['from_connection_id'] = self.from_connection_id
        if self.from_source_id:
            if hasattr(self.from_source_id, 'to_alipay_dict'):
                params['from_source_id'] = self.from_source_id.to_alipay_dict()
            else:
                params['from_source_id'] = self.from_source_id
        if self.from_source_type:
            if hasattr(self.from_source_type, 'to_alipay_dict'):
                params['from_source_type'] = self.from_source_type.to_alipay_dict()
            else:
                params['from_source_type'] = self.from_source_type
        if self.method_action:
            if hasattr(self.method_action, 'to_alipay_dict'):
                params['method_action'] = self.method_action.to_alipay_dict()
            else:
                params['method_action'] = self.method_action
        if self.msg_body:
            if hasattr(self.msg_body, 'to_alipay_dict'):
                params['msg_body'] = self.msg_body.to_alipay_dict()
            else:
                params['msg_body'] = self.msg_body
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.need_xss:
            if hasattr(self.need_xss, 'to_alipay_dict'):
                params['need_xss'] = self.need_xss.to_alipay_dict()
            else:
                params['need_xss'] = self.need_xss
        if self.sdk_version:
            if hasattr(self.sdk_version, 'to_alipay_dict'):
                params['sdk_version'] = self.sdk_version.to_alipay_dict()
            else:
                params['sdk_version'] = self.sdk_version
        if self.to_detail_id_list:
            if hasattr(self.to_detail_id_list, 'to_alipay_dict'):
                params['to_detail_id_list'] = self.to_detail_id_list.to_alipay_dict()
            else:
                params['to_detail_id_list'] = self.to_detail_id_list
        if self.to_source_id:
            if hasattr(self.to_source_id, 'to_alipay_dict'):
                params['to_source_id'] = self.to_source_id.to_alipay_dict()
            else:
                params['to_source_id'] = self.to_source_id
        if self.to_source_type:
            if hasattr(self.to_source_type, 'to_alipay_dict'):
                params['to_source_type'] = self.to_source_type.to_alipay_dict()
            else:
                params['to_source_type'] = self.to_source_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayCommerceMedicalHdfImmessageSendModel()
        if 'action' in d:
            o.action = d['action']
        if 'app_msg_id' in d:
            o.app_msg_id = d['app_msg_id']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'business' in d:
            o.business = d['business']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'device' in d:
            o.device = d['device']
        if 'device_key' in d:
            o.device_key = d['device_key']
        if 'from_connection_id' in d:
            o.from_connection_id = d['from_connection_id']
        if 'from_source_id' in d:
            o.from_source_id = d['from_source_id']
        if 'from_source_type' in d:
            o.from_source_type = d['from_source_type']
        if 'method_action' in d:
            o.method_action = d['method_action']
        if 'msg_body' in d:
            o.msg_body = d['msg_body']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'need_xss' in d:
            o.need_xss = d['need_xss']
        if 'sdk_version' in d:
            o.sdk_version = d['sdk_version']
        if 'to_detail_id_list' in d:
            o.to_detail_id_list = d['to_detail_id_list']
        if 'to_source_id' in d:
            o.to_source_id = d['to_source_id']
        if 'to_source_type' in d:
            o.to_source_type = d['to_source_type']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



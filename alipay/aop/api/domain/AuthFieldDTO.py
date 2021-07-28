#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthFieldDTO(object):

    def __init__(self):
        self._api_name = None
        self._field_name = None
        self._package_code = None
        self._reason = None
        self._status = None
        self._user_app_id = None

    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_app_id(self):
        return self._user_app_id

    @user_app_id.setter
    def user_app_id(self, value):
        self._user_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_app_id:
            if hasattr(self.user_app_id, 'to_alipay_dict'):
                params['user_app_id'] = self.user_app_id.to_alipay_dict()
            else:
                params['user_app_id'] = self.user_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthFieldDTO()
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'package_code' in d:
            o.package_code = d['package_code']
        if 'reason' in d:
            o.reason = d['reason']
        if 'status' in d:
            o.status = d['status']
        if 'user_app_id' in d:
            o.user_app_id = d['user_app_id']
        return o



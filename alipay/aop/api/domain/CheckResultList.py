#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckResultList(object):

    def __init__(self):
        self._action_id = None
        self._action_name = None
        self._error_code = None
        self._error_desc = None
        self._ext_infos = None
        self._success = None

    @property
    def action_id(self):
        return self._action_id

    @action_id.setter
    def action_id(self, value):
        self._action_id = value
    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_id:
            if hasattr(self.action_id, 'to_alipay_dict'):
                params['action_id'] = self.action_id.to_alipay_dict()
            else:
                params['action_id'] = self.action_id
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckResultList()
        if 'action_id' in d:
            o.action_id = d['action_id']
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'success' in d:
            o.success = d['success']
        return o



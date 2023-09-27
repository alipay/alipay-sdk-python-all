#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenApplicationInfoDTO(object):

    def __init__(self):
        self._app_name = None
        self._application_id = None
        self._application_type = None
        self._pid = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def application_type(self):
        return self._application_type

    @application_type.setter
    def application_type(self, value):
        self._application_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.application_type:
            if hasattr(self.application_type, 'to_alipay_dict'):
                params['application_type'] = self.application_type.to_alipay_dict()
            else:
                params['application_type'] = self.application_type
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenApplicationInfoDTO()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'application_type' in d:
            o.application_type = d['application_type']
        if 'pid' in d:
            o.pid = d['pid']
        return o



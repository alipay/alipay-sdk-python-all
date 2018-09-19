#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoCreateModel(object):

    def __init__(self):
        self._app_alias_name = None
        self._app_desc = None
        self._app_logo = None
        self._app_slogan = None
        self._client_type = None
        self._pid = None

    @property
    def app_alias_name(self):
        return self._app_alias_name

    @app_alias_name.setter
    def app_alias_name(self, value):
        self._app_alias_name = value
    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        self._client_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_alias_name:
            if hasattr(self.app_alias_name, 'to_alipay_dict'):
                params['app_alias_name'] = self.app_alias_name.to_alipay_dict()
            else:
                params['app_alias_name'] = self.app_alias_name
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.client_type:
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
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
        o = AlipayOpenMiniInnerbaseinfoCreateModel()
        if 'app_alias_name' in d:
            o.app_alias_name = d['app_alias_name']
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'pid' in d:
            o.pid = d['pid']
        return o



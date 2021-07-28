#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BindedMiniAppInfo(object):

    def __init__(self):
        self._dev_name = None
        self._mini_app_id = None
        self._mini_app_logo = None
        self._mini_app_name = None
        self._mini_app_slogan = None
        self._online = None
        self._support_ampe = None

    @property
    def dev_name(self):
        return self._dev_name

    @dev_name.setter
    def dev_name(self, value):
        self._dev_name = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_logo(self):
        return self._mini_app_logo

    @mini_app_logo.setter
    def mini_app_logo(self, value):
        self._mini_app_logo = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def mini_app_slogan(self):
        return self._mini_app_slogan

    @mini_app_slogan.setter
    def mini_app_slogan(self, value):
        self._mini_app_slogan = value
    @property
    def online(self):
        return self._online

    @online.setter
    def online(self, value):
        self._online = value
    @property
    def support_ampe(self):
        return self._support_ampe

    @support_ampe.setter
    def support_ampe(self, value):
        self._support_ampe = value


    def to_alipay_dict(self):
        params = dict()
        if self.dev_name:
            if hasattr(self.dev_name, 'to_alipay_dict'):
                params['dev_name'] = self.dev_name.to_alipay_dict()
            else:
                params['dev_name'] = self.dev_name
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_logo:
            if hasattr(self.mini_app_logo, 'to_alipay_dict'):
                params['mini_app_logo'] = self.mini_app_logo.to_alipay_dict()
            else:
                params['mini_app_logo'] = self.mini_app_logo
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.mini_app_slogan:
            if hasattr(self.mini_app_slogan, 'to_alipay_dict'):
                params['mini_app_slogan'] = self.mini_app_slogan.to_alipay_dict()
            else:
                params['mini_app_slogan'] = self.mini_app_slogan
        if self.online:
            if hasattr(self.online, 'to_alipay_dict'):
                params['online'] = self.online.to_alipay_dict()
            else:
                params['online'] = self.online
        if self.support_ampe:
            if hasattr(self.support_ampe, 'to_alipay_dict'):
                params['support_ampe'] = self.support_ampe.to_alipay_dict()
            else:
                params['support_ampe'] = self.support_ampe
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BindedMiniAppInfo()
        if 'dev_name' in d:
            o.dev_name = d['dev_name']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_logo' in d:
            o.mini_app_logo = d['mini_app_logo']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'mini_app_slogan' in d:
            o.mini_app_slogan = d['mini_app_slogan']
        if 'online' in d:
            o.online = d['online']
        if 'support_ampe' in d:
            o.support_ampe = d['support_ampe']
        return o



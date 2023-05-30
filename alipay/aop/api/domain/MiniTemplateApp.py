#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniTemplateVersionInfo import MiniTemplateVersionInfo


class MiniTemplateApp(object):

    def __init__(self):
        self._app_name = None
        self._date_create = None
        self._logo_url = None
        self._mini_app_id = None
        self._version_list = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def date_create(self):
        return self._date_create

    @date_create.setter
    def date_create(self, value):
        self._date_create = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def version_list(self):
        return self._version_list

    @version_list.setter
    def version_list(self, value):
        if isinstance(value, list):
            self._version_list = list()
            for i in value:
                if isinstance(i, MiniTemplateVersionInfo):
                    self._version_list.append(i)
                else:
                    self._version_list.append(MiniTemplateVersionInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.date_create:
            if hasattr(self.date_create, 'to_alipay_dict'):
                params['date_create'] = self.date_create.to_alipay_dict()
            else:
                params['date_create'] = self.date_create
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.version_list:
            if isinstance(self.version_list, list):
                for i in range(0, len(self.version_list)):
                    element = self.version_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.version_list[i] = element.to_alipay_dict()
            if hasattr(self.version_list, 'to_alipay_dict'):
                params['version_list'] = self.version_list.to_alipay_dict()
            else:
                params['version_list'] = self.version_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniTemplateApp()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'date_create' in d:
            o.date_create = d['date_create']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'version_list' in d:
            o.version_list = d['version_list']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBoxAppInfo import SearchBoxAppInfo


class SearchBoxAccountModule(object):

    def __init__(self):
        self._app_infos = None
        self._module_id = None
        self._module_type = None

    @property
    def app_infos(self):
        return self._app_infos

    @app_infos.setter
    def app_infos(self, value):
        if isinstance(value, list):
            self._app_infos = list()
            for i in value:
                if isinstance(i, SearchBoxAppInfo):
                    self._app_infos.append(i)
                else:
                    self._app_infos.append(SearchBoxAppInfo.from_alipay_dict(i))
    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def module_type(self):
        return self._module_type

    @module_type.setter
    def module_type(self, value):
        self._module_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_infos:
            if isinstance(self.app_infos, list):
                for i in range(0, len(self.app_infos)):
                    element = self.app_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_infos[i] = element.to_alipay_dict()
            if hasattr(self.app_infos, 'to_alipay_dict'):
                params['app_infos'] = self.app_infos.to_alipay_dict()
            else:
                params['app_infos'] = self.app_infos
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.module_type:
            if hasattr(self.module_type, 'to_alipay_dict'):
                params['module_type'] = self.module_type.to_alipay_dict()
            else:
                params['module_type'] = self.module_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxAccountModule()
        if 'app_infos' in d:
            o.app_infos = d['app_infos']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        return o



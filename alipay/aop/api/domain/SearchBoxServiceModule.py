#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBoxServiceInfo import SearchBoxServiceInfo


class SearchBoxServiceModule(object):

    def __init__(self):
        self._module_id = None
        self._module_type = None
        self._service_infos = None

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
    @property
    def service_infos(self):
        return self._service_infos

    @service_infos.setter
    def service_infos(self, value):
        if isinstance(value, list):
            self._service_infos = list()
            for i in value:
                if isinstance(i, SearchBoxServiceInfo):
                    self._service_infos.append(i)
                else:
                    self._service_infos.append(SearchBoxServiceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.service_infos:
            if isinstance(self.service_infos, list):
                for i in range(0, len(self.service_infos)):
                    element = self.service_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_infos[i] = element.to_alipay_dict()
            if hasattr(self.service_infos, 'to_alipay_dict'):
                params['service_infos'] = self.service_infos.to_alipay_dict()
            else:
                params['service_infos'] = self.service_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxServiceModule()
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        if 'service_infos' in d:
            o.service_infos = d['service_infos']
        return o



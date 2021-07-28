#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxExclusiveServiceOpenApiInfos(object):

    def __init__(self):
        self._appid = None
        self._catalog_id = None
        self._catalog_name = None
        self._sepc_code = None
        self._service_code = None
        self._service_logo = None
        self._service_name = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def catalog_id(self):
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, value):
        self._catalog_id = value
    @property
    def catalog_name(self):
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, value):
        self._catalog_name = value
    @property
    def sepc_code(self):
        return self._sepc_code

    @sepc_code.setter
    def sepc_code(self, value):
        self._sepc_code = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_logo(self):
        return self._service_logo

    @service_logo.setter
    def service_logo(self, value):
        self._service_logo = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.catalog_id:
            if hasattr(self.catalog_id, 'to_alipay_dict'):
                params['catalog_id'] = self.catalog_id.to_alipay_dict()
            else:
                params['catalog_id'] = self.catalog_id
        if self.catalog_name:
            if hasattr(self.catalog_name, 'to_alipay_dict'):
                params['catalog_name'] = self.catalog_name.to_alipay_dict()
            else:
                params['catalog_name'] = self.catalog_name
        if self.sepc_code:
            if hasattr(self.sepc_code, 'to_alipay_dict'):
                params['sepc_code'] = self.sepc_code.to_alipay_dict()
            else:
                params['sepc_code'] = self.sepc_code
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_logo:
            if hasattr(self.service_logo, 'to_alipay_dict'):
                params['service_logo'] = self.service_logo.to_alipay_dict()
            else:
                params['service_logo'] = self.service_logo
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxExclusiveServiceOpenApiInfos()
        if 'appid' in d:
            o.appid = d['appid']
        if 'catalog_id' in d:
            o.catalog_id = d['catalog_id']
        if 'catalog_name' in d:
            o.catalog_name = d['catalog_name']
        if 'sepc_code' in d:
            o.sepc_code = d['sepc_code']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_logo' in d:
            o.service_logo = d['service_logo']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o



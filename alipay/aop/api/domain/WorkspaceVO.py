#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkspaceVO(object):

    def __init__(self):
        self._cloudbase_api_gateway = None
        self._description = None
        self._display_name = None
        self._enable_cloud_invoke = None
        self._enable_http = None
        self._id = None
        self._name = None
        self._outside_id = None
        self._product_id = None
        self._product_status = None
        self._region_name = None
        self._status = None

    @property
    def cloudbase_api_gateway(self):
        return self._cloudbase_api_gateway

    @cloudbase_api_gateway.setter
    def cloudbase_api_gateway(self, value):
        self._cloudbase_api_gateway = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def enable_cloud_invoke(self):
        return self._enable_cloud_invoke

    @enable_cloud_invoke.setter
    def enable_cloud_invoke(self, value):
        self._enable_cloud_invoke = value
    @property
    def enable_http(self):
        return self._enable_http

    @enable_http.setter
    def enable_http(self, value):
        self._enable_http = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def outside_id(self):
        return self._outside_id

    @outside_id.setter
    def outside_id(self, value):
        self._outside_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloudbase_api_gateway:
            if hasattr(self.cloudbase_api_gateway, 'to_alipay_dict'):
                params['cloudbase_api_gateway'] = self.cloudbase_api_gateway.to_alipay_dict()
            else:
                params['cloudbase_api_gateway'] = self.cloudbase_api_gateway
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.enable_cloud_invoke:
            if hasattr(self.enable_cloud_invoke, 'to_alipay_dict'):
                params['enable_cloud_invoke'] = self.enable_cloud_invoke.to_alipay_dict()
            else:
                params['enable_cloud_invoke'] = self.enable_cloud_invoke
        if self.enable_http:
            if hasattr(self.enable_http, 'to_alipay_dict'):
                params['enable_http'] = self.enable_http.to_alipay_dict()
            else:
                params['enable_http'] = self.enable_http
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.outside_id:
            if hasattr(self.outside_id, 'to_alipay_dict'):
                params['outside_id'] = self.outside_id.to_alipay_dict()
            else:
                params['outside_id'] = self.outside_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_status:
            if hasattr(self.product_status, 'to_alipay_dict'):
                params['product_status'] = self.product_status.to_alipay_dict()
            else:
                params['product_status'] = self.product_status
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkspaceVO()
        if 'cloudbase_api_gateway' in d:
            o.cloudbase_api_gateway = d['cloudbase_api_gateway']
        if 'description' in d:
            o.description = d['description']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'enable_cloud_invoke' in d:
            o.enable_cloud_invoke = d['enable_cloud_invoke']
        if 'enable_http' in d:
            o.enable_http = d['enable_http']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'outside_id' in d:
            o.outside_id = d['outside_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_status' in d:
            o.product_status = d['product_status']
        if 'region_name' in d:
            o.region_name = d['region_name']
        if 'status' in d:
            o.status = d['status']
        return o



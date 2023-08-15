#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnvVar import EnvVar


class Env(object):

    def __init__(self):
        self._cloudbase_api_gateway_ak = None
        self._cloudbase_api_gateway_sk = None
        self._description = None
        self._env_id = None
        self._env_vars = None
        self._name = None
        self._pkg_expiration_time = None
        self._region = None
        self._status = None
        self._workspace_pkg_name = None

    @property
    def cloudbase_api_gateway_ak(self):
        return self._cloudbase_api_gateway_ak

    @cloudbase_api_gateway_ak.setter
    def cloudbase_api_gateway_ak(self, value):
        self._cloudbase_api_gateway_ak = value
    @property
    def cloudbase_api_gateway_sk(self):
        return self._cloudbase_api_gateway_sk

    @cloudbase_api_gateway_sk.setter
    def cloudbase_api_gateway_sk(self, value):
        self._cloudbase_api_gateway_sk = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def env_vars(self):
        return self._env_vars

    @env_vars.setter
    def env_vars(self, value):
        if isinstance(value, list):
            self._env_vars = list()
            for i in value:
                if isinstance(i, EnvVar):
                    self._env_vars.append(i)
                else:
                    self._env_vars.append(EnvVar.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pkg_expiration_time(self):
        return self._pkg_expiration_time

    @pkg_expiration_time.setter
    def pkg_expiration_time(self, value):
        self._pkg_expiration_time = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def workspace_pkg_name(self):
        return self._workspace_pkg_name

    @workspace_pkg_name.setter
    def workspace_pkg_name(self, value):
        self._workspace_pkg_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloudbase_api_gateway_ak:
            if hasattr(self.cloudbase_api_gateway_ak, 'to_alipay_dict'):
                params['cloudbase_api_gateway_ak'] = self.cloudbase_api_gateway_ak.to_alipay_dict()
            else:
                params['cloudbase_api_gateway_ak'] = self.cloudbase_api_gateway_ak
        if self.cloudbase_api_gateway_sk:
            if hasattr(self.cloudbase_api_gateway_sk, 'to_alipay_dict'):
                params['cloudbase_api_gateway_sk'] = self.cloudbase_api_gateway_sk.to_alipay_dict()
            else:
                params['cloudbase_api_gateway_sk'] = self.cloudbase_api_gateway_sk
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.env_vars:
            if isinstance(self.env_vars, list):
                for i in range(0, len(self.env_vars)):
                    element = self.env_vars[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.env_vars[i] = element.to_alipay_dict()
            if hasattr(self.env_vars, 'to_alipay_dict'):
                params['env_vars'] = self.env_vars.to_alipay_dict()
            else:
                params['env_vars'] = self.env_vars
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pkg_expiration_time:
            if hasattr(self.pkg_expiration_time, 'to_alipay_dict'):
                params['pkg_expiration_time'] = self.pkg_expiration_time.to_alipay_dict()
            else:
                params['pkg_expiration_time'] = self.pkg_expiration_time
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.workspace_pkg_name:
            if hasattr(self.workspace_pkg_name, 'to_alipay_dict'):
                params['workspace_pkg_name'] = self.workspace_pkg_name.to_alipay_dict()
            else:
                params['workspace_pkg_name'] = self.workspace_pkg_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Env()
        if 'cloudbase_api_gateway_ak' in d:
            o.cloudbase_api_gateway_ak = d['cloudbase_api_gateway_ak']
        if 'cloudbase_api_gateway_sk' in d:
            o.cloudbase_api_gateway_sk = d['cloudbase_api_gateway_sk']
        if 'description' in d:
            o.description = d['description']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'env_vars' in d:
            o.env_vars = d['env_vars']
        if 'name' in d:
            o.name = d['name']
        if 'pkg_expiration_time' in d:
            o.pkg_expiration_time = d['pkg_expiration_time']
        if 'region' in d:
            o.region = d['region']
        if 'status' in d:
            o.status = d['status']
        if 'workspace_pkg_name' in d:
            o.workspace_pkg_name = d['workspace_pkg_name']
        return o



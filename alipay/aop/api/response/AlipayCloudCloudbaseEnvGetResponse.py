#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnvVar import EnvVar


class AlipayCloudCloudbaseEnvGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseEnvGetResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseEnvGetResponse, self).parse_response_content(response_content)
        if 'cloudbase_api_gateway_ak' in response:
            self.cloudbase_api_gateway_ak = response['cloudbase_api_gateway_ak']
        if 'cloudbase_api_gateway_sk' in response:
            self.cloudbase_api_gateway_sk = response['cloudbase_api_gateway_sk']
        if 'description' in response:
            self.description = response['description']
        if 'env_id' in response:
            self.env_id = response['env_id']
        if 'env_vars' in response:
            self.env_vars = response['env_vars']
        if 'name' in response:
            self.name = response['name']
        if 'pkg_expiration_time' in response:
            self.pkg_expiration_time = response['pkg_expiration_time']
        if 'region' in response:
            self.region = response['region']
        if 'status' in response:
            self.status = response['status']
        if 'workspace_pkg_name' in response:
            self.workspace_pkg_name = response['workspace_pkg_name']

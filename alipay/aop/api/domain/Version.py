#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnvVar import EnvVar


class Version(object):

    def __init__(self):
        self._description = None
        self._env_vars = None
        self._id = None
        self._latest = None
        self._max_idle_timeout = None
        self._max_req_timeout = None
        self._max_retry_time = None
        self._name = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def latest(self):
        return self._latest

    @latest.setter
    def latest(self, value):
        self._latest = value
    @property
    def max_idle_timeout(self):
        return self._max_idle_timeout

    @max_idle_timeout.setter
    def max_idle_timeout(self, value):
        self._max_idle_timeout = value
    @property
    def max_req_timeout(self):
        return self._max_req_timeout

    @max_req_timeout.setter
    def max_req_timeout(self, value):
        self._max_req_timeout = value
    @property
    def max_retry_time(self):
        return self._max_retry_time

    @max_retry_time.setter
    def max_retry_time(self, value):
        self._max_retry_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.latest:
            if hasattr(self.latest, 'to_alipay_dict'):
                params['latest'] = self.latest.to_alipay_dict()
            else:
                params['latest'] = self.latest
        if self.max_idle_timeout:
            if hasattr(self.max_idle_timeout, 'to_alipay_dict'):
                params['max_idle_timeout'] = self.max_idle_timeout.to_alipay_dict()
            else:
                params['max_idle_timeout'] = self.max_idle_timeout
        if self.max_req_timeout:
            if hasattr(self.max_req_timeout, 'to_alipay_dict'):
                params['max_req_timeout'] = self.max_req_timeout.to_alipay_dict()
            else:
                params['max_req_timeout'] = self.max_req_timeout
        if self.max_retry_time:
            if hasattr(self.max_retry_time, 'to_alipay_dict'):
                params['max_retry_time'] = self.max_retry_time.to_alipay_dict()
            else:
                params['max_retry_time'] = self.max_retry_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Version()
        if 'description' in d:
            o.description = d['description']
        if 'env_vars' in d:
            o.env_vars = d['env_vars']
        if 'id' in d:
            o.id = d['id']
        if 'latest' in d:
            o.latest = d['latest']
        if 'max_idle_timeout' in d:
            o.max_idle_timeout = d['max_idle_timeout']
        if 'max_req_timeout' in d:
            o.max_req_timeout = d['max_req_timeout']
        if 'max_retry_time' in d:
            o.max_retry_time = d['max_retry_time']
        if 'name' in d:
            o.name = d['name']
        return o



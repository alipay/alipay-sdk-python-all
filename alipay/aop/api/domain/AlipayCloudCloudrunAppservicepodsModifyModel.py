#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunAppservicepodsModifyModel(object):

    def __init__(self):
        self._app_service_name = None
        self._env_id = None
        self._host_name = None
        self._pod_name = None
        self._pod_uuid = None

    @property
    def app_service_name(self):
        return self._app_service_name

    @app_service_name.setter
    def app_service_name(self, value):
        self._app_service_name = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def host_name(self):
        return self._host_name

    @host_name.setter
    def host_name(self, value):
        self._host_name = value
    @property
    def pod_name(self):
        return self._pod_name

    @pod_name.setter
    def pod_name(self, value):
        self._pod_name = value
    @property
    def pod_uuid(self):
        return self._pod_uuid

    @pod_uuid.setter
    def pod_uuid(self, value):
        self._pod_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_service_name:
            if hasattr(self.app_service_name, 'to_alipay_dict'):
                params['app_service_name'] = self.app_service_name.to_alipay_dict()
            else:
                params['app_service_name'] = self.app_service_name
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.host_name:
            if hasattr(self.host_name, 'to_alipay_dict'):
                params['host_name'] = self.host_name.to_alipay_dict()
            else:
                params['host_name'] = self.host_name
        if self.pod_name:
            if hasattr(self.pod_name, 'to_alipay_dict'):
                params['pod_name'] = self.pod_name.to_alipay_dict()
            else:
                params['pod_name'] = self.pod_name
        if self.pod_uuid:
            if hasattr(self.pod_uuid, 'to_alipay_dict'):
                params['pod_uuid'] = self.pod_uuid.to_alipay_dict()
            else:
                params['pod_uuid'] = self.pod_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunAppservicepodsModifyModel()
        if 'app_service_name' in d:
            o.app_service_name = d['app_service_name']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'host_name' in d:
            o.host_name = d['host_name']
        if 'pod_name' in d:
            o.pod_name = d['pod_name']
        if 'pod_uuid' in d:
            o.pod_uuid = d['pod_uuid']
        return o



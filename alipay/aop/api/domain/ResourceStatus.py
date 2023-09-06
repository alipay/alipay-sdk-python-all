#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceStatus(object):

    def __init__(self):
        self._resource_id = None
        self._resource_status = None
        self._resource_type = None
        self._spec_instance_id = None
        self._status = None

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def resource_status(self):
        return self._resource_status

    @resource_status.setter
    def resource_status(self, value):
        self._resource_status = value
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value
    @property
    def spec_instance_id(self):
        return self._spec_instance_id

    @spec_instance_id.setter
    def spec_instance_id(self, value):
        self._spec_instance_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.resource_status:
            if hasattr(self.resource_status, 'to_alipay_dict'):
                params['resource_status'] = self.resource_status.to_alipay_dict()
            else:
                params['resource_status'] = self.resource_status
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        if self.spec_instance_id:
            if hasattr(self.spec_instance_id, 'to_alipay_dict'):
                params['spec_instance_id'] = self.spec_instance_id.to_alipay_dict()
            else:
                params['spec_instance_id'] = self.spec_instance_id
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
        o = ResourceStatus()
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'resource_status' in d:
            o.resource_status = d['resource_status']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        if 'spec_instance_id' in d:
            o.spec_instance_id = d['spec_instance_id']
        if 'status' in d:
            o.status = d['status']
        return o



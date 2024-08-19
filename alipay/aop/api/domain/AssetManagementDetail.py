#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetManagementDetail(object):

    def __init__(self):
        self._check_name = None
        self._check_type = None
        self._require_phase = None
        self._require_resource = None

    @property
    def check_name(self):
        return self._check_name

    @check_name.setter
    def check_name(self, value):
        self._check_name = value
    @property
    def check_type(self):
        return self._check_type

    @check_type.setter
    def check_type(self, value):
        self._check_type = value
    @property
    def require_phase(self):
        return self._require_phase

    @require_phase.setter
    def require_phase(self, value):
        self._require_phase = value
    @property
    def require_resource(self):
        return self._require_resource

    @require_resource.setter
    def require_resource(self, value):
        self._require_resource = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_name:
            if hasattr(self.check_name, 'to_alipay_dict'):
                params['check_name'] = self.check_name.to_alipay_dict()
            else:
                params['check_name'] = self.check_name
        if self.check_type:
            if hasattr(self.check_type, 'to_alipay_dict'):
                params['check_type'] = self.check_type.to_alipay_dict()
            else:
                params['check_type'] = self.check_type
        if self.require_phase:
            if hasattr(self.require_phase, 'to_alipay_dict'):
                params['require_phase'] = self.require_phase.to_alipay_dict()
            else:
                params['require_phase'] = self.require_phase
        if self.require_resource:
            if hasattr(self.require_resource, 'to_alipay_dict'):
                params['require_resource'] = self.require_resource.to_alipay_dict()
            else:
                params['require_resource'] = self.require_resource
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetManagementDetail()
        if 'check_name' in d:
            o.check_name = d['check_name']
        if 'check_type' in d:
            o.check_type = d['check_type']
        if 'require_phase' in d:
            o.require_phase = d['require_phase']
        if 'require_resource' in d:
            o.require_resource = d['require_resource']
        return o



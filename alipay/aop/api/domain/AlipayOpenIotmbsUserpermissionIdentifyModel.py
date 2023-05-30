#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsUserpermissionIdentifyModel(object):

    def __init__(self):
        self._param_id = None
        self._param_type = None
        self._project_id = None
        self._sn = None

    @property
    def param_id(self):
        return self._param_id

    @param_id.setter
    def param_id(self, value):
        self._param_id = value
    @property
    def param_type(self):
        return self._param_type

    @param_type.setter
    def param_type(self, value):
        self._param_type = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_id:
            if hasattr(self.param_id, 'to_alipay_dict'):
                params['param_id'] = self.param_id.to_alipay_dict()
            else:
                params['param_id'] = self.param_id
        if self.param_type:
            if hasattr(self.param_type, 'to_alipay_dict'):
                params['param_type'] = self.param_type.to_alipay_dict()
            else:
                params['param_type'] = self.param_type
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsUserpermissionIdentifyModel()
        if 'param_id' in d:
            o.param_id = d['param_id']
        if 'param_type' in d:
            o.param_type = d['param_type']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'sn' in d:
            o.sn = d['sn']
        return o



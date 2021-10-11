#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDossierNameMatchModel(object):

    def __init__(self):
        self._ep_name = None
        self._ep_type_scope = None

    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_type_scope(self):
        return self._ep_type_scope

    @ep_type_scope.setter
    def ep_type_scope(self, value):
        self._ep_type_scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_type_scope:
            if hasattr(self.ep_type_scope, 'to_alipay_dict'):
                params['ep_type_scope'] = self.ep_type_scope.to_alipay_dict()
            else:
                params['ep_type_scope'] = self.ep_type_scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDossierNameMatchModel()
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_type_scope' in d:
            o.ep_type_scope = d['ep_type_scope']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementInvolvedPartyQuerier(object):

    def __init__(self):
        self._ip_id = None
        self._ip_role_id = None
        self._ip_type = None

    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_type(self):
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        self._ip_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_type:
            if hasattr(self.ip_type, 'to_alipay_dict'):
                params['ip_type'] = self.ip_type.to_alipay_dict()
            else:
                params['ip_type'] = self.ip_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementInvolvedPartyQuerier()
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_type' in d:
            o.ip_type = d['ip_type']
        return o



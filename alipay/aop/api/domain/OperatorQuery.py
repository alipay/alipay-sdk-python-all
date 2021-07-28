#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorQuery(object):

    def __init__(self):
        self._id = None
        self._id_type = None
        self._logon_id_type = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def logon_id_type(self):
        return self._logon_id_type

    @logon_id_type.setter
    def logon_id_type(self, value):
        self._logon_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.logon_id_type:
            if hasattr(self.logon_id_type, 'to_alipay_dict'):
                params['logon_id_type'] = self.logon_id_type.to_alipay_dict()
            else:
                params['logon_id_type'] = self.logon_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorQuery()
        if 'id' in d:
            o.id = d['id']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'logon_id_type' in d:
            o.logon_id_type = d['logon_id_type']
        return o



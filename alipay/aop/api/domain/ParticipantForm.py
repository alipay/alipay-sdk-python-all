#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParticipantForm(object):

    def __init__(self):
        self._ext_info = None
        self._identity_id = None
        self._identity_type = None
        self._principal_open_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.principal_open_id:
            if hasattr(self.principal_open_id, 'to_alipay_dict'):
                params['principal_open_id'] = self.principal_open_id.to_alipay_dict()
            else:
                params['principal_open_id'] = self.principal_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParticipantForm()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'principal_open_id' in d:
            o.principal_open_id = d['principal_open_id']
        return o



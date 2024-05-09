#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchSessionDetailQueryModel(object):

    def __init__(self):
        self._identity_id = None
        self._session_id = None

    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchSessionDetailQueryModel()
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchSessionDetailModifyModel(object):

    def __init__(self):
        self._identity_id = None
        self._new_title = None
        self._operate_type = None
        self._session_id = None

    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def new_title(self):
        return self._new_title

    @new_title.setter
    def new_title(self, value):
        self._new_title = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
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
        if self.new_title:
            if hasattr(self.new_title, 'to_alipay_dict'):
                params['new_title'] = self.new_title.to_alipay_dict()
            else:
                params['new_title'] = self.new_title
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
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
        o = AntfortuneFinresearchSessionDetailModifyModel()
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'new_title' in d:
            o.new_title = d['new_title']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o



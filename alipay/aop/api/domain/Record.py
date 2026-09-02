#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Record(object):

    def __init__(self):
        self._aq_open_id = None
        self._data_id = None
        self._data_source = None
        self._data_type = None
        self._open_id = None
        self._user_id = None

    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Record()
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



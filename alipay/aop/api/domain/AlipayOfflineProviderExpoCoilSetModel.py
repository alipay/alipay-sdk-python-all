#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoCoilSetModel(object):

    def __init__(self):
        self._coil_type = None
        self._open_id = None
        self._page_params = None
        self._tag_id = None
        self._user_id = None
        self._user_name = None

    @property
    def coil_type(self):
        return self._coil_type

    @coil_type.setter
    def coil_type(self, value):
        self._coil_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_params(self):
        return self._page_params

    @page_params.setter
    def page_params(self, value):
        self._page_params = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.coil_type:
            if hasattr(self.coil_type, 'to_alipay_dict'):
                params['coil_type'] = self.coil_type.to_alipay_dict()
            else:
                params['coil_type'] = self.coil_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_params:
            if hasattr(self.page_params, 'to_alipay_dict'):
                params['page_params'] = self.page_params.to_alipay_dict()
            else:
                params['page_params'] = self.page_params
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderExpoCoilSetModel()
        if 'coil_type' in d:
            o.coil_type = d['coil_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_params' in d:
            o.page_params = d['page_params']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



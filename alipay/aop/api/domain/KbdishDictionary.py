#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishDictionary(object):

    def __init__(self):
        self._create_user = None
        self._dictionary_id = None
        self._ext_info = None
        self._merchant_id = None
        self._name = None
        self._status = None
        self._update_user = None

    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def dictionary_id(self):
        return self._dictionary_id

    @dictionary_id.setter
    def dictionary_id(self, value):
        self._dictionary_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.dictionary_id:
            if hasattr(self.dictionary_id, 'to_alipay_dict'):
                params['dictionary_id'] = self.dictionary_id.to_alipay_dict()
            else:
                params['dictionary_id'] = self.dictionary_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishDictionary()
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'dictionary_id' in d:
            o.dictionary_id = d['dictionary_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerZmcardIdentityQueryModel(object):

    def __init__(self):
        self._guest_open_id = None
        self._guest_uid = None
        self._host_open_id = None
        self._host_uid = None
        self._role_type = None
        self._source = None

    @property
    def guest_open_id(self):
        return self._guest_open_id

    @guest_open_id.setter
    def guest_open_id(self, value):
        self._guest_open_id = value
    @property
    def guest_uid(self):
        return self._guest_uid

    @guest_uid.setter
    def guest_uid(self, value):
        self._guest_uid = value
    @property
    def host_open_id(self):
        return self._host_open_id

    @host_open_id.setter
    def host_open_id(self, value):
        self._host_open_id = value
    @property
    def host_uid(self):
        return self._host_uid

    @host_uid.setter
    def host_uid(self, value):
        self._host_uid = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.guest_open_id:
            if hasattr(self.guest_open_id, 'to_alipay_dict'):
                params['guest_open_id'] = self.guest_open_id.to_alipay_dict()
            else:
                params['guest_open_id'] = self.guest_open_id
        if self.guest_uid:
            if hasattr(self.guest_uid, 'to_alipay_dict'):
                params['guest_uid'] = self.guest_uid.to_alipay_dict()
            else:
                params['guest_uid'] = self.guest_uid
        if self.host_open_id:
            if hasattr(self.host_open_id, 'to_alipay_dict'):
                params['host_open_id'] = self.host_open_id.to_alipay_dict()
            else:
                params['host_open_id'] = self.host_open_id
        if self.host_uid:
            if hasattr(self.host_uid, 'to_alipay_dict'):
                params['host_uid'] = self.host_uid.to_alipay_dict()
            else:
                params['host_uid'] = self.host_uid
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerZmcardIdentityQueryModel()
        if 'guest_open_id' in d:
            o.guest_open_id = d['guest_open_id']
        if 'guest_uid' in d:
            o.guest_uid = d['guest_uid']
        if 'host_open_id' in d:
            o.host_open_id = d['host_open_id']
        if 'host_uid' in d:
            o.host_uid = d['host_uid']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'source' in d:
            o.source = d['source']
        return o



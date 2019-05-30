#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountBindingSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._create_time = None
        self._data_version = None
        self._havana_user_id = None
        self._modify_time = None
        self._realm = None
        self._status = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def havana_user_id(self):
        return self._havana_user_id

    @havana_user_id.setter
    def havana_user_id(self, value):
        self._havana_user_id = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def realm(self):
        return self._realm

    @realm.setter
    def realm(self, value):
        self._realm = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.havana_user_id:
            if hasattr(self.havana_user_id, 'to_alipay_dict'):
                params['havana_user_id'] = self.havana_user_id.to_alipay_dict()
            else:
                params['havana_user_id'] = self.havana_user_id
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.realm:
            if hasattr(self.realm, 'to_alipay_dict'):
                params['realm'] = self.realm.to_alipay_dict()
            else:
                params['realm'] = self.realm
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountBindingSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'havana_user_id' in d:
            o.havana_user_id = d['havana_user_id']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'realm' in d:
            o.realm = d['realm']
        if 'status' in d:
            o.status = d['status']
        return o



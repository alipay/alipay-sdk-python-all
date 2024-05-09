#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoContractsLoanAuthSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._auth_status = None
        self._free_portion_grant_time = None
        self._free_portion_used_time = None
        self._open_id = None
        self._out_user_id = None
        self._sync_request_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def free_portion_grant_time(self):
        return self._free_portion_grant_time

    @free_portion_grant_time.setter
    def free_portion_grant_time(self, value):
        self._free_portion_grant_time = value
    @property
    def free_portion_used_time(self):
        return self._free_portion_used_time

    @free_portion_used_time.setter
    def free_portion_used_time(self, value):
        self._free_portion_used_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def sync_request_id(self):
        return self._sync_request_id

    @sync_request_id.setter
    def sync_request_id(self, value):
        self._sync_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.free_portion_grant_time:
            if hasattr(self.free_portion_grant_time, 'to_alipay_dict'):
                params['free_portion_grant_time'] = self.free_portion_grant_time.to_alipay_dict()
            else:
                params['free_portion_grant_time'] = self.free_portion_grant_time
        if self.free_portion_used_time:
            if hasattr(self.free_portion_used_time, 'to_alipay_dict'):
                params['free_portion_used_time'] = self.free_portion_used_time.to_alipay_dict()
            else:
                params['free_portion_used_time'] = self.free_portion_used_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.sync_request_id:
            if hasattr(self.sync_request_id, 'to_alipay_dict'):
                params['sync_request_id'] = self.sync_request_id.to_alipay_dict()
            else:
                params['sync_request_id'] = self.sync_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractsLoanAuthSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'free_portion_grant_time' in d:
            o.free_portion_grant_time = d['free_portion_grant_time']
        if 'free_portion_used_time' in d:
            o.free_portion_used_time = d['free_portion_used_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'sync_request_id' in d:
            o.sync_request_id = d['sync_request_id']
        return o



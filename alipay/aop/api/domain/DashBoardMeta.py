#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DashBoardMeta(object):

    def __init__(self):
        self._auth_status = None
        self._create_time = None
        self._dashboard_id = None
        self._dashboard_name = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def dashboard_id(self):
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, value):
        self._dashboard_id = value
    @property
    def dashboard_name(self):
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, value):
        self._dashboard_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.dashboard_id:
            if hasattr(self.dashboard_id, 'to_alipay_dict'):
                params['dashboard_id'] = self.dashboard_id.to_alipay_dict()
            else:
                params['dashboard_id'] = self.dashboard_id
        if self.dashboard_name:
            if hasattr(self.dashboard_name, 'to_alipay_dict'):
                params['dashboard_name'] = self.dashboard_name.to_alipay_dict()
            else:
                params['dashboard_name'] = self.dashboard_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DashBoardMeta()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'dashboard_id' in d:
            o.dashboard_id = d['dashboard_id']
        if 'dashboard_name' in d:
            o.dashboard_name = d['dashboard_name']
        return o



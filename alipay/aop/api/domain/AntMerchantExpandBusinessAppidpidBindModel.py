#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBusinessAppidpidBindModel(object):

    def __init__(self):
        self._app_id_bind = None
        self._pid_bind = None

    @property
    def app_id_bind(self):
        return self._app_id_bind

    @app_id_bind.setter
    def app_id_bind(self, value):
        self._app_id_bind = value
    @property
    def pid_bind(self):
        return self._pid_bind

    @pid_bind.setter
    def pid_bind(self, value):
        self._pid_bind = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id_bind:
            if hasattr(self.app_id_bind, 'to_alipay_dict'):
                params['app_id_bind'] = self.app_id_bind.to_alipay_dict()
            else:
                params['app_id_bind'] = self.app_id_bind
        if self.pid_bind:
            if hasattr(self.pid_bind, 'to_alipay_dict'):
                params['pid_bind'] = self.pid_bind.to_alipay_dict()
            else:
                params['pid_bind'] = self.pid_bind
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandBusinessAppidpidBindModel()
        if 'app_id_bind' in d:
            o.app_id_bind = d['app_id_bind']
        if 'pid_bind' in d:
            o.pid_bind = d['pid_bind']
        return o



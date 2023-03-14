#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniIsvFastregisterCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._auth_notify_url = None
        self._out_order_no = None
        self._uid = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def auth_notify_url(self):
        return self._auth_notify_url

    @auth_notify_url.setter
    def auth_notify_url(self, value):
        self._auth_notify_url = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.auth_notify_url:
            if hasattr(self.auth_notify_url, 'to_alipay_dict'):
                params['auth_notify_url'] = self.auth_notify_url.to_alipay_dict()
            else:
                params['auth_notify_url'] = self.auth_notify_url
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniIsvFastregisterCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'auth_notify_url' in d:
            o.auth_notify_url = d['auth_notify_url']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'uid' in d:
            o.uid = d['uid']
        return o



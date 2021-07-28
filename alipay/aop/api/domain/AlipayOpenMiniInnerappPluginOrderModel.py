#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappPluginOrderModel(object):

    def __init__(self):
        self._app_origin = None
        self._merchandise_id = None
        self._mini_app_id = None
        self._request_id = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def merchandise_id(self):
        return self._merchandise_id

    @merchandise_id.setter
    def merchandise_id(self, value):
        self._merchandise_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.merchandise_id:
            if hasattr(self.merchandise_id, 'to_alipay_dict'):
                params['merchandise_id'] = self.merchandise_id.to_alipay_dict()
            else:
                params['merchandise_id'] = self.merchandise_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerappPluginOrderModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'merchandise_id' in d:
            o.merchandise_id = d['merchandise_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o



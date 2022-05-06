#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerSafedomainQueryModel(object):

    def __init__(self):
        self._app_origin = None
        self._mini_app_id = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerSafedomainQueryModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o



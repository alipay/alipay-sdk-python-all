#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBrandAuthQueryModel(object):

    def __init__(self):
        self._authorized = None
        self._need_app = None

    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, value):
        self._authorized = value
    @property
    def need_app(self):
        return self._need_app

    @need_app.setter
    def need_app(self, value):
        self._need_app = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized:
            if hasattr(self.authorized, 'to_alipay_dict'):
                params['authorized'] = self.authorized.to_alipay_dict()
            else:
                params['authorized'] = self.authorized
        if self.need_app:
            if hasattr(self.need_app, 'to_alipay_dict'):
                params['need_app'] = self.need_app.to_alipay_dict()
            else:
                params['need_app'] = self.need_app
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBrandAuthQueryModel()
        if 'authorized' in d:
            o.authorized = d['authorized']
        if 'need_app' in d:
            o.need_app = d['need_app']
        return o



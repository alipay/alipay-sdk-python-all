#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QrcodeWhiteList(object):

    def __init__(self):
        self._app_id_or_domain = None
        self._type = None

    @property
    def app_id_or_domain(self):
        return self._app_id_or_domain

    @app_id_or_domain.setter
    def app_id_or_domain(self, value):
        self._app_id_or_domain = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id_or_domain:
            if hasattr(self.app_id_or_domain, 'to_alipay_dict'):
                params['app_id_or_domain'] = self.app_id_or_domain.to_alipay_dict()
            else:
                params['app_id_or_domain'] = self.app_id_or_domain
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QrcodeWhiteList()
        if 'app_id_or_domain' in d:
            o.app_id_or_domain = d['app_id_or_domain']
        if 'type' in d:
            o.type = d['type']
        return o



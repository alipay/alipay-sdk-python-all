#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JumpInfo(object):

    def __init__(self):
        self._app_identifier = None
        self._applink_url = None
        self._normal_url = None
        self._scheme_url = None

    @property
    def app_identifier(self):
        return self._app_identifier

    @app_identifier.setter
    def app_identifier(self, value):
        self._app_identifier = value
    @property
    def applink_url(self):
        return self._applink_url

    @applink_url.setter
    def applink_url(self, value):
        self._applink_url = value
    @property
    def normal_url(self):
        return self._normal_url

    @normal_url.setter
    def normal_url(self, value):
        self._normal_url = value
    @property
    def scheme_url(self):
        return self._scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self._scheme_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_identifier:
            if hasattr(self.app_identifier, 'to_alipay_dict'):
                params['app_identifier'] = self.app_identifier.to_alipay_dict()
            else:
                params['app_identifier'] = self.app_identifier
        if self.applink_url:
            if hasattr(self.applink_url, 'to_alipay_dict'):
                params['applink_url'] = self.applink_url.to_alipay_dict()
            else:
                params['applink_url'] = self.applink_url
        if self.normal_url:
            if hasattr(self.normal_url, 'to_alipay_dict'):
                params['normal_url'] = self.normal_url.to_alipay_dict()
            else:
                params['normal_url'] = self.normal_url
        if self.scheme_url:
            if hasattr(self.scheme_url, 'to_alipay_dict'):
                params['scheme_url'] = self.scheme_url.to_alipay_dict()
            else:
                params['scheme_url'] = self.scheme_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JumpInfo()
        if 'app_identifier' in d:
            o.app_identifier = d['app_identifier']
        if 'applink_url' in d:
            o.applink_url = d['applink_url']
        if 'normal_url' in d:
            o.normal_url = d['normal_url']
        if 'scheme_url' in d:
            o.scheme_url = d['scheme_url']
        return o



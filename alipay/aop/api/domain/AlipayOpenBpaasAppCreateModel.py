#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBpaasAppCreateModel(object):

    def __init__(self):
        self._app_icon_url = None
        self._app_introduction = None
        self._app_name = None
        self._app_package = None
        self._app_platform = None
        self._app_sign = None
        self._app_type = None

    @property
    def app_icon_url(self):
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, value):
        self._app_icon_url = value
    @property
    def app_introduction(self):
        return self._app_introduction

    @app_introduction.setter
    def app_introduction(self, value):
        self._app_introduction = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_package(self):
        return self._app_package

    @app_package.setter
    def app_package(self, value):
        self._app_package = value
    @property
    def app_platform(self):
        return self._app_platform

    @app_platform.setter
    def app_platform(self, value):
        self._app_platform = value
    @property
    def app_sign(self):
        return self._app_sign

    @app_sign.setter
    def app_sign(self, value):
        self._app_sign = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_icon_url:
            if hasattr(self.app_icon_url, 'to_alipay_dict'):
                params['app_icon_url'] = self.app_icon_url.to_alipay_dict()
            else:
                params['app_icon_url'] = self.app_icon_url
        if self.app_introduction:
            if hasattr(self.app_introduction, 'to_alipay_dict'):
                params['app_introduction'] = self.app_introduction.to_alipay_dict()
            else:
                params['app_introduction'] = self.app_introduction
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_package:
            if hasattr(self.app_package, 'to_alipay_dict'):
                params['app_package'] = self.app_package.to_alipay_dict()
            else:
                params['app_package'] = self.app_package
        if self.app_platform:
            if hasattr(self.app_platform, 'to_alipay_dict'):
                params['app_platform'] = self.app_platform.to_alipay_dict()
            else:
                params['app_platform'] = self.app_platform
        if self.app_sign:
            if hasattr(self.app_sign, 'to_alipay_dict'):
                params['app_sign'] = self.app_sign.to_alipay_dict()
            else:
                params['app_sign'] = self.app_sign
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBpaasAppCreateModel()
        if 'app_icon_url' in d:
            o.app_icon_url = d['app_icon_url']
        if 'app_introduction' in d:
            o.app_introduction = d['app_introduction']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_package' in d:
            o.app_package = d['app_package']
        if 'app_platform' in d:
            o.app_platform = d['app_platform']
        if 'app_sign' in d:
            o.app_sign = d['app_sign']
        if 'app_type' in d:
            o.app_type = d['app_type']
        return o



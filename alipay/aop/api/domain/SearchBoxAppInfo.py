#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxAppInfo(object):

    def __init__(self):
        self._app_name = None
        self._app_type = None
        self._relate_appid = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def relate_appid(self):
        return self._relate_appid

    @relate_appid.setter
    def relate_appid(self, value):
        self._relate_appid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.relate_appid:
            if hasattr(self.relate_appid, 'to_alipay_dict'):
                params['relate_appid'] = self.relate_appid.to_alipay_dict()
            else:
                params['relate_appid'] = self.relate_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxAppInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'relate_appid' in d:
            o.relate_appid = d['relate_appid']
        return o



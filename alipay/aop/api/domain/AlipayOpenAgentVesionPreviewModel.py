#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentVesionPreviewModel(object):

    def __init__(self):
        self._app_version = None
        self._bundle_id = None
        self._enviroment = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def enviroment(self):
        return self._enviroment

    @enviroment.setter
    def enviroment(self, value):
        self._enviroment = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.enviroment:
            if hasattr(self.enviroment, 'to_alipay_dict'):
                params['enviroment'] = self.enviroment.to_alipay_dict()
            else:
                params['enviroment'] = self.enviroment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentVesionPreviewModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'enviroment' in d:
            o.enviroment = d['enviroment']
        return o



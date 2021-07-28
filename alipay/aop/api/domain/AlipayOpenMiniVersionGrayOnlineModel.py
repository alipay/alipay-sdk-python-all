#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniVersionGrayOnlineModel(object):

    def __init__(self):
        self._app_version = None
        self._bundle_id = None
        self._gray_strategy = None

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
    def gray_strategy(self):
        return self._gray_strategy

    @gray_strategy.setter
    def gray_strategy(self, value):
        self._gray_strategy = value


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
        if self.gray_strategy:
            if hasattr(self.gray_strategy, 'to_alipay_dict'):
                params['gray_strategy'] = self.gray_strategy.to_alipay_dict()
            else:
                params['gray_strategy'] = self.gray_strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniVersionGrayOnlineModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'gray_strategy' in d:
            o.gray_strategy = d['gray_strategy']
        return o



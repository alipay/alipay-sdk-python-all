#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionGrayPublishModel(object):

    def __init__(self):
        self._app_origin = None
        self._app_version = None
        self._beta_app_id_list = None
        self._bundle_id = None
        self._gray_strategy = None
        self._mini_app_id = None
        self._pid = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def beta_app_id_list(self):
        return self._beta_app_id_list

    @beta_app_id_list.setter
    def beta_app_id_list(self, value):
        if isinstance(value, list):
            self._beta_app_id_list = list()
            for i in value:
                self._beta_app_id_list.append(i)
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
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.beta_app_id_list:
            if isinstance(self.beta_app_id_list, list):
                for i in range(0, len(self.beta_app_id_list)):
                    element = self.beta_app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.beta_app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.beta_app_id_list, 'to_alipay_dict'):
                params['beta_app_id_list'] = self.beta_app_id_list.to_alipay_dict()
            else:
                params['beta_app_id_list'] = self.beta_app_id_list
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
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionGrayPublishModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'beta_app_id_list' in d:
            o.beta_app_id_list = d['beta_app_id_list']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'gray_strategy' in d:
            o.gray_strategy = d['gray_strategy']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'pid' in d:
            o.pid = d['pid']
        return o



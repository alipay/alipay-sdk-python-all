#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerRelationconfigModifyModel(object):

    def __init__(self):
        self._app_origin = None
        self._dev_id = None
        self._mini_app_id = None
        self._operate_id = None
        self._un_limited = None
        self._white_list = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def operate_id(self):
        return self._operate_id

    @operate_id.setter
    def operate_id(self, value):
        self._operate_id = value
    @property
    def un_limited(self):
        return self._un_limited

    @un_limited.setter
    def un_limited(self, value):
        self._un_limited = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        self._white_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.operate_id:
            if hasattr(self.operate_id, 'to_alipay_dict'):
                params['operate_id'] = self.operate_id.to_alipay_dict()
            else:
                params['operate_id'] = self.operate_id
        if self.un_limited:
            if hasattr(self.un_limited, 'to_alipay_dict'):
                params['un_limited'] = self.un_limited.to_alipay_dict()
            else:
                params['un_limited'] = self.un_limited
        if self.white_list:
            if hasattr(self.white_list, 'to_alipay_dict'):
                params['white_list'] = self.white_list.to_alipay_dict()
            else:
                params['white_list'] = self.white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerRelationconfigModifyModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'operate_id' in d:
            o.operate_id = d['operate_id']
        if 'un_limited' in d:
            o.un_limited = d['un_limited']
        if 'white_list' in d:
            o.white_list = d['white_list']
        return o



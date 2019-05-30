#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoQueryModel(object):

    def __init__(self):
        self._app_sub_type = None
        self._inst_code = None
        self._mini_app_id = None
        self._mini_app_name = None

    @property
    def app_sub_type(self):
        return self._app_sub_type

    @app_sub_type.setter
    def app_sub_type(self, value):
        self._app_sub_type = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_sub_type:
            if hasattr(self.app_sub_type, 'to_alipay_dict'):
                params['app_sub_type'] = self.app_sub_type.to_alipay_dict()
            else:
                params['app_sub_type'] = self.app_sub_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerbaseinfoQueryModel()
        if 'app_sub_type' in d:
            o.app_sub_type = d['app_sub_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        return o



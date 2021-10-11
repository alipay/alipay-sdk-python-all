#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerMtopsyncModifyModel(object):

    def __init__(self):
        self._alipay_app_id = None
        self._app_origin = None
        self._mtop_app_key = None
        self._operation_type = None

    @property
    def alipay_app_id(self):
        return self._alipay_app_id

    @alipay_app_id.setter
    def alipay_app_id(self, value):
        self._alipay_app_id = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def mtop_app_key(self):
        return self._mtop_app_key

    @mtop_app_key.setter
    def mtop_app_key(self, value):
        self._mtop_app_key = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_app_id:
            if hasattr(self.alipay_app_id, 'to_alipay_dict'):
                params['alipay_app_id'] = self.alipay_app_id.to_alipay_dict()
            else:
                params['alipay_app_id'] = self.alipay_app_id
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.mtop_app_key:
            if hasattr(self.mtop_app_key, 'to_alipay_dict'):
                params['mtop_app_key'] = self.mtop_app_key.to_alipay_dict()
            else:
                params['mtop_app_key'] = self.mtop_app_key
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerMtopsyncModifyModel()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'mtop_app_key' in d:
            o.mtop_app_key = d['mtop_app_key']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        return o



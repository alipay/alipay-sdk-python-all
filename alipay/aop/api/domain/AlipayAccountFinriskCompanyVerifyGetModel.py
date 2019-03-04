#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountFinriskCompanyVerifyGetModel(object):

    def __init__(self):
        self._app = None
        self._param = None
        self._request_id = None
        self._scene_id = None
        self._tnt_inst_id = None

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, value):
        self._app = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app:
            if hasattr(self.app, 'to_alipay_dict'):
                params['app'] = self.app.to_alipay_dict()
            else:
                params['app'] = self.app
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountFinriskCompanyVerifyGetModel()
        if 'app' in d:
            o.app = d['app']
        if 'param' in d:
            o.param = d['param']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpFinRiskIdentifyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._params = None
        self._request_id = None
        self._risk_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_scene(self):
        return self._risk_scene

    @risk_scene.setter
    def risk_scene(self, value):
        self._risk_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.risk_scene:
            if hasattr(self.risk_scene, 'to_alipay_dict'):
                params['risk_scene'] = self.risk_scene.to_alipay_dict()
            else:
                params['risk_scene'] = self.risk_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpFinRiskIdentifyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'params' in d:
            o.params = d['params']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'risk_scene' in d:
            o.risk_scene = d['risk_scene']
        return o



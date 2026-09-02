#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountAcccoreCetifyQueryModel(object):

    def __init__(self):
        self._alipay_id = None
        self._query_scene = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def query_scene(self):
        return self._query_scene

    @query_scene.setter
    def query_scene(self, value):
        self._query_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.query_scene:
            if hasattr(self.query_scene, 'to_alipay_dict'):
                params['query_scene'] = self.query_scene.to_alipay_dict()
            else:
                params['query_scene'] = self.query_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountAcccoreCetifyQueryModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'query_scene' in d:
            o.query_scene = d['query_scene']
        return o



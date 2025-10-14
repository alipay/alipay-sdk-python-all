#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountAssetlibviewRealtimebalanceQueryModel(object):

    def __init__(self):
        self._asset_alipay_id = None
        self._query_scene = None

    @property
    def asset_alipay_id(self):
        return self._asset_alipay_id

    @asset_alipay_id.setter
    def asset_alipay_id(self, value):
        self._asset_alipay_id = value
    @property
    def query_scene(self):
        return self._query_scene

    @query_scene.setter
    def query_scene(self, value):
        self._query_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_alipay_id:
            if hasattr(self.asset_alipay_id, 'to_alipay_dict'):
                params['asset_alipay_id'] = self.asset_alipay_id.to_alipay_dict()
            else:
                params['asset_alipay_id'] = self.asset_alipay_id
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
        o = AlipayUserAccountAssetlibviewRealtimebalanceQueryModel()
        if 'asset_alipay_id' in d:
            o.asset_alipay_id = d['asset_alipay_id']
        if 'query_scene' in d:
            o.query_scene = d['query_scene']
        return o



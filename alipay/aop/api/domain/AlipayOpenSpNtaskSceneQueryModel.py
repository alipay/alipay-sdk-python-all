#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNtaskSceneQueryModel(object):

    def __init__(self):
        self._batch_query_param = None
        self._query_type = None
        self._scene = None

    @property
    def batch_query_param(self):
        return self._batch_query_param

    @batch_query_param.setter
    def batch_query_param(self, value):
        if isinstance(value, list):
            self._batch_query_param = list()
            for i in value:
                self._batch_query_param.append(i)
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_query_param:
            if isinstance(self.batch_query_param, list):
                for i in range(0, len(self.batch_query_param)):
                    element = self.batch_query_param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batch_query_param[i] = element.to_alipay_dict()
            if hasattr(self.batch_query_param, 'to_alipay_dict'):
                params['batch_query_param'] = self.batch_query_param.to_alipay_dict()
            else:
                params['batch_query_param'] = self.batch_query_param
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNtaskSceneQueryModel()
        if 'batch_query_param' in d:
            o.batch_query_param = d['batch_query_param']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'scene' in d:
            o.scene = d['scene']
        return o



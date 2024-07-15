#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LayerBinding(object):

    def __init__(self):
        self._layer_name = None
        self._layer_version_name = None
        self._sort_score = None

    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version_name(self):
        return self._layer_version_name

    @layer_version_name.setter
    def layer_version_name(self, value):
        self._layer_version_name = value
    @property
    def sort_score(self):
        return self._sort_score

    @sort_score.setter
    def sort_score(self, value):
        self._sort_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.layer_version_name:
            if hasattr(self.layer_version_name, 'to_alipay_dict'):
                params['layer_version_name'] = self.layer_version_name.to_alipay_dict()
            else:
                params['layer_version_name'] = self.layer_version_name
        if self.sort_score:
            if hasattr(self.sort_score, 'to_alipay_dict'):
                params['sort_score'] = self.sort_score.to_alipay_dict()
            else:
                params['sort_score'] = self.sort_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LayerBinding()
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'layer_version_name' in d:
            o.layer_version_name = d['layer_version_name']
        if 'sort_score' in d:
            o.sort_score = d['sort_score']
        return o



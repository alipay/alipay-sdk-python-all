#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryDetailPositionPipelineConfigVO(object):

    def __init__(self):
        self._pipeline_node_config = None
        self._pipeline_node_expressions = None
        self._position_code = None

    @property
    def pipeline_node_config(self):
        return self._pipeline_node_config

    @pipeline_node_config.setter
    def pipeline_node_config(self, value):
        self._pipeline_node_config = value
    @property
    def pipeline_node_expressions(self):
        return self._pipeline_node_expressions

    @pipeline_node_expressions.setter
    def pipeline_node_expressions(self, value):
        self._pipeline_node_expressions = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.pipeline_node_config:
            if hasattr(self.pipeline_node_config, 'to_alipay_dict'):
                params['pipeline_node_config'] = self.pipeline_node_config.to_alipay_dict()
            else:
                params['pipeline_node_config'] = self.pipeline_node_config
        if self.pipeline_node_expressions:
            if hasattr(self.pipeline_node_expressions, 'to_alipay_dict'):
                params['pipeline_node_expressions'] = self.pipeline_node_expressions.to_alipay_dict()
            else:
                params['pipeline_node_expressions'] = self.pipeline_node_expressions
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryDetailPositionPipelineConfigVO()
        if 'pipeline_node_config' in d:
            o.pipeline_node_config = d['pipeline_node_config']
        if 'pipeline_node_expressions' in d:
            o.pipeline_node_expressions = d['pipeline_node_expressions']
        if 'position_code' in d:
            o.position_code = d['position_code']
        return o



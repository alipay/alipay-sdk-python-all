#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiSceneInstanceInfo(object):

    def __init__(self):
        self._external_inst_id = None

    @property
    def external_inst_id(self):
        return self._external_inst_id

    @external_inst_id.setter
    def external_inst_id(self, value):
        self._external_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_inst_id:
            if hasattr(self.external_inst_id, 'to_alipay_dict'):
                params['external_inst_id'] = self.external_inst_id.to_alipay_dict()
            else:
                params['external_inst_id'] = self.external_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSceneInstanceInfo()
        if 'external_inst_id' in d:
            o.external_inst_id = d['external_inst_id']
        return o



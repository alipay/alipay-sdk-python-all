#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnchorInstance(object):

    def __init__(self):
        self._anchor_id = None
        self._anchor_instance_id = None

    @property
    def anchor_id(self):
        return self._anchor_id

    @anchor_id.setter
    def anchor_id(self, value):
        self._anchor_id = value
    @property
    def anchor_instance_id(self):
        return self._anchor_instance_id

    @anchor_instance_id.setter
    def anchor_instance_id(self, value):
        self._anchor_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.anchor_id:
            if hasattr(self.anchor_id, 'to_alipay_dict'):
                params['anchor_id'] = self.anchor_id.to_alipay_dict()
            else:
                params['anchor_id'] = self.anchor_id
        if self.anchor_instance_id:
            if hasattr(self.anchor_instance_id, 'to_alipay_dict'):
                params['anchor_instance_id'] = self.anchor_instance_id.to_alipay_dict()
            else:
                params['anchor_instance_id'] = self.anchor_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnchorInstance()
        if 'anchor_id' in d:
            o.anchor_id = d['anchor_id']
        if 'anchor_instance_id' in d:
            o.anchor_instance_id = d['anchor_instance_id']
        return o



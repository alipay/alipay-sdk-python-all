#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicLifeLabelDeleteModel(object):

    def __init__(self):
        self._label_id = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicLifeLabelDeleteModel()
        if 'label_id' in d:
            o.label_id = d['label_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QualificationConsultInfo(object):

    def __init__(self):
        self._entity_id = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QualificationConsultInfo()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        return o



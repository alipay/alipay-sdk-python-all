#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityservicePolymerSyncSendModel(object):

    def __init__(self):
        self._cud_type = None
        self._entity_content = None
        self._entity_type = None

    @property
    def cud_type(self):
        return self._cud_type

    @cud_type.setter
    def cud_type(self, value):
        self._cud_type = value
    @property
    def entity_content(self):
        return self._entity_content

    @entity_content.setter
    def entity_content(self, value):
        self._entity_content = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cud_type:
            if hasattr(self.cud_type, 'to_alipay_dict'):
                params['cud_type'] = self.cud_type.to_alipay_dict()
            else:
                params['cud_type'] = self.cud_type
        if self.entity_content:
            if hasattr(self.entity_content, 'to_alipay_dict'):
                params['entity_content'] = self.entity_content.to_alipay_dict()
            else:
                params['entity_content'] = self.entity_content
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityservicePolymerSyncSendModel()
        if 'cud_type' in d:
            o.cud_type = d['cud_type']
        if 'entity_content' in d:
            o.entity_content = d['entity_content']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        return o



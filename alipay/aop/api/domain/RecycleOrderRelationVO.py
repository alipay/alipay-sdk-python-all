#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOrderRelationVO(object):

    def __init__(self):
        self._relation_desc = None
        self._relation_id = None
        self._relation_type = None

    @property
    def relation_desc(self):
        return self._relation_desc

    @relation_desc.setter
    def relation_desc(self, value):
        self._relation_desc = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.relation_desc:
            if hasattr(self.relation_desc, 'to_alipay_dict'):
                params['relation_desc'] = self.relation_desc.to_alipay_dict()
            else:
                params['relation_desc'] = self.relation_desc
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOrderRelationVO()
        if 'relation_desc' in d:
            o.relation_desc = d['relation_desc']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        return o



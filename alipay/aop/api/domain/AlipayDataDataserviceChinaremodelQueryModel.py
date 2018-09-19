#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceChinaremodelQueryModel(object):

    def __init__(self):
        self._id = None
        self._rule_id = None
        self._trans_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def trans_id(self):
        return self._trans_id

    @trans_id.setter
    def trans_id(self, value):
        self._trans_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.trans_id:
            if hasattr(self.trans_id, 'to_alipay_dict'):
                params['trans_id'] = self.trans_id.to_alipay_dict()
            else:
                params['trans_id'] = self.trans_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceChinaremodelQueryModel()
        if 'id' in d:
            o.id = d['id']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'trans_id' in d:
            o.trans_id = d['trans_id']
        return o



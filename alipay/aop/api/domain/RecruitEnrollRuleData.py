#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitEnrollRuleData(object):

    def __init__(self):
        self._schema = None

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.schema:
            if hasattr(self.schema, 'to_alipay_dict'):
                params['schema'] = self.schema.to_alipay_dict()
            else:
                params['schema'] = self.schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollRuleData()
        if 'schema' in d:
            o.schema = d['schema']
        return o



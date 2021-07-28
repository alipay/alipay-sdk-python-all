#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityRelationshipExtendField(object):

    def __init__(self):
        self._external_billkey_query_flag = None

    @property
    def external_billkey_query_flag(self):
        return self._external_billkey_query_flag

    @external_billkey_query_flag.setter
    def external_billkey_query_flag(self, value):
        self._external_billkey_query_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_billkey_query_flag:
            if hasattr(self.external_billkey_query_flag, 'to_alipay_dict'):
                params['external_billkey_query_flag'] = self.external_billkey_query_flag.to_alipay_dict()
            else:
                params['external_billkey_query_flag'] = self.external_billkey_query_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityRelationshipExtendField()
        if 'external_billkey_query_flag' in d:
            o.external_billkey_query_flag = d['external_billkey_query_flag']
        return o



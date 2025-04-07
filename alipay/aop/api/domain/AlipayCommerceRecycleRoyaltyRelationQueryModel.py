#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleRoyaltyRelationQueryModel(object):

    def __init__(self):
        self._bind_role_ids = None
        self._bind_role_type = None

    @property
    def bind_role_ids(self):
        return self._bind_role_ids

    @bind_role_ids.setter
    def bind_role_ids(self, value):
        if isinstance(value, list):
            self._bind_role_ids = list()
            for i in value:
                self._bind_role_ids.append(i)
    @property
    def bind_role_type(self):
        return self._bind_role_type

    @bind_role_type.setter
    def bind_role_type(self, value):
        self._bind_role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_role_ids:
            if isinstance(self.bind_role_ids, list):
                for i in range(0, len(self.bind_role_ids)):
                    element = self.bind_role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_role_ids[i] = element.to_alipay_dict()
            if hasattr(self.bind_role_ids, 'to_alipay_dict'):
                params['bind_role_ids'] = self.bind_role_ids.to_alipay_dict()
            else:
                params['bind_role_ids'] = self.bind_role_ids
        if self.bind_role_type:
            if hasattr(self.bind_role_type, 'to_alipay_dict'):
                params['bind_role_type'] = self.bind_role_type.to_alipay_dict()
            else:
                params['bind_role_type'] = self.bind_role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleRoyaltyRelationQueryModel()
        if 'bind_role_ids' in d:
            o.bind_role_ids = d['bind_role_ids']
        if 'bind_role_type' in d:
            o.bind_role_type = d['bind_role_type']
        return o



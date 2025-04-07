#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleRoyaltyRelationVO import RecycleRoyaltyRelationVO


class AlipayCommerceRecycleRoyaltyRelationSaveModel(object):

    def __init__(self):
        self._handle_type = None
        self._relation_list = None

    @property
    def handle_type(self):
        return self._handle_type

    @handle_type.setter
    def handle_type(self, value):
        self._handle_type = value
    @property
    def relation_list(self):
        return self._relation_list

    @relation_list.setter
    def relation_list(self, value):
        if isinstance(value, list):
            self._relation_list = list()
            for i in value:
                if isinstance(i, RecycleRoyaltyRelationVO):
                    self._relation_list.append(i)
                else:
                    self._relation_list.append(RecycleRoyaltyRelationVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.handle_type:
            if hasattr(self.handle_type, 'to_alipay_dict'):
                params['handle_type'] = self.handle_type.to_alipay_dict()
            else:
                params['handle_type'] = self.handle_type
        if self.relation_list:
            if isinstance(self.relation_list, list):
                for i in range(0, len(self.relation_list)):
                    element = self.relation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relation_list[i] = element.to_alipay_dict()
            if hasattr(self.relation_list, 'to_alipay_dict'):
                params['relation_list'] = self.relation_list.to_alipay_dict()
            else:
                params['relation_list'] = self.relation_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleRoyaltyRelationSaveModel()
        if 'handle_type' in d:
            o.handle_type = d['handle_type']
        if 'relation_list' in d:
            o.relation_list = d['relation_list']
        return o



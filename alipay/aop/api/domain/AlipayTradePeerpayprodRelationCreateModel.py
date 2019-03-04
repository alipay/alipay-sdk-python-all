#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradePeerpayprodRelationCreateModel(object):

    def __init__(self):
        self._aliapy_related_id = None
        self._alipay_user_id = None
        self._relation_name = None
        self._relation_type = None
        self._taobao_related_id = None
        self._taobao_user_id = None

    @property
    def aliapy_related_id(self):
        return self._aliapy_related_id

    @aliapy_related_id.setter
    def aliapy_related_id(self, value):
        self._aliapy_related_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def relation_name(self):
        return self._relation_name

    @relation_name.setter
    def relation_name(self, value):
        self._relation_name = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def taobao_related_id(self):
        return self._taobao_related_id

    @taobao_related_id.setter
    def taobao_related_id(self, value):
        self._taobao_related_id = value
    @property
    def taobao_user_id(self):
        return self._taobao_user_id

    @taobao_user_id.setter
    def taobao_user_id(self, value):
        self._taobao_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aliapy_related_id:
            if hasattr(self.aliapy_related_id, 'to_alipay_dict'):
                params['aliapy_related_id'] = self.aliapy_related_id.to_alipay_dict()
            else:
                params['aliapy_related_id'] = self.aliapy_related_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.relation_name:
            if hasattr(self.relation_name, 'to_alipay_dict'):
                params['relation_name'] = self.relation_name.to_alipay_dict()
            else:
                params['relation_name'] = self.relation_name
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.taobao_related_id:
            if hasattr(self.taobao_related_id, 'to_alipay_dict'):
                params['taobao_related_id'] = self.taobao_related_id.to_alipay_dict()
            else:
                params['taobao_related_id'] = self.taobao_related_id
        if self.taobao_user_id:
            if hasattr(self.taobao_user_id, 'to_alipay_dict'):
                params['taobao_user_id'] = self.taobao_user_id.to_alipay_dict()
            else:
                params['taobao_user_id'] = self.taobao_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePeerpayprodRelationCreateModel()
        if 'aliapy_related_id' in d:
            o.aliapy_related_id = d['aliapy_related_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'relation_name' in d:
            o.relation_name = d['relation_name']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'taobao_related_id' in d:
            o.taobao_related_id = d['taobao_related_id']
        if 'taobao_user_id' in d:
            o.taobao_user_id = d['taobao_user_id']
        return o



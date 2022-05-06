#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BPOpenApiAddSignContent import BPOpenApiAddSignContent


class AlipayBossBaseProcessTaskAddsignModel(object):

    def __init__(self):
        self._add_sign_contents = None
        self._memo = None
        self._node = None
        self._operator_id = None
        self._prev = None
        self._puid = None

    @property
    def add_sign_contents(self):
        return self._add_sign_contents

    @add_sign_contents.setter
    def add_sign_contents(self, value):
        if isinstance(value, list):
            self._add_sign_contents = list()
            for i in value:
                if isinstance(i, BPOpenApiAddSignContent):
                    self._add_sign_contents.append(i)
                else:
                    self._add_sign_contents.append(BPOpenApiAddSignContent.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value
    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_sign_contents:
            if isinstance(self.add_sign_contents, list):
                for i in range(0, len(self.add_sign_contents)):
                    element = self.add_sign_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_sign_contents[i] = element.to_alipay_dict()
            if hasattr(self.add_sign_contents, 'to_alipay_dict'):
                params['add_sign_contents'] = self.add_sign_contents.to_alipay_dict()
            else:
                params['add_sign_contents'] = self.add_sign_contents
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.prev:
            if hasattr(self.prev, 'to_alipay_dict'):
                params['prev'] = self.prev.to_alipay_dict()
            else:
                params['prev'] = self.prev
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessTaskAddsignModel()
        if 'add_sign_contents' in d:
            o.add_sign_contents = d['add_sign_contents']
        if 'memo' in d:
            o.memo = d['memo']
        if 'node' in d:
            o.node = d['node']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'prev' in d:
            o.prev = d['prev']
        if 'puid' in d:
            o.puid = d['puid']
        return o



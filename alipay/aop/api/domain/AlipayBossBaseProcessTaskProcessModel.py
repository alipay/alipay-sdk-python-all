#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessTaskProcessModel(object):

    def __init__(self):
        self._context = None
        self._idempotent_id = None
        self._memo = None
        self._node = None
        self._operate = None
        self._operator = None
        self._priority = None
        self._puid = None
        self._sub_contexts = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
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
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value
    @property
    def sub_contexts(self):
        return self._sub_contexts

    @sub_contexts.setter
    def sub_contexts(self, value):
        if isinstance(value, list):
            self._sub_contexts = list()
            for i in value:
                self._sub_contexts.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
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
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        if self.sub_contexts:
            if isinstance(self.sub_contexts, list):
                for i in range(0, len(self.sub_contexts)):
                    element = self.sub_contexts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_contexts[i] = element.to_alipay_dict()
            if hasattr(self.sub_contexts, 'to_alipay_dict'):
                params['sub_contexts'] = self.sub_contexts.to_alipay_dict()
            else:
                params['sub_contexts'] = self.sub_contexts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessTaskProcessModel()
        if 'context' in d:
            o.context = d['context']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'node' in d:
            o.node = d['node']
        if 'operate' in d:
            o.operate = d['operate']
        if 'operator' in d:
            o.operator = d['operator']
        if 'priority' in d:
            o.priority = d['priority']
        if 'puid' in d:
            o.puid = d['puid']
        if 'sub_contexts' in d:
            o.sub_contexts = d['sub_contexts']
        return o



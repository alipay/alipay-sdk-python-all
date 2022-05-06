#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessTaskReleaseModel(object):

    def __init__(self):
        self._memo = None
        self._node = None
        self._operator_id = None
        self._puid = None

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
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayBossBaseProcessTaskReleaseModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'node' in d:
            o.node = d['node']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'puid' in d:
            o.puid = d['puid']
        return o



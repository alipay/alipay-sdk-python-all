#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperateFailRes(object):

    def __init__(self):
        self._id = None
        self._operate_memo = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def operate_memo(self):
        return self._operate_memo

    @operate_memo.setter
    def operate_memo(self, value):
        self._operate_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.operate_memo:
            if hasattr(self.operate_memo, 'to_alipay_dict'):
                params['operate_memo'] = self.operate_memo.to_alipay_dict()
            else:
                params['operate_memo'] = self.operate_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperateFailRes()
        if 'id' in d:
            o.id = d['id']
        if 'operate_memo' in d:
            o.operate_memo = d['operate_memo']
        return o



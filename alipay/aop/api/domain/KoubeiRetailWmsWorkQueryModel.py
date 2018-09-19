#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsWorkQueryModel(object):

    def __init__(self):
        self._operate_context = None
        self._work_id = None

    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsWorkQueryModel()
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'work_id' in d:
            o.work_id = d['work_id']
        return o



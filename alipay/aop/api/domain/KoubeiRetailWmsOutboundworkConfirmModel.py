#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsOutboundworkConfirmModel(object):

    def __init__(self):
        self._operate_context = None
        self._outbound_work_id = None
        self._remark = None

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
    def outbound_work_id(self):
        return self._outbound_work_id

    @outbound_work_id.setter
    def outbound_work_id(self, value):
        self._outbound_work_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.outbound_work_id:
            if hasattr(self.outbound_work_id, 'to_alipay_dict'):
                params['outbound_work_id'] = self.outbound_work_id.to_alipay_dict()
            else:
                params['outbound_work_id'] = self.outbound_work_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsOutboundworkConfirmModel()
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'outbound_work_id' in d:
            o.outbound_work_id = d['outbound_work_id']
        if 'remark' in d:
            o.remark = d['remark']
        return o



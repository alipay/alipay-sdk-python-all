#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsInboundworkConfirmModel(object):

    def __init__(self):
        self._inbound_work_id = None
        self._operate_context = None
        self._remark = None

    @property
    def inbound_work_id(self):
        return self._inbound_work_id

    @inbound_work_id.setter
    def inbound_work_id(self, value):
        self._inbound_work_id = value
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
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.inbound_work_id:
            if hasattr(self.inbound_work_id, 'to_alipay_dict'):
                params['inbound_work_id'] = self.inbound_work_id.to_alipay_dict()
            else:
                params['inbound_work_id'] = self.inbound_work_id
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
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
        o = KoubeiRetailWmsInboundworkConfirmModel()
        if 'inbound_work_id' in d:
            o.inbound_work_id = d['inbound_work_id']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'remark' in d:
            o.remark = d['remark']
        return o



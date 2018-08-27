#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayItemAuditRule import AlipayItemAuditRule
from alipay.aop.api.domain.AlipayItemOperationContext import AlipayItemOperationContext


class AlipayOfflineMarketItemStateModel(object):

    def __init__(self):
        self._audit_rule = None
        self._item_id = None
        self._memo = None
        self._operate_notify_url = None
        self._operation_context = None
        self._request_id = None
        self._state_type = None

    @property
    def audit_rule(self):
        return self._audit_rule

    @audit_rule.setter
    def audit_rule(self, value):
        if isinstance(value, AlipayItemAuditRule):
            self._audit_rule = value
        else:
            self._audit_rule = AlipayItemAuditRule.from_alipay_dict(value)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operate_notify_url(self):
        return self._operate_notify_url

    @operate_notify_url.setter
    def operate_notify_url(self, value):
        self._operate_notify_url = value
    @property
    def operation_context(self):
        return self._operation_context

    @operation_context.setter
    def operation_context(self, value):
        if isinstance(value, AlipayItemOperationContext):
            self._operation_context = value
        else:
            self._operation_context = AlipayItemOperationContext.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def state_type(self):
        return self._state_type

    @state_type.setter
    def state_type(self, value):
        self._state_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_rule:
            if hasattr(self.audit_rule, 'to_alipay_dict'):
                params['audit_rule'] = self.audit_rule.to_alipay_dict()
            else:
                params['audit_rule'] = self.audit_rule
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operate_notify_url:
            if hasattr(self.operate_notify_url, 'to_alipay_dict'):
                params['operate_notify_url'] = self.operate_notify_url.to_alipay_dict()
            else:
                params['operate_notify_url'] = self.operate_notify_url
        if self.operation_context:
            if hasattr(self.operation_context, 'to_alipay_dict'):
                params['operation_context'] = self.operation_context.to_alipay_dict()
            else:
                params['operation_context'] = self.operation_context
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.state_type:
            if hasattr(self.state_type, 'to_alipay_dict'):
                params['state_type'] = self.state_type.to_alipay_dict()
            else:
                params['state_type'] = self.state_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketItemStateModel()
        if 'audit_rule' in d:
            o.audit_rule = d['audit_rule']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operate_notify_url' in d:
            o.operate_notify_url = d['operate_notify_url']
        if 'operation_context' in d:
            o.operation_context = d['operation_context']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'state_type' in d:
            o.state_type = d['state_type']
        return o



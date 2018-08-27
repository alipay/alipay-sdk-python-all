#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KoubeiOperationContext import KoubeiOperationContext


class KoubeiItemStateModel(object):

    def __init__(self):
        self._auth_code = None
        self._item_id = None
        self._memo = None
        self._operation_context = None
        self._request_id = None
        self._state_type = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
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
    def operation_context(self):
        return self._operation_context

    @operation_context.setter
    def operation_context(self, value):
        if isinstance(value, KoubeiOperationContext):
            self._operation_context = value
        else:
            self._operation_context = KoubeiOperationContext.from_alipay_dict(value)
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
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
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
        o = KoubeiItemStateModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operation_context' in d:
            o.operation_context = d['operation_context']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'state_type' in d:
            o.state_type = d['state_type']
        return o



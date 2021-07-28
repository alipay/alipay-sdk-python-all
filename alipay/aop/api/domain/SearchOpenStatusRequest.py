#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchOpenStatusRequest(object):

    def __init__(self):
        self._action = None
        self._apply_type = None
        self._box_id = None
        self._close_reason = None
        self._service_code = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.box_id:
            if hasattr(self.box_id, 'to_alipay_dict'):
                params['box_id'] = self.box_id.to_alipay_dict()
            else:
                params['box_id'] = self.box_id
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOpenStatusRequest()
        if 'action' in d:
            o.action = d['action']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'box_id' in d:
            o.box_id = d['box_id']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o



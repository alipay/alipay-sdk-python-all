#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarCommercializationRefundConfirmModel(object):

    def __init__(self):
        self._async_request_no = None
        self._audit_reason = None
        self._audit_status = None
        self._order_id = None
        self._user_id = None
        self._user_open_id = None

    @property
    def async_request_no(self):
        return self._async_request_no

    @async_request_no.setter
    def async_request_no(self, value):
        self._async_request_no = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_request_no:
            if hasattr(self.async_request_no, 'to_alipay_dict'):
                params['async_request_no'] = self.async_request_no.to_alipay_dict()
            else:
                params['async_request_no'] = self.async_request_no
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCommercializationRefundConfirmModel()
        if 'async_request_no' in d:
            o.async_request_no = d['async_request_no']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarOrdermodifyConfirmModel(object):

    def __init__(self):
        self._confirm_result = None
        self._modified_out_order_no = None
        self._open_id = None
        self._parent_out_order_no = None
        self._reject_reason = None
        self._user_id = None

    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        self._confirm_result = value
    @property
    def modified_out_order_no(self):
        return self._modified_out_order_no

    @modified_out_order_no.setter
    def modified_out_order_no(self, value):
        self._modified_out_order_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def parent_out_order_no(self):
        return self._parent_out_order_no

    @parent_out_order_no.setter
    def parent_out_order_no(self, value):
        self._parent_out_order_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_result:
            if hasattr(self.confirm_result, 'to_alipay_dict'):
                params['confirm_result'] = self.confirm_result.to_alipay_dict()
            else:
                params['confirm_result'] = self.confirm_result
        if self.modified_out_order_no:
            if hasattr(self.modified_out_order_no, 'to_alipay_dict'):
                params['modified_out_order_no'] = self.modified_out_order_no.to_alipay_dict()
            else:
                params['modified_out_order_no'] = self.modified_out_order_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.parent_out_order_no:
            if hasattr(self.parent_out_order_no, 'to_alipay_dict'):
                params['parent_out_order_no'] = self.parent_out_order_no.to_alipay_dict()
            else:
                params['parent_out_order_no'] = self.parent_out_order_no
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarOrdermodifyConfirmModel()
        if 'confirm_result' in d:
            o.confirm_result = d['confirm_result']
        if 'modified_out_order_no' in d:
            o.modified_out_order_no = d['modified_out_order_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'parent_out_order_no' in d:
            o.parent_out_order_no = d['parent_out_order_no']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfImmessageRollbackModel(object):

    def __init__(self):
        self._from_source_id = None
        self._from_source_type = None
        self._method_action = None
        self._msg_id = None
        self._need_distribute = None
        self._to_source_id = None
        self._to_source_type = None
        self._user_id = None

    @property
    def from_source_id(self):
        return self._from_source_id

    @from_source_id.setter
    def from_source_id(self, value):
        self._from_source_id = value
    @property
    def from_source_type(self):
        return self._from_source_type

    @from_source_type.setter
    def from_source_type(self, value):
        self._from_source_type = value
    @property
    def method_action(self):
        return self._method_action

    @method_action.setter
    def method_action(self, value):
        self._method_action = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def need_distribute(self):
        return self._need_distribute

    @need_distribute.setter
    def need_distribute(self, value):
        self._need_distribute = value
    @property
    def to_source_id(self):
        return self._to_source_id

    @to_source_id.setter
    def to_source_id(self, value):
        self._to_source_id = value
    @property
    def to_source_type(self):
        return self._to_source_type

    @to_source_type.setter
    def to_source_type(self, value):
        self._to_source_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_source_id:
            if hasattr(self.from_source_id, 'to_alipay_dict'):
                params['from_source_id'] = self.from_source_id.to_alipay_dict()
            else:
                params['from_source_id'] = self.from_source_id
        if self.from_source_type:
            if hasattr(self.from_source_type, 'to_alipay_dict'):
                params['from_source_type'] = self.from_source_type.to_alipay_dict()
            else:
                params['from_source_type'] = self.from_source_type
        if self.method_action:
            if hasattr(self.method_action, 'to_alipay_dict'):
                params['method_action'] = self.method_action.to_alipay_dict()
            else:
                params['method_action'] = self.method_action
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.need_distribute:
            if hasattr(self.need_distribute, 'to_alipay_dict'):
                params['need_distribute'] = self.need_distribute.to_alipay_dict()
            else:
                params['need_distribute'] = self.need_distribute
        if self.to_source_id:
            if hasattr(self.to_source_id, 'to_alipay_dict'):
                params['to_source_id'] = self.to_source_id.to_alipay_dict()
            else:
                params['to_source_id'] = self.to_source_id
        if self.to_source_type:
            if hasattr(self.to_source_type, 'to_alipay_dict'):
                params['to_source_type'] = self.to_source_type.to_alipay_dict()
            else:
                params['to_source_type'] = self.to_source_type
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
        o = AlipayCommerceMedicalHdfImmessageRollbackModel()
        if 'from_source_id' in d:
            o.from_source_id = d['from_source_id']
        if 'from_source_type' in d:
            o.from_source_type = d['from_source_type']
        if 'method_action' in d:
            o.method_action = d['method_action']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'need_distribute' in d:
            o.need_distribute = d['need_distribute']
        if 'to_source_id' in d:
            o.to_source_id = d['to_source_id']
        if 'to_source_type' in d:
            o.to_source_type = d['to_source_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



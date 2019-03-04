#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasRoleRelationSaveModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._alipay_user_occupied_auto_delete = None
        self._op_type = None
        self._user_id = None
        self._user_occupied_auto_delete = None
        self._user_source = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def alipay_user_occupied_auto_delete(self):
        return self._alipay_user_occupied_auto_delete

    @alipay_user_occupied_auto_delete.setter
    def alipay_user_occupied_auto_delete(self, value):
        self._alipay_user_occupied_auto_delete = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_occupied_auto_delete(self):
        return self._user_occupied_auto_delete

    @user_occupied_auto_delete.setter
    def user_occupied_auto_delete(self, value):
        self._user_occupied_auto_delete = value
    @property
    def user_source(self):
        return self._user_source

    @user_source.setter
    def user_source(self, value):
        self._user_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.alipay_user_occupied_auto_delete:
            if hasattr(self.alipay_user_occupied_auto_delete, 'to_alipay_dict'):
                params['alipay_user_occupied_auto_delete'] = self.alipay_user_occupied_auto_delete.to_alipay_dict()
            else:
                params['alipay_user_occupied_auto_delete'] = self.alipay_user_occupied_auto_delete
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_occupied_auto_delete:
            if hasattr(self.user_occupied_auto_delete, 'to_alipay_dict'):
                params['user_occupied_auto_delete'] = self.user_occupied_auto_delete.to_alipay_dict()
            else:
                params['user_occupied_auto_delete'] = self.user_occupied_auto_delete
        if self.user_source:
            if hasattr(self.user_source, 'to_alipay_dict'):
                params['user_source'] = self.user_source.to_alipay_dict()
            else:
                params['user_source'] = self.user_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntpaasRoleRelationSaveModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'alipay_user_occupied_auto_delete' in d:
            o.alipay_user_occupied_auto_delete = d['alipay_user_occupied_auto_delete']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_occupied_auto_delete' in d:
            o.user_occupied_auto_delete = d['user_occupied_auto_delete']
        if 'user_source' in d:
            o.user_source = d['user_source']
        return o



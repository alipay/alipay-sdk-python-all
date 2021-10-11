#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JointAccountMemberInfoRespDTO(object):

    def __init__(self):
        self._operate_role = None
        self._user_id = None

    @property
    def operate_role(self):
        return self._operate_role

    @operate_role.setter
    def operate_role(self, value):
        self._operate_role = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_role:
            if hasattr(self.operate_role, 'to_alipay_dict'):
                params['operate_role'] = self.operate_role.to_alipay_dict()
            else:
                params['operate_role'] = self.operate_role
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
        o = JointAccountMemberInfoRespDTO()
        if 'operate_role' in d:
            o.operate_role = d['operate_role']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



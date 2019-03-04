#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserPermit(object):

    def __init__(self):
        self._permit_status = None
        self._user_id = None

    @property
    def permit_status(self):
        return self._permit_status

    @permit_status.setter
    def permit_status(self, value):
        self._permit_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.permit_status:
            if hasattr(self.permit_status, 'to_alipay_dict'):
                params['permit_status'] = self.permit_status.to_alipay_dict()
            else:
                params['permit_status'] = self.permit_status
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
        o = UserPermit()
        if 'permit_status' in d:
            o.permit_status = d['permit_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



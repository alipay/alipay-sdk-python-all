#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OuterMemberInfo(object):

    def __init__(self):
        self._user_info = None

    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        self._user_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OuterMemberInfo()
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o



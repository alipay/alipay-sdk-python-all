#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserInfoFromNJ import UserInfoFromNJ


class AlipayCommerceLogisticsNanjingtestQueryModel(object):

    def __init__(self):
        self._user_id = None
        self._user_info = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, UserInfoFromNJ):
            self._user_info = value
        else:
            self._user_info = UserInfoFromNJ.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = AlipayCommerceLogisticsNanjingtestQueryModel()
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o



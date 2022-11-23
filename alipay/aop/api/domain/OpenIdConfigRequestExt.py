#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenIdConfigRequestExt(object):

    def __init__(self):
        self._biz_id = None
        self._biz_type = None
        self._cal_type = None
        self._execute_mode = None
        self._gray_mode = None
        self._gray_ratio = None
        self._gray_users = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cal_type(self):
        return self._cal_type

    @cal_type.setter
    def cal_type(self, value):
        self._cal_type = value
    @property
    def execute_mode(self):
        return self._execute_mode

    @execute_mode.setter
    def execute_mode(self, value):
        self._execute_mode = value
    @property
    def gray_mode(self):
        return self._gray_mode

    @gray_mode.setter
    def gray_mode(self, value):
        self._gray_mode = value
    @property
    def gray_ratio(self):
        return self._gray_ratio

    @gray_ratio.setter
    def gray_ratio(self, value):
        self._gray_ratio = value
    @property
    def gray_users(self):
        return self._gray_users

    @gray_users.setter
    def gray_users(self, value):
        if isinstance(value, list):
            self._gray_users = list()
            for i in value:
                self._gray_users.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cal_type:
            if hasattr(self.cal_type, 'to_alipay_dict'):
                params['cal_type'] = self.cal_type.to_alipay_dict()
            else:
                params['cal_type'] = self.cal_type
        if self.execute_mode:
            if hasattr(self.execute_mode, 'to_alipay_dict'):
                params['execute_mode'] = self.execute_mode.to_alipay_dict()
            else:
                params['execute_mode'] = self.execute_mode
        if self.gray_mode:
            if hasattr(self.gray_mode, 'to_alipay_dict'):
                params['gray_mode'] = self.gray_mode.to_alipay_dict()
            else:
                params['gray_mode'] = self.gray_mode
        if self.gray_ratio:
            if hasattr(self.gray_ratio, 'to_alipay_dict'):
                params['gray_ratio'] = self.gray_ratio.to_alipay_dict()
            else:
                params['gray_ratio'] = self.gray_ratio
        if self.gray_users:
            if isinstance(self.gray_users, list):
                for i in range(0, len(self.gray_users)):
                    element = self.gray_users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gray_users[i] = element.to_alipay_dict()
            if hasattr(self.gray_users, 'to_alipay_dict'):
                params['gray_users'] = self.gray_users.to_alipay_dict()
            else:
                params['gray_users'] = self.gray_users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenIdConfigRequestExt()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cal_type' in d:
            o.cal_type = d['cal_type']
        if 'execute_mode' in d:
            o.execute_mode = d['execute_mode']
        if 'gray_mode' in d:
            o.gray_mode = d['gray_mode']
        if 'gray_ratio' in d:
            o.gray_ratio = d['gray_ratio']
        if 'gray_users' in d:
            o.gray_users = d['gray_users']
        return o



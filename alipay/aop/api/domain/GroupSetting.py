#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupSetting(object):

    def __init__(self):
        self._group_name = None
        self._is_openinv = None
        self._public_notice = None

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def is_openinv(self):
        return self._is_openinv

    @is_openinv.setter
    def is_openinv(self, value):
        self._is_openinv = value
    @property
    def public_notice(self):
        return self._public_notice

    @public_notice.setter
    def public_notice(self, value):
        self._public_notice = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.is_openinv:
            if hasattr(self.is_openinv, 'to_alipay_dict'):
                params['is_openinv'] = self.is_openinv.to_alipay_dict()
            else:
                params['is_openinv'] = self.is_openinv
        if self.public_notice:
            if hasattr(self.public_notice, 'to_alipay_dict'):
                params['public_notice'] = self.public_notice.to_alipay_dict()
            else:
                params['public_notice'] = self.public_notice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupSetting()
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'is_openinv' in d:
            o.is_openinv = d['is_openinv']
        if 'public_notice' in d:
            o.public_notice = d['public_notice']
        return o



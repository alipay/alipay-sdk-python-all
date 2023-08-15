#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseExternalaccountBindCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._open_id = None
        self._prebind_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def prebind_id(self):
        return self._prebind_id

    @prebind_id.setter
    def prebind_id(self, value):
        self._prebind_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.prebind_id:
            if hasattr(self.prebind_id, 'to_alipay_dict'):
                params['prebind_id'] = self.prebind_id.to_alipay_dict()
            else:
                params['prebind_id'] = self.prebind_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseExternalaccountBindCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'prebind_id' in d:
            o.prebind_id = d['prebind_id']
        return o



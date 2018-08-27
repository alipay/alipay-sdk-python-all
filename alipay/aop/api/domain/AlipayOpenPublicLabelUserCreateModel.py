#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicLabelUserCreateModel(object):

    def __init__(self):
        self._label_id = None
        self._user_id = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
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
        o = AlipayOpenPublicLabelUserCreateModel()
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



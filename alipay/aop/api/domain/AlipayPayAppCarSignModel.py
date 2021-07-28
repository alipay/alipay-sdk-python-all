#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppCarSignModel(object):

    def __init__(self):
        self._current_user_id = None

    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_user_id:
            if hasattr(self.current_user_id, 'to_alipay_dict'):
                params['current_user_id'] = self.current_user_id.to_alipay_dict()
            else:
                params['current_user_id'] = self.current_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppCarSignModel()
        if 'current_user_id' in d:
            o.current_user_id = d['current_user_id']
        return o



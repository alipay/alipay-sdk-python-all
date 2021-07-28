#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TbapiQueryAmountBizContent import TbapiQueryAmountBizContent


class AlipayPcreditHuabeiPcreditamountQueryprocessorQueryModel(object):

    def __init__(self):
        self._params = None
        self._user_id = None

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, TbapiQueryAmountBizContent):
            self._params = value
        else:
            self._params = TbapiQueryAmountBizContent.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
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
        o = AlipayPcreditHuabeiPcreditamountQueryprocessorQueryModel()
        if 'params' in d:
            o.params = d['params']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



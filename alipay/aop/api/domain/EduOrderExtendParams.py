#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduOrderExtendParams(object):

    def __init__(self):
        self._bank_memo = None
        self._sys_service_provider_id = None

    @property
    def bank_memo(self):
        return self._bank_memo

    @bank_memo.setter
    def bank_memo(self, value):
        self._bank_memo = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_memo:
            if hasattr(self.bank_memo, 'to_alipay_dict'):
                params['bank_memo'] = self.bank_memo.to_alipay_dict()
            else:
                params['bank_memo'] = self.bank_memo
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduOrderExtendParams()
        if 'bank_memo' in d:
            o.bank_memo = d['bank_memo']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o



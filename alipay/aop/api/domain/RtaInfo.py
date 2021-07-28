#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RtaInfo(object):

    def __init__(self):
        self._account_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RtaInfo()
        if 'account_id' in d:
            o.account_id = d['account_id']
        return o



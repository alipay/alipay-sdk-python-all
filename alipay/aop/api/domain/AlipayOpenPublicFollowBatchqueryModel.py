#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicFollowBatchqueryModel(object):

    def __init__(self):
        self._next_user_id = None

    @property
    def next_user_id(self):
        return self._next_user_id

    @next_user_id.setter
    def next_user_id(self, value):
        self._next_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.next_user_id:
            if hasattr(self.next_user_id, 'to_alipay_dict'):
                params['next_user_id'] = self.next_user_id.to_alipay_dict()
            else:
                params['next_user_id'] = self.next_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicFollowBatchqueryModel()
        if 'next_user_id' in d:
            o.next_user_id = d['next_user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleInfoForm(object):

    def __init__(self):
        self._recycle_memo = None
        self._recycle_user_id = None

    @property
    def recycle_memo(self):
        return self._recycle_memo

    @recycle_memo.setter
    def recycle_memo(self, value):
        self._recycle_memo = value
    @property
    def recycle_user_id(self):
        return self._recycle_user_id

    @recycle_user_id.setter
    def recycle_user_id(self, value):
        self._recycle_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.recycle_memo:
            if hasattr(self.recycle_memo, 'to_alipay_dict'):
                params['recycle_memo'] = self.recycle_memo.to_alipay_dict()
            else:
                params['recycle_memo'] = self.recycle_memo
        if self.recycle_user_id:
            if hasattr(self.recycle_user_id, 'to_alipay_dict'):
                params['recycle_user_id'] = self.recycle_user_id.to_alipay_dict()
            else:
                params['recycle_user_id'] = self.recycle_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInfoForm()
        if 'recycle_memo' in d:
            o.recycle_memo = d['recycle_memo']
        if 'recycle_user_id' in d:
            o.recycle_user_id = d['recycle_user_id']
        return o



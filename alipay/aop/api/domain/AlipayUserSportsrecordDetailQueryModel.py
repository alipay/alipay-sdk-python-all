#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSportsrecordDetailQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._out_biz_code = None
        self._record_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, value):
        self._out_biz_code = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_code:
            if hasattr(self.out_biz_code, 'to_alipay_dict'):
                params['out_biz_code'] = self.out_biz_code.to_alipay_dict()
            else:
                params['out_biz_code'] = self.out_biz_code
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
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
        o = AlipayUserSportsrecordDetailQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_code' in d:
            o.out_biz_code = d['out_biz_code']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



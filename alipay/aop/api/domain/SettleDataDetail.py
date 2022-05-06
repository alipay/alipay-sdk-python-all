#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleDataDetail(object):

    def __init__(self):
        self._data_detail = None
        self._user_id = None

    @property
    def data_detail(self):
        return self._data_detail

    @data_detail.setter
    def data_detail(self, value):
        self._data_detail = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_detail:
            if hasattr(self.data_detail, 'to_alipay_dict'):
                params['data_detail'] = self.data_detail.to_alipay_dict()
            else:
                params['data_detail'] = self.data_detail
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
        o = SettleDataDetail()
        if 'data_detail' in d:
            o.data_detail = d['data_detail']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



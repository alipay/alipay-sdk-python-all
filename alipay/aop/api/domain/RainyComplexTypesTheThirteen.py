#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesTheThirteen(object):

    def __init__(self):
        self._open_id = None
        self._open_ids = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_ids(self):
        return self._open_ids

    @open_ids.setter
    def open_ids(self, value):
        if isinstance(value, list):
            self._open_ids = list()
            for i in value:
                self._open_ids.append(i)
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
        if self.open_ids:
            if isinstance(self.open_ids, list):
                for i in range(0, len(self.open_ids)):
                    element = self.open_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_ids[i] = element.to_alipay_dict()
            if hasattr(self.open_ids, 'to_alipay_dict'):
                params['open_ids'] = self.open_ids.to_alipay_dict()
            else:
                params['open_ids'] = self.open_ids
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
        o = RainyComplexTypesTheThirteen()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_ids' in d:
            o.open_ids = d['open_ids']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



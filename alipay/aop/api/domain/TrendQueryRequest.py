#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrendQueryRequest(object):

    def __init__(self):
        self._dim = None
        self._end_date = None
        self._exclude_import = None
        self._relation_type = None
        self._start_date = None
        self._user_key = None

    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, value):
        self._dim = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def exclude_import(self):
        return self._exclude_import

    @exclude_import.setter
    def exclude_import(self, value):
        self._exclude_import = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def user_key(self):
        return self._user_key

    @user_key.setter
    def user_key(self, value):
        self._user_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.dim:
            if hasattr(self.dim, 'to_alipay_dict'):
                params['dim'] = self.dim.to_alipay_dict()
            else:
                params['dim'] = self.dim
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.exclude_import:
            if hasattr(self.exclude_import, 'to_alipay_dict'):
                params['exclude_import'] = self.exclude_import.to_alipay_dict()
            else:
                params['exclude_import'] = self.exclude_import
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.user_key:
            if hasattr(self.user_key, 'to_alipay_dict'):
                params['user_key'] = self.user_key.to_alipay_dict()
            else:
                params['user_key'] = self.user_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrendQueryRequest()
        if 'dim' in d:
            o.dim = d['dim']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'exclude_import' in d:
            o.exclude_import = d['exclude_import']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'user_key' in d:
            o.user_key = d['user_key']
        return o



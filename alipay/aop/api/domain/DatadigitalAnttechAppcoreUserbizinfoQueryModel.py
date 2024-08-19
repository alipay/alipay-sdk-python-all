#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechAppcoreUserbizinfoQueryModel(object):

    def __init__(self):
        self._company_uscc = None
        self._open_id = None
        self._phone_number = None
        self._query_type = None
        self._resident_id = None
        self._user_id = None

    @property
    def company_uscc(self):
        return self._company_uscc

    @company_uscc.setter
    def company_uscc(self, value):
        self._company_uscc = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def resident_id(self):
        return self._resident_id

    @resident_id.setter
    def resident_id(self, value):
        self._resident_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_uscc:
            if hasattr(self.company_uscc, 'to_alipay_dict'):
                params['company_uscc'] = self.company_uscc.to_alipay_dict()
            else:
                params['company_uscc'] = self.company_uscc
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.resident_id:
            if hasattr(self.resident_id, 'to_alipay_dict'):
                params['resident_id'] = self.resident_id.to_alipay_dict()
            else:
                params['resident_id'] = self.resident_id
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
        o = DatadigitalAnttechAppcoreUserbizinfoQueryModel()
        if 'company_uscc' in d:
            o.company_uscc = d['company_uscc']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'resident_id' in d:
            o.resident_id = d['resident_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



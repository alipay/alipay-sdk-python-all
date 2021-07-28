#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Org(object):

    def __init__(self):
        self._org_id_number = None
        self._org_id_type = None
        self._org_legal_id_number = None
        self._org_legal_id_type = None
        self._org_legal_name = None
        self._org_name = None
        self._third_party_user_id = None

    @property
    def org_id_number(self):
        return self._org_id_number

    @org_id_number.setter
    def org_id_number(self, value):
        self._org_id_number = value
    @property
    def org_id_type(self):
        return self._org_id_type

    @org_id_type.setter
    def org_id_type(self, value):
        self._org_id_type = value
    @property
    def org_legal_id_number(self):
        return self._org_legal_id_number

    @org_legal_id_number.setter
    def org_legal_id_number(self, value):
        self._org_legal_id_number = value
    @property
    def org_legal_id_type(self):
        return self._org_legal_id_type

    @org_legal_id_type.setter
    def org_legal_id_type(self, value):
        self._org_legal_id_type = value
    @property
    def org_legal_name(self):
        return self._org_legal_name

    @org_legal_name.setter
    def org_legal_name(self, value):
        self._org_legal_name = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def third_party_user_id(self):
        return self._third_party_user_id

    @third_party_user_id.setter
    def third_party_user_id(self, value):
        self._third_party_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_id_number:
            if hasattr(self.org_id_number, 'to_alipay_dict'):
                params['org_id_number'] = self.org_id_number.to_alipay_dict()
            else:
                params['org_id_number'] = self.org_id_number
        if self.org_id_type:
            if hasattr(self.org_id_type, 'to_alipay_dict'):
                params['org_id_type'] = self.org_id_type.to_alipay_dict()
            else:
                params['org_id_type'] = self.org_id_type
        if self.org_legal_id_number:
            if hasattr(self.org_legal_id_number, 'to_alipay_dict'):
                params['org_legal_id_number'] = self.org_legal_id_number.to_alipay_dict()
            else:
                params['org_legal_id_number'] = self.org_legal_id_number
        if self.org_legal_id_type:
            if hasattr(self.org_legal_id_type, 'to_alipay_dict'):
                params['org_legal_id_type'] = self.org_legal_id_type.to_alipay_dict()
            else:
                params['org_legal_id_type'] = self.org_legal_id_type
        if self.org_legal_name:
            if hasattr(self.org_legal_name, 'to_alipay_dict'):
                params['org_legal_name'] = self.org_legal_name.to_alipay_dict()
            else:
                params['org_legal_name'] = self.org_legal_name
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.third_party_user_id:
            if hasattr(self.third_party_user_id, 'to_alipay_dict'):
                params['third_party_user_id'] = self.third_party_user_id.to_alipay_dict()
            else:
                params['third_party_user_id'] = self.third_party_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Org()
        if 'org_id_number' in d:
            o.org_id_number = d['org_id_number']
        if 'org_id_type' in d:
            o.org_id_type = d['org_id_type']
        if 'org_legal_id_number' in d:
            o.org_legal_id_number = d['org_legal_id_number']
        if 'org_legal_id_type' in d:
            o.org_legal_id_type = d['org_legal_id_type']
        if 'org_legal_name' in d:
            o.org_legal_name = d['org_legal_name']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'third_party_user_id' in d:
            o.third_party_user_id = d['third_party_user_id']
        return o



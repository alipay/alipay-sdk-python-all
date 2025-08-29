#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuranceUserInformation(object):

    def __init__(self):
        self._binded_mobile = None
        self._cert_no = None
        self._cert_no_flag = None
        self._cert_type = None
        self._open_id = None
        self._relation_type = None
        self._user_id = None
        self._user_name = None

    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_no_flag(self):
        return self._cert_no_flag

    @cert_no_flag.setter
    def cert_no_flag(self, value):
        self._cert_no_flag = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.binded_mobile:
            if hasattr(self.binded_mobile, 'to_alipay_dict'):
                params['binded_mobile'] = self.binded_mobile.to_alipay_dict()
            else:
                params['binded_mobile'] = self.binded_mobile
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_no_flag:
            if hasattr(self.cert_no_flag, 'to_alipay_dict'):
                params['cert_no_flag'] = self.cert_no_flag.to_alipay_dict()
            else:
                params['cert_no_flag'] = self.cert_no_flag
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuranceUserInformation()
        if 'binded_mobile' in d:
            o.binded_mobile = d['binded_mobile']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_no_flag' in d:
            o.cert_no_flag = d['cert_no_flag']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



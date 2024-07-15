#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FmBindFmVO(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._gender = None
        self._nick_name = None
        self._relation_type = None
        self._user_real_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def user_real_name(self):
        return self._user_real_name

    @user_real_name.setter
    def user_real_name(self, value):
        self._user_real_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.user_real_name:
            if hasattr(self.user_real_name, 'to_alipay_dict'):
                params['user_real_name'] = self.user_real_name.to_alipay_dict()
            else:
                params['user_real_name'] = self.user_real_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FmBindFmVO()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'user_real_name' in d:
            o.user_real_name = d['user_real_name']
        return o



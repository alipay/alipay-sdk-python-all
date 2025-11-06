#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuredVO(object):

    def __init__(self):
        self._birthday = None
        self._cert_no = None
        self._cert_type = None
        self._gender = None
        self._name = None
        self._phone_no = None
        self._relation_to_ph = None
        self._sub_order_no = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def relation_to_ph(self):
        return self._relation_to_ph

    @relation_to_ph.setter
    def relation_to_ph(self, value):
        self._relation_to_ph = value
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.relation_to_ph:
            if hasattr(self.relation_to_ph, 'to_alipay_dict'):
                params['relation_to_ph'] = self.relation_to_ph.to_alipay_dict()
            else:
                params['relation_to_ph'] = self.relation_to_ph
        if self.sub_order_no:
            if hasattr(self.sub_order_no, 'to_alipay_dict'):
                params['sub_order_no'] = self.sub_order_no.to_alipay_dict()
            else:
                params['sub_order_no'] = self.sub_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuredVO()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'name' in d:
            o.name = d['name']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'relation_to_ph' in d:
            o.relation_to_ph = d['relation_to_ph']
        if 'sub_order_no' in d:
            o.sub_order_no = d['sub_order_no']
        return o



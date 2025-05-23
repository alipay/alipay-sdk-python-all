#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlimamaPrincipalExtendInfo(object):

    def __init__(self):
        self._principal_define_name = None
        self._second_email = None
        self._second_oid = None
        self._seller_id = None
        self._store_id = None
        self._store_name = None
        self._store_type = None

    @property
    def principal_define_name(self):
        return self._principal_define_name

    @principal_define_name.setter
    def principal_define_name(self, value):
        self._principal_define_name = value
    @property
    def second_email(self):
        return self._second_email

    @second_email.setter
    def second_email(self, value):
        self._second_email = value
    @property
    def second_oid(self):
        return self._second_oid

    @second_oid.setter
    def second_oid(self, value):
        self._second_oid = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_type(self):
        return self._store_type

    @store_type.setter
    def store_type(self, value):
        self._store_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.principal_define_name:
            if hasattr(self.principal_define_name, 'to_alipay_dict'):
                params['principal_define_name'] = self.principal_define_name.to_alipay_dict()
            else:
                params['principal_define_name'] = self.principal_define_name
        if self.second_email:
            if hasattr(self.second_email, 'to_alipay_dict'):
                params['second_email'] = self.second_email.to_alipay_dict()
            else:
                params['second_email'] = self.second_email
        if self.second_oid:
            if hasattr(self.second_oid, 'to_alipay_dict'):
                params['second_oid'] = self.second_oid.to_alipay_dict()
            else:
                params['second_oid'] = self.second_oid
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_type:
            if hasattr(self.store_type, 'to_alipay_dict'):
                params['store_type'] = self.store_type.to_alipay_dict()
            else:
                params['store_type'] = self.store_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlimamaPrincipalExtendInfo()
        if 'principal_define_name' in d:
            o.principal_define_name = d['principal_define_name']
        if 'second_email' in d:
            o.second_email = d['second_email']
        if 'second_oid' in d:
            o.second_oid = d['second_oid']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_type' in d:
            o.store_type = d['store_type']
        return o



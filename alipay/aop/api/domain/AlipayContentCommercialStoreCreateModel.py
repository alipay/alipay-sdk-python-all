#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialStoreCreateModel(object):

    def __init__(self):
        self._access_code = None
        self._access_model = None
        self._name = None
        self._owner_oid = None
        self._owner_pid = None
        self._owner_type = None
        self._public_id = None
        self._store_biz_id = None
        self._sub_type = None
        self._type = None

    @property
    def access_code(self):
        return self._access_code

    @access_code.setter
    def access_code(self, value):
        self._access_code = value
    @property
    def access_model(self):
        return self._access_model

    @access_model.setter
    def access_model(self, value):
        self._access_model = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def owner_oid(self):
        return self._owner_oid

    @owner_oid.setter
    def owner_oid(self, value):
        self._owner_oid = value
    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def store_biz_id(self):
        return self._store_biz_id

    @store_biz_id.setter
    def store_biz_id(self, value):
        self._store_biz_id = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_code:
            if hasattr(self.access_code, 'to_alipay_dict'):
                params['access_code'] = self.access_code.to_alipay_dict()
            else:
                params['access_code'] = self.access_code
        if self.access_model:
            if hasattr(self.access_model, 'to_alipay_dict'):
                params['access_model'] = self.access_model.to_alipay_dict()
            else:
                params['access_model'] = self.access_model
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.owner_oid:
            if hasattr(self.owner_oid, 'to_alipay_dict'):
                params['owner_oid'] = self.owner_oid.to_alipay_dict()
            else:
                params['owner_oid'] = self.owner_oid
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.store_biz_id:
            if hasattr(self.store_biz_id, 'to_alipay_dict'):
                params['store_biz_id'] = self.store_biz_id.to_alipay_dict()
            else:
                params['store_biz_id'] = self.store_biz_id
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialStoreCreateModel()
        if 'access_code' in d:
            o.access_code = d['access_code']
        if 'access_model' in d:
            o.access_model = d['access_model']
        if 'name' in d:
            o.name = d['name']
        if 'owner_oid' in d:
            o.owner_oid = d['owner_oid']
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'store_biz_id' in d:
            o.store_biz_id = d['store_biz_id']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'type' in d:
            o.type = d['type']
        return o



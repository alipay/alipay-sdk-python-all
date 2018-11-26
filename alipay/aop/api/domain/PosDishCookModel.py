#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosDishCookModel(object):

    def __init__(self):
        self._cook_channel = None
        self._cook_id = None
        self._cook_name = None
        self._create_user = None
        self._gmt_create = None
        self._gmt_modified = None
        self._merchant_id = None
        self._remarks = None
        self._shop_id = None
        self._source_from = None
        self._status = None

    @property
    def cook_channel(self):
        return self._cook_channel

    @cook_channel.setter
    def cook_channel(self, value):
        self._cook_channel = value
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def cook_name(self):
        return self._cook_name

    @cook_name.setter
    def cook_name(self, value):
        self._cook_name = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_from(self):
        return self._source_from

    @source_from.setter
    def source_from(self, value):
        self._source_from = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_channel:
            if hasattr(self.cook_channel, 'to_alipay_dict'):
                params['cook_channel'] = self.cook_channel.to_alipay_dict()
            else:
                params['cook_channel'] = self.cook_channel
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.cook_name:
            if hasattr(self.cook_name, 'to_alipay_dict'):
                params['cook_name'] = self.cook_name.to_alipay_dict()
            else:
                params['cook_name'] = self.cook_name
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_from:
            if hasattr(self.source_from, 'to_alipay_dict'):
                params['source_from'] = self.source_from.to_alipay_dict()
            else:
                params['source_from'] = self.source_from
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDishCookModel()
        if 'cook_channel' in d:
            o.cook_channel = d['cook_channel']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'cook_name' in d:
            o.cook_name = d['cook_name']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_from' in d:
            o.source_from = d['source_from']
        if 'status' in d:
            o.status = d['status']
        return o



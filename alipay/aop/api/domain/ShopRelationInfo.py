#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopRelationInfo(object):

    def __init__(self):
        self._credit_code = None
        self._ent_id = None
        self._ent_name = None
        self._platform_id = None
        self._platform_name = None
        self._platform_type_code = None
        self._reg_no = None
        self._rel_type_code = None
        self._shop_id = None
        self._shop_name = None
        self._shop_status = None
        self._shop_type = None

    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_id(self):
        return self._ent_id

    @ent_id.setter
    def ent_id(self, value):
        self._ent_id = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def platform_name(self):
        return self._platform_name

    @platform_name.setter
    def platform_name(self, value):
        self._platform_name = value
    @property
    def platform_type_code(self):
        return self._platform_type_code

    @platform_type_code.setter
    def platform_type_code(self, value):
        self._platform_type_code = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def rel_type_code(self):
        return self._rel_type_code

    @rel_type_code.setter
    def rel_type_code(self, value):
        self._rel_type_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.ent_id:
            if hasattr(self.ent_id, 'to_alipay_dict'):
                params['ent_id'] = self.ent_id.to_alipay_dict()
            else:
                params['ent_id'] = self.ent_id
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        if self.platform_name:
            if hasattr(self.platform_name, 'to_alipay_dict'):
                params['platform_name'] = self.platform_name.to_alipay_dict()
            else:
                params['platform_name'] = self.platform_name
        if self.platform_type_code:
            if hasattr(self.platform_type_code, 'to_alipay_dict'):
                params['platform_type_code'] = self.platform_type_code.to_alipay_dict()
            else:
                params['platform_type_code'] = self.platform_type_code
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.rel_type_code:
            if hasattr(self.rel_type_code, 'to_alipay_dict'):
                params['rel_type_code'] = self.rel_type_code.to_alipay_dict()
            else:
                params['rel_type_code'] = self.rel_type_code
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopRelationInfo()
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'ent_id' in d:
            o.ent_id = d['ent_id']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'platform_name' in d:
            o.platform_name = d['platform_name']
        if 'platform_type_code' in d:
            o.platform_type_code = d['platform_type_code']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'rel_type_code' in d:
            o.rel_type_code = d['rel_type_code']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        return o



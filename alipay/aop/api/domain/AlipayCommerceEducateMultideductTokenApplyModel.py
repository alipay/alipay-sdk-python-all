#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayConfig import PayConfig


class AlipayCommerceEducateMultideductTokenApplyModel(object):

    def __init__(self):
        self._biz_code = None
        self._operation_type = None
        self._parent_phone = None
        self._pay_config = None
        self._query_asset = None
        self._school_code = None
        self._user_cert_no = None
        self._user_cert_type = None
        self._user_name = None
        self._user_unique_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def parent_phone(self):
        return self._parent_phone

    @parent_phone.setter
    def parent_phone(self, value):
        self._parent_phone = value
    @property
    def pay_config(self):
        return self._pay_config

    @pay_config.setter
    def pay_config(self, value):
        if isinstance(value, PayConfig):
            self._pay_config = value
        else:
            self._pay_config = PayConfig.from_alipay_dict(value)
    @property
    def query_asset(self):
        return self._query_asset

    @query_asset.setter
    def query_asset(self, value):
        self._query_asset = value
    @property
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_unique_id(self):
        return self._user_unique_id

    @user_unique_id.setter
    def user_unique_id(self, value):
        self._user_unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.parent_phone:
            if hasattr(self.parent_phone, 'to_alipay_dict'):
                params['parent_phone'] = self.parent_phone.to_alipay_dict()
            else:
                params['parent_phone'] = self.parent_phone
        if self.pay_config:
            if hasattr(self.pay_config, 'to_alipay_dict'):
                params['pay_config'] = self.pay_config.to_alipay_dict()
            else:
                params['pay_config'] = self.pay_config
        if self.query_asset:
            if hasattr(self.query_asset, 'to_alipay_dict'):
                params['query_asset'] = self.query_asset.to_alipay_dict()
            else:
                params['query_asset'] = self.query_asset
        if self.school_code:
            if hasattr(self.school_code, 'to_alipay_dict'):
                params['school_code'] = self.school_code.to_alipay_dict()
            else:
                params['school_code'] = self.school_code
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_unique_id:
            if hasattr(self.user_unique_id, 'to_alipay_dict'):
                params['user_unique_id'] = self.user_unique_id.to_alipay_dict()
            else:
                params['user_unique_id'] = self.user_unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateMultideductTokenApplyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'parent_phone' in d:
            o.parent_phone = d['parent_phone']
        if 'pay_config' in d:
            o.pay_config = d['pay_config']
        if 'query_asset' in d:
            o.query_asset = d['query_asset']
        if 'school_code' in d:
            o.school_code = d['school_code']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_unique_id' in d:
            o.user_unique_id = d['user_unique_id']
        return o



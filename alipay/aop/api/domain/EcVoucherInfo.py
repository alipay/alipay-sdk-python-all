#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcVoucherInfo(object):

    def __init__(self):
        self._account_id = None
        self._employee_id = None
        self._enterprise_id = None
        self._open_id = None
        self._user_id = None
        self._voucher_content = None
        self._voucher_date = None
        self._voucher_id = None
        self._voucher_source = None
        self._voucher_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_content(self):
        return self._voucher_content

    @voucher_content.setter
    def voucher_content(self, value):
        self._voucher_content = value
    @property
    def voucher_date(self):
        return self._voucher_date

    @voucher_date.setter
    def voucher_date(self, value):
        self._voucher_date = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_source(self):
        return self._voucher_source

    @voucher_source.setter
    def voucher_source(self, value):
        self._voucher_source = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_content:
            if hasattr(self.voucher_content, 'to_alipay_dict'):
                params['voucher_content'] = self.voucher_content.to_alipay_dict()
            else:
                params['voucher_content'] = self.voucher_content
        if self.voucher_date:
            if hasattr(self.voucher_date, 'to_alipay_dict'):
                params['voucher_date'] = self.voucher_date.to_alipay_dict()
            else:
                params['voucher_date'] = self.voucher_date
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_source:
            if hasattr(self.voucher_source, 'to_alipay_dict'):
                params['voucher_source'] = self.voucher_source.to_alipay_dict()
            else:
                params['voucher_source'] = self.voucher_source
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcVoucherInfo()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_content' in d:
            o.voucher_content = d['voucher_content']
        if 'voucher_date' in d:
            o.voucher_date = d['voucher_date']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_source' in d:
            o.voucher_source = d['voucher_source']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o



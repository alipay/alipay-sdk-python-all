#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class WriteOffLeftRightDetailOpenApiDTO(object):

    def __init__(self):
        self._inst_id = None
        self._ip_role_id = None
        self._left_apply_write_off_amt = None
        self._left_bill_no = None
        self._left_write_off_bill_type = None
        self._right_apply_write_off_amt = None
        self._right_bill_no = None
        self._right_write_off_bill_type = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def left_apply_write_off_amt(self):
        return self._left_apply_write_off_amt

    @left_apply_write_off_amt.setter
    def left_apply_write_off_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._left_apply_write_off_amt = value
        else:
            self._left_apply_write_off_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def left_bill_no(self):
        return self._left_bill_no

    @left_bill_no.setter
    def left_bill_no(self, value):
        self._left_bill_no = value
    @property
    def left_write_off_bill_type(self):
        return self._left_write_off_bill_type

    @left_write_off_bill_type.setter
    def left_write_off_bill_type(self, value):
        self._left_write_off_bill_type = value
    @property
    def right_apply_write_off_amt(self):
        return self._right_apply_write_off_amt

    @right_apply_write_off_amt.setter
    def right_apply_write_off_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._right_apply_write_off_amt = value
        else:
            self._right_apply_write_off_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def right_bill_no(self):
        return self._right_bill_no

    @right_bill_no.setter
    def right_bill_no(self, value):
        self._right_bill_no = value
    @property
    def right_write_off_bill_type(self):
        return self._right_write_off_bill_type

    @right_write_off_bill_type.setter
    def right_write_off_bill_type(self, value):
        self._right_write_off_bill_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.left_apply_write_off_amt:
            if hasattr(self.left_apply_write_off_amt, 'to_alipay_dict'):
                params['left_apply_write_off_amt'] = self.left_apply_write_off_amt.to_alipay_dict()
            else:
                params['left_apply_write_off_amt'] = self.left_apply_write_off_amt
        if self.left_bill_no:
            if hasattr(self.left_bill_no, 'to_alipay_dict'):
                params['left_bill_no'] = self.left_bill_no.to_alipay_dict()
            else:
                params['left_bill_no'] = self.left_bill_no
        if self.left_write_off_bill_type:
            if hasattr(self.left_write_off_bill_type, 'to_alipay_dict'):
                params['left_write_off_bill_type'] = self.left_write_off_bill_type.to_alipay_dict()
            else:
                params['left_write_off_bill_type'] = self.left_write_off_bill_type
        if self.right_apply_write_off_amt:
            if hasattr(self.right_apply_write_off_amt, 'to_alipay_dict'):
                params['right_apply_write_off_amt'] = self.right_apply_write_off_amt.to_alipay_dict()
            else:
                params['right_apply_write_off_amt'] = self.right_apply_write_off_amt
        if self.right_bill_no:
            if hasattr(self.right_bill_no, 'to_alipay_dict'):
                params['right_bill_no'] = self.right_bill_no.to_alipay_dict()
            else:
                params['right_bill_no'] = self.right_bill_no
        if self.right_write_off_bill_type:
            if hasattr(self.right_write_off_bill_type, 'to_alipay_dict'):
                params['right_write_off_bill_type'] = self.right_write_off_bill_type.to_alipay_dict()
            else:
                params['right_write_off_bill_type'] = self.right_write_off_bill_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WriteOffLeftRightDetailOpenApiDTO()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'left_apply_write_off_amt' in d:
            o.left_apply_write_off_amt = d['left_apply_write_off_amt']
        if 'left_bill_no' in d:
            o.left_bill_no = d['left_bill_no']
        if 'left_write_off_bill_type' in d:
            o.left_write_off_bill_type = d['left_write_off_bill_type']
        if 'right_apply_write_off_amt' in d:
            o.right_apply_write_off_amt = d['right_apply_write_off_amt']
        if 'right_bill_no' in d:
            o.right_bill_no = d['right_bill_no']
        if 'right_write_off_bill_type' in d:
            o.right_write_off_bill_type = d['right_write_off_bill_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillSendExtInfo(object):

    def __init__(self):
        self._ext_school_id = None
        self._order_pay_type = None
        self._royalty_amount = None
        self._school_name = None
        self._trans_in_pid = None

    @property
    def ext_school_id(self):
        return self._ext_school_id

    @ext_school_id.setter
    def ext_school_id(self, value):
        self._ext_school_id = value
    @property
    def order_pay_type(self):
        return self._order_pay_type

    @order_pay_type.setter
    def order_pay_type(self, value):
        self._order_pay_type = value
    @property
    def royalty_amount(self):
        return self._royalty_amount

    @royalty_amount.setter
    def royalty_amount(self, value):
        self._royalty_amount = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def trans_in_pid(self):
        return self._trans_in_pid

    @trans_in_pid.setter
    def trans_in_pid(self, value):
        self._trans_in_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_school_id:
            if hasattr(self.ext_school_id, 'to_alipay_dict'):
                params['ext_school_id'] = self.ext_school_id.to_alipay_dict()
            else:
                params['ext_school_id'] = self.ext_school_id
        if self.order_pay_type:
            if hasattr(self.order_pay_type, 'to_alipay_dict'):
                params['order_pay_type'] = self.order_pay_type.to_alipay_dict()
            else:
                params['order_pay_type'] = self.order_pay_type
        if self.royalty_amount:
            if hasattr(self.royalty_amount, 'to_alipay_dict'):
                params['royalty_amount'] = self.royalty_amount.to_alipay_dict()
            else:
                params['royalty_amount'] = self.royalty_amount
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.trans_in_pid:
            if hasattr(self.trans_in_pid, 'to_alipay_dict'):
                params['trans_in_pid'] = self.trans_in_pid.to_alipay_dict()
            else:
                params['trans_in_pid'] = self.trans_in_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillSendExtInfo()
        if 'ext_school_id' in d:
            o.ext_school_id = d['ext_school_id']
        if 'order_pay_type' in d:
            o.order_pay_type = d['order_pay_type']
        if 'royalty_amount' in d:
            o.royalty_amount = d['royalty_amount']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'trans_in_pid' in d:
            o.trans_in_pid = d['trans_in_pid']
        return o



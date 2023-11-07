#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceFeeExtInfo import ServiceFeeExtInfo


class ServiceFeeInfo(object):

    def __init__(self):
        self._amount = None
        self._bill_no = None
        self._bill_type = None
        self._execute_dt = None
        self._ext_info = None
        self._pay_no = None
        self._related_bill_no = None
        self._trans_in_open_id = None
        self._trans_in_user_id = None
        self._trans_in_user_name = None
        self._trans_out_open_id = None
        self._trans_out_user_id = None
        self._trans_out_user_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def execute_dt(self):
        return self._execute_dt

    @execute_dt.setter
    def execute_dt(self, value):
        self._execute_dt = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ServiceFeeExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ServiceFeeExtInfo.from_alipay_dict(value)
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def related_bill_no(self):
        return self._related_bill_no

    @related_bill_no.setter
    def related_bill_no(self, value):
        self._related_bill_no = value
    @property
    def trans_in_open_id(self):
        return self._trans_in_open_id

    @trans_in_open_id.setter
    def trans_in_open_id(self, value):
        self._trans_in_open_id = value
    @property
    def trans_in_user_id(self):
        return self._trans_in_user_id

    @trans_in_user_id.setter
    def trans_in_user_id(self, value):
        self._trans_in_user_id = value
    @property
    def trans_in_user_name(self):
        return self._trans_in_user_name

    @trans_in_user_name.setter
    def trans_in_user_name(self, value):
        self._trans_in_user_name = value
    @property
    def trans_out_open_id(self):
        return self._trans_out_open_id

    @trans_out_open_id.setter
    def trans_out_open_id(self, value):
        self._trans_out_open_id = value
    @property
    def trans_out_user_id(self):
        return self._trans_out_user_id

    @trans_out_user_id.setter
    def trans_out_user_id(self, value):
        self._trans_out_user_id = value
    @property
    def trans_out_user_name(self):
        return self._trans_out_user_name

    @trans_out_user_name.setter
    def trans_out_user_name(self, value):
        self._trans_out_user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.execute_dt:
            if hasattr(self.execute_dt, 'to_alipay_dict'):
                params['execute_dt'] = self.execute_dt.to_alipay_dict()
            else:
                params['execute_dt'] = self.execute_dt
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        if self.related_bill_no:
            if hasattr(self.related_bill_no, 'to_alipay_dict'):
                params['related_bill_no'] = self.related_bill_no.to_alipay_dict()
            else:
                params['related_bill_no'] = self.related_bill_no
        if self.trans_in_open_id:
            if hasattr(self.trans_in_open_id, 'to_alipay_dict'):
                params['trans_in_open_id'] = self.trans_in_open_id.to_alipay_dict()
            else:
                params['trans_in_open_id'] = self.trans_in_open_id
        if self.trans_in_user_id:
            if hasattr(self.trans_in_user_id, 'to_alipay_dict'):
                params['trans_in_user_id'] = self.trans_in_user_id.to_alipay_dict()
            else:
                params['trans_in_user_id'] = self.trans_in_user_id
        if self.trans_in_user_name:
            if hasattr(self.trans_in_user_name, 'to_alipay_dict'):
                params['trans_in_user_name'] = self.trans_in_user_name.to_alipay_dict()
            else:
                params['trans_in_user_name'] = self.trans_in_user_name
        if self.trans_out_open_id:
            if hasattr(self.trans_out_open_id, 'to_alipay_dict'):
                params['trans_out_open_id'] = self.trans_out_open_id.to_alipay_dict()
            else:
                params['trans_out_open_id'] = self.trans_out_open_id
        if self.trans_out_user_id:
            if hasattr(self.trans_out_user_id, 'to_alipay_dict'):
                params['trans_out_user_id'] = self.trans_out_user_id.to_alipay_dict()
            else:
                params['trans_out_user_id'] = self.trans_out_user_id
        if self.trans_out_user_name:
            if hasattr(self.trans_out_user_name, 'to_alipay_dict'):
                params['trans_out_user_name'] = self.trans_out_user_name.to_alipay_dict()
            else:
                params['trans_out_user_name'] = self.trans_out_user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceFeeInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'execute_dt' in d:
            o.execute_dt = d['execute_dt']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        if 'related_bill_no' in d:
            o.related_bill_no = d['related_bill_no']
        if 'trans_in_open_id' in d:
            o.trans_in_open_id = d['trans_in_open_id']
        if 'trans_in_user_id' in d:
            o.trans_in_user_id = d['trans_in_user_id']
        if 'trans_in_user_name' in d:
            o.trans_in_user_name = d['trans_in_user_name']
        if 'trans_out_open_id' in d:
            o.trans_out_open_id = d['trans_out_open_id']
        if 'trans_out_user_id' in d:
            o.trans_out_user_id = d['trans_out_user_id']
        if 'trans_out_user_name' in d:
            o.trans_out_user_name = d['trans_out_user_name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankVerifyDetailInfo(object):

    def __init__(self):
        self._account_name = None
        self._bank_card_no = None
        self._bank_verify_order_no = None
        self._branch_bank_code = None
        self._branch_bank_name = None
        self._certify_end_time = None
        self._out_request_no = None
        self._root_bank_name = None
        self._status = None
        self._status_desc = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_verify_order_no(self):
        return self._bank_verify_order_no

    @bank_verify_order_no.setter
    def bank_verify_order_no(self, value):
        self._bank_verify_order_no = value
    @property
    def branch_bank_code(self):
        return self._branch_bank_code

    @branch_bank_code.setter
    def branch_bank_code(self, value):
        self._branch_bank_code = value
    @property
    def branch_bank_name(self):
        return self._branch_bank_name

    @branch_bank_name.setter
    def branch_bank_name(self, value):
        self._branch_bank_name = value
    @property
    def certify_end_time(self):
        return self._certify_end_time

    @certify_end_time.setter
    def certify_end_time(self, value):
        self._certify_end_time = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def root_bank_name(self):
        return self._root_bank_name

    @root_bank_name.setter
    def root_bank_name(self, value):
        self._root_bank_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_verify_order_no:
            if hasattr(self.bank_verify_order_no, 'to_alipay_dict'):
                params['bank_verify_order_no'] = self.bank_verify_order_no.to_alipay_dict()
            else:
                params['bank_verify_order_no'] = self.bank_verify_order_no
        if self.branch_bank_code:
            if hasattr(self.branch_bank_code, 'to_alipay_dict'):
                params['branch_bank_code'] = self.branch_bank_code.to_alipay_dict()
            else:
                params['branch_bank_code'] = self.branch_bank_code
        if self.branch_bank_name:
            if hasattr(self.branch_bank_name, 'to_alipay_dict'):
                params['branch_bank_name'] = self.branch_bank_name.to_alipay_dict()
            else:
                params['branch_bank_name'] = self.branch_bank_name
        if self.certify_end_time:
            if hasattr(self.certify_end_time, 'to_alipay_dict'):
                params['certify_end_time'] = self.certify_end_time.to_alipay_dict()
            else:
                params['certify_end_time'] = self.certify_end_time
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.root_bank_name:
            if hasattr(self.root_bank_name, 'to_alipay_dict'):
                params['root_bank_name'] = self.root_bank_name.to_alipay_dict()
            else:
                params['root_bank_name'] = self.root_bank_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankVerifyDetailInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_verify_order_no' in d:
            o.bank_verify_order_no = d['bank_verify_order_no']
        if 'branch_bank_code' in d:
            o.branch_bank_code = d['branch_bank_code']
        if 'branch_bank_name' in d:
            o.branch_bank_name = d['branch_bank_name']
        if 'certify_end_time' in d:
            o.certify_end_time = d['certify_end_time']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'root_bank_name' in d:
            o.root_bank_name = d['root_bank_name']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o



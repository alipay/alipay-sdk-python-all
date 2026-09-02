#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclingInvoiceBizTransfer(object):

    def __init__(self):
        self._alipay_pay_no = None
        self._biz_transfer_id = None
        self._company_account_id = None
        self._fail_code = None
        self._fail_reason = None
        self._gmt_pay = None
        self._out_biz_transfer_id = None
        self._out_source = None
        self._payee_account = None
        self._payee_account_type = None
        self._payee_name = None
        self._receipt_file_url = None
        self._receipt_id = None
        self._recycling_order_id = None
        self._transfer_biz_amount = None
        self._transfer_biz_status = None
        self._transfer_biz_type = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def biz_transfer_id(self):
        return self._biz_transfer_id

    @biz_transfer_id.setter
    def biz_transfer_id(self, value):
        self._biz_transfer_id = value
    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def out_biz_transfer_id(self):
        return self._out_biz_transfer_id

    @out_biz_transfer_id.setter
    def out_biz_transfer_id(self, value):
        self._out_biz_transfer_id = value
    @property
    def out_source(self):
        return self._out_source

    @out_source.setter
    def out_source(self, value):
        self._out_source = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def receipt_file_url(self):
        return self._receipt_file_url

    @receipt_file_url.setter
    def receipt_file_url(self, value):
        self._receipt_file_url = value
    @property
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self._receipt_id = value
    @property
    def recycling_order_id(self):
        return self._recycling_order_id

    @recycling_order_id.setter
    def recycling_order_id(self, value):
        self._recycling_order_id = value
    @property
    def transfer_biz_amount(self):
        return self._transfer_biz_amount

    @transfer_biz_amount.setter
    def transfer_biz_amount(self, value):
        self._transfer_biz_amount = value
    @property
    def transfer_biz_status(self):
        return self._transfer_biz_status

    @transfer_biz_status.setter
    def transfer_biz_status(self, value):
        self._transfer_biz_status = value
    @property
    def transfer_biz_type(self):
        return self._transfer_biz_type

    @transfer_biz_type.setter
    def transfer_biz_type(self, value):
        self._transfer_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pay_no:
            if hasattr(self.alipay_pay_no, 'to_alipay_dict'):
                params['alipay_pay_no'] = self.alipay_pay_no.to_alipay_dict()
            else:
                params['alipay_pay_no'] = self.alipay_pay_no
        if self.biz_transfer_id:
            if hasattr(self.biz_transfer_id, 'to_alipay_dict'):
                params['biz_transfer_id'] = self.biz_transfer_id.to_alipay_dict()
            else:
                params['biz_transfer_id'] = self.biz_transfer_id
        if self.company_account_id:
            if hasattr(self.company_account_id, 'to_alipay_dict'):
                params['company_account_id'] = self.company_account_id.to_alipay_dict()
            else:
                params['company_account_id'] = self.company_account_id
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.out_biz_transfer_id:
            if hasattr(self.out_biz_transfer_id, 'to_alipay_dict'):
                params['out_biz_transfer_id'] = self.out_biz_transfer_id.to_alipay_dict()
            else:
                params['out_biz_transfer_id'] = self.out_biz_transfer_id
        if self.out_source:
            if hasattr(self.out_source, 'to_alipay_dict'):
                params['out_source'] = self.out_source.to_alipay_dict()
            else:
                params['out_source'] = self.out_source
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.receipt_file_url:
            if hasattr(self.receipt_file_url, 'to_alipay_dict'):
                params['receipt_file_url'] = self.receipt_file_url.to_alipay_dict()
            else:
                params['receipt_file_url'] = self.receipt_file_url
        if self.receipt_id:
            if hasattr(self.receipt_id, 'to_alipay_dict'):
                params['receipt_id'] = self.receipt_id.to_alipay_dict()
            else:
                params['receipt_id'] = self.receipt_id
        if self.recycling_order_id:
            if hasattr(self.recycling_order_id, 'to_alipay_dict'):
                params['recycling_order_id'] = self.recycling_order_id.to_alipay_dict()
            else:
                params['recycling_order_id'] = self.recycling_order_id
        if self.transfer_biz_amount:
            if hasattr(self.transfer_biz_amount, 'to_alipay_dict'):
                params['transfer_biz_amount'] = self.transfer_biz_amount.to_alipay_dict()
            else:
                params['transfer_biz_amount'] = self.transfer_biz_amount
        if self.transfer_biz_status:
            if hasattr(self.transfer_biz_status, 'to_alipay_dict'):
                params['transfer_biz_status'] = self.transfer_biz_status.to_alipay_dict()
            else:
                params['transfer_biz_status'] = self.transfer_biz_status
        if self.transfer_biz_type:
            if hasattr(self.transfer_biz_type, 'to_alipay_dict'):
                params['transfer_biz_type'] = self.transfer_biz_type.to_alipay_dict()
            else:
                params['transfer_biz_type'] = self.transfer_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclingInvoiceBizTransfer()
        if 'alipay_pay_no' in d:
            o.alipay_pay_no = d['alipay_pay_no']
        if 'biz_transfer_id' in d:
            o.biz_transfer_id = d['biz_transfer_id']
        if 'company_account_id' in d:
            o.company_account_id = d['company_account_id']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'out_biz_transfer_id' in d:
            o.out_biz_transfer_id = d['out_biz_transfer_id']
        if 'out_source' in d:
            o.out_source = d['out_source']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'receipt_file_url' in d:
            o.receipt_file_url = d['receipt_file_url']
        if 'receipt_id' in d:
            o.receipt_id = d['receipt_id']
        if 'recycling_order_id' in d:
            o.recycling_order_id = d['recycling_order_id']
        if 'transfer_biz_amount' in d:
            o.transfer_biz_amount = d['transfer_biz_amount']
        if 'transfer_biz_status' in d:
            o.transfer_biz_status = d['transfer_biz_status']
        if 'transfer_biz_type' in d:
            o.transfer_biz_type = d['transfer_biz_type']
        return o



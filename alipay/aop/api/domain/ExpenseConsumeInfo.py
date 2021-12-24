#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseConsumeInfo(object):

    def __init__(self):
        self._account_id = None
        self._actual_account_number = None
        self._batch_id = None
        self._bill_no = None
        self._bill_type = None
        self._category_name = None
        self._consume_amount = None
        self._consume_date = None
        self._consume_title = None
        self._employee_id = None
        self._merchant_id = None
        self._mshop_id = None
        self._open_model = None
        self._original_voucher_id = None
        self._out_biz_no = None
        self._p_pay_amount = None
        self._payee_name = None
        self._project_id = None
        self._projiect_id = None
        self._refund_amount = None
        self._refund_status = None
        self._standard_id = None
        self._store_id = None
        self._summary_id = None
        self._tp_sign = None
        self._voucher_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def actual_account_number(self):
        return self._actual_account_number

    @actual_account_number.setter
    def actual_account_number(self, value):
        self._actual_account_number = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
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
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def consume_amount(self):
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, value):
        self._consume_amount = value
    @property
    def consume_date(self):
        return self._consume_date

    @consume_date.setter
    def consume_date(self, value):
        self._consume_date = value
    @property
    def consume_title(self):
        return self._consume_title

    @consume_title.setter
    def consume_title(self, value):
        self._consume_title = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def mshop_id(self):
        return self._mshop_id

    @mshop_id.setter
    def mshop_id(self, value):
        self._mshop_id = value
    @property
    def open_model(self):
        return self._open_model

    @open_model.setter
    def open_model(self, value):
        self._open_model = value
    @property
    def original_voucher_id(self):
        return self._original_voucher_id

    @original_voucher_id.setter
    def original_voucher_id(self, value):
        self._original_voucher_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def p_pay_amount(self):
        return self._p_pay_amount

    @p_pay_amount.setter
    def p_pay_amount(self, value):
        self._p_pay_amount = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def projiect_id(self):
        return self._projiect_id

    @projiect_id.setter
    def projiect_id(self, value):
        self._projiect_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def standard_id(self):
        return self._standard_id

    @standard_id.setter
    def standard_id(self, value):
        self._standard_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def summary_id(self):
        return self._summary_id

    @summary_id.setter
    def summary_id(self, value):
        self._summary_id = value
    @property
    def tp_sign(self):
        return self._tp_sign

    @tp_sign.setter
    def tp_sign(self, value):
        self._tp_sign = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.actual_account_number:
            if hasattr(self.actual_account_number, 'to_alipay_dict'):
                params['actual_account_number'] = self.actual_account_number.to_alipay_dict()
            else:
                params['actual_account_number'] = self.actual_account_number
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
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
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.consume_amount:
            if hasattr(self.consume_amount, 'to_alipay_dict'):
                params['consume_amount'] = self.consume_amount.to_alipay_dict()
            else:
                params['consume_amount'] = self.consume_amount
        if self.consume_date:
            if hasattr(self.consume_date, 'to_alipay_dict'):
                params['consume_date'] = self.consume_date.to_alipay_dict()
            else:
                params['consume_date'] = self.consume_date
        if self.consume_title:
            if hasattr(self.consume_title, 'to_alipay_dict'):
                params['consume_title'] = self.consume_title.to_alipay_dict()
            else:
                params['consume_title'] = self.consume_title
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.mshop_id:
            if hasattr(self.mshop_id, 'to_alipay_dict'):
                params['mshop_id'] = self.mshop_id.to_alipay_dict()
            else:
                params['mshop_id'] = self.mshop_id
        if self.open_model:
            if hasattr(self.open_model, 'to_alipay_dict'):
                params['open_model'] = self.open_model.to_alipay_dict()
            else:
                params['open_model'] = self.open_model
        if self.original_voucher_id:
            if hasattr(self.original_voucher_id, 'to_alipay_dict'):
                params['original_voucher_id'] = self.original_voucher_id.to_alipay_dict()
            else:
                params['original_voucher_id'] = self.original_voucher_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.p_pay_amount:
            if hasattr(self.p_pay_amount, 'to_alipay_dict'):
                params['p_pay_amount'] = self.p_pay_amount.to_alipay_dict()
            else:
                params['p_pay_amount'] = self.p_pay_amount
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.projiect_id:
            if hasattr(self.projiect_id, 'to_alipay_dict'):
                params['projiect_id'] = self.projiect_id.to_alipay_dict()
            else:
                params['projiect_id'] = self.projiect_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.standard_id:
            if hasattr(self.standard_id, 'to_alipay_dict'):
                params['standard_id'] = self.standard_id.to_alipay_dict()
            else:
                params['standard_id'] = self.standard_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.summary_id:
            if hasattr(self.summary_id, 'to_alipay_dict'):
                params['summary_id'] = self.summary_id.to_alipay_dict()
            else:
                params['summary_id'] = self.summary_id
        if self.tp_sign:
            if hasattr(self.tp_sign, 'to_alipay_dict'):
                params['tp_sign'] = self.tp_sign.to_alipay_dict()
            else:
                params['tp_sign'] = self.tp_sign
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseConsumeInfo()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'actual_account_number' in d:
            o.actual_account_number = d['actual_account_number']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'consume_amount' in d:
            o.consume_amount = d['consume_amount']
        if 'consume_date' in d:
            o.consume_date = d['consume_date']
        if 'consume_title' in d:
            o.consume_title = d['consume_title']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'mshop_id' in d:
            o.mshop_id = d['mshop_id']
        if 'open_model' in d:
            o.open_model = d['open_model']
        if 'original_voucher_id' in d:
            o.original_voucher_id = d['original_voucher_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'p_pay_amount' in d:
            o.p_pay_amount = d['p_pay_amount']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'projiect_id' in d:
            o.projiect_id = d['projiect_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'standard_id' in d:
            o.standard_id = d['standard_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'summary_id' in d:
            o.summary_id = d['summary_id']
        if 'tp_sign' in d:
            o.tp_sign = d['tp_sign']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o



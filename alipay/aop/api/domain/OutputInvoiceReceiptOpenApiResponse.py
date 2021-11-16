#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class OutputInvoiceReceiptOpenApiResponse(object):

    def __init__(self):
        self._arrangement_no = None
        self._can_appoint_invoice_mode = None
        self._inst_id = None
        self._inv_dt = None
        self._inv_mode = None
        self._invoice_amt = None
        self._invoiced_amt = None
        self._ip_id = None
        self._ip_role_id = None
        self._link_invoice_amt = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._prod_code = None
        self._receivable_amount = None
        self._settle_type = None
        self._status = None
        self._tax_rate = None
        self._tax_type = None
        self._tnt_inst_id = None
        self._write_off_amount = None

    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def can_appoint_invoice_mode(self):
        return self._can_appoint_invoice_mode

    @can_appoint_invoice_mode.setter
    def can_appoint_invoice_mode(self, value):
        self._can_appoint_invoice_mode = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inv_dt(self):
        return self._inv_dt

    @inv_dt.setter
    def inv_dt(self, value):
        self._inv_dt = value
    @property
    def inv_mode(self):
        return self._inv_mode

    @inv_mode.setter
    def inv_mode(self, value):
        self._inv_mode = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoiced_amt(self):
        return self._invoiced_amt

    @invoiced_amt.setter
    def invoiced_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoiced_amt = value
        else:
            self._invoiced_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def link_invoice_amt(self):
        return self._link_invoice_amt

    @link_invoice_amt.setter
    def link_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._link_invoice_amt = value
        else:
            self._link_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def receivable_amount(self):
        return self._receivable_amount

    @receivable_amount.setter
    def receivable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._receivable_amount = value
        else:
            self._receivable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def write_off_amount(self):
        return self._write_off_amount

    @write_off_amount.setter
    def write_off_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._write_off_amount = value
        else:
            self._write_off_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.can_appoint_invoice_mode:
            if hasattr(self.can_appoint_invoice_mode, 'to_alipay_dict'):
                params['can_appoint_invoice_mode'] = self.can_appoint_invoice_mode.to_alipay_dict()
            else:
                params['can_appoint_invoice_mode'] = self.can_appoint_invoice_mode
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inv_dt:
            if hasattr(self.inv_dt, 'to_alipay_dict'):
                params['inv_dt'] = self.inv_dt.to_alipay_dict()
            else:
                params['inv_dt'] = self.inv_dt
        if self.inv_mode:
            if hasattr(self.inv_mode, 'to_alipay_dict'):
                params['inv_mode'] = self.inv_mode.to_alipay_dict()
            else:
                params['inv_mode'] = self.inv_mode
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoiced_amt:
            if hasattr(self.invoiced_amt, 'to_alipay_dict'):
                params['invoiced_amt'] = self.invoiced_amt.to_alipay_dict()
            else:
                params['invoiced_amt'] = self.invoiced_amt
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.link_invoice_amt:
            if hasattr(self.link_invoice_amt, 'to_alipay_dict'):
                params['link_invoice_amt'] = self.link_invoice_amt.to_alipay_dict()
            else:
                params['link_invoice_amt'] = self.link_invoice_amt
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.receivable_amount:
            if hasattr(self.receivable_amount, 'to_alipay_dict'):
                params['receivable_amount'] = self.receivable_amount.to_alipay_dict()
            else:
                params['receivable_amount'] = self.receivable_amount
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.write_off_amount:
            if hasattr(self.write_off_amount, 'to_alipay_dict'):
                params['write_off_amount'] = self.write_off_amount.to_alipay_dict()
            else:
                params['write_off_amount'] = self.write_off_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutputInvoiceReceiptOpenApiResponse()
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'can_appoint_invoice_mode' in d:
            o.can_appoint_invoice_mode = d['can_appoint_invoice_mode']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inv_dt' in d:
            o.inv_dt = d['inv_dt']
        if 'inv_mode' in d:
            o.inv_mode = d['inv_mode']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'link_invoice_amt' in d:
            o.link_invoice_amt = d['link_invoice_amt']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'receivable_amount' in d:
            o.receivable_amount = d['receivable_amount']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'status' in d:
            o.status = d['status']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'write_off_amount' in d:
            o.write_off_amount = d['write_off_amount']
        return o



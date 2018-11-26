#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ArMonthlyBillDTO(object):

    def __init__(self):
        self._account_day = None
        self._accrued_date = None
        self._adjust_amt = None
        self._analysis_dmsn_1 = None
        self._analysis_dmsn_2 = None
        self._analysis_dmsn_3 = None
        self._analysis_dmsn_4 = None
        self._arrangement_no = None
        self._bill_amt = None
        self._bill_end_date = None
        self._bill_month = None
        self._bill_no = None
        self._bill_start_date = None
        self._bill_type = None
        self._charge_item_code = None
        self._charge_type = None
        self._check_status = None
        self._checked_amt = None
        self._checking_amt = None
        self._clcn_basic_amt = None
        self._clcn_basic_type = None
        self._clcn_method = None
        self._freeze_amt = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_pay = None
        self._inst_id = None
        self._invoice_amt = None
        self._invoiced_amt = None
        self._ip_id = None
        self._ip_name = None
        self._ip_role_id = None
        self._last_moder = None
        self._link_invoice_amt = None
        self._pay_original = None
        self._pay_status = None
        self._pay_way = None
        self._payee_account = None
        self._payer_account = None
        self._payer_ip_role_id = None
        self._prod_code = None
        self._received_amt = None
        self._record_id = None
        self._service_amt = None
        self._settle_type = None
        self._sign_ip_id = None
        self._sign_ip_role_id = None
        self._stl_ip_role_id = None
        self._tax_amt = None
        self._tax_rate = None
        self._tax_type = None
        self._to_writeoff_detail_count = None
        self._type = None
        self._writeoff_detail_dount = None
        self._writingoff_amt = None

    @property
    def account_day(self):
        return self._account_day

    @account_day.setter
    def account_day(self, value):
        self._account_day = value
    @property
    def accrued_date(self):
        return self._accrued_date

    @accrued_date.setter
    def accrued_date(self, value):
        self._accrued_date = value
    @property
    def adjust_amt(self):
        return self._adjust_amt

    @adjust_amt.setter
    def adjust_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._adjust_amt = value
        else:
            self._adjust_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def analysis_dmsn_1(self):
        return self._analysis_dmsn_1

    @analysis_dmsn_1.setter
    def analysis_dmsn_1(self, value):
        self._analysis_dmsn_1 = value
    @property
    def analysis_dmsn_2(self):
        return self._analysis_dmsn_2

    @analysis_dmsn_2.setter
    def analysis_dmsn_2(self, value):
        self._analysis_dmsn_2 = value
    @property
    def analysis_dmsn_3(self):
        return self._analysis_dmsn_3

    @analysis_dmsn_3.setter
    def analysis_dmsn_3(self, value):
        self._analysis_dmsn_3 = value
    @property
    def analysis_dmsn_4(self):
        return self._analysis_dmsn_4

    @analysis_dmsn_4.setter
    def analysis_dmsn_4(self, value):
        self._analysis_dmsn_4 = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def bill_amt(self):
        return self._bill_amt

    @bill_amt.setter
    def bill_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amt = value
        else:
            self._bill_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_end_date(self):
        return self._bill_end_date

    @bill_end_date.setter
    def bill_end_date(self, value):
        self._bill_end_date = value
    @property
    def bill_month(self):
        return self._bill_month

    @bill_month.setter
    def bill_month(self, value):
        self._bill_month = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_start_date(self):
        return self._bill_start_date

    @bill_start_date.setter
    def bill_start_date(self, value):
        self._bill_start_date = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def charge_item_code(self):
        return self._charge_item_code

    @charge_item_code.setter
    def charge_item_code(self, value):
        self._charge_item_code = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def check_status(self):
        return self._check_status

    @check_status.setter
    def check_status(self, value):
        self._check_status = value
    @property
    def checked_amt(self):
        return self._checked_amt

    @checked_amt.setter
    def checked_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._checked_amt = value
        else:
            self._checked_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def checking_amt(self):
        return self._checking_amt

    @checking_amt.setter
    def checking_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._checking_amt = value
        else:
            self._checking_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def clcn_basic_amt(self):
        return self._clcn_basic_amt

    @clcn_basic_amt.setter
    def clcn_basic_amt(self, value):
        self._clcn_basic_amt = value
    @property
    def clcn_basic_type(self):
        return self._clcn_basic_type

    @clcn_basic_type.setter
    def clcn_basic_type(self, value):
        self._clcn_basic_type = value
    @property
    def clcn_method(self):
        return self._clcn_method

    @clcn_method.setter
    def clcn_method(self, value):
        self._clcn_method = value
    @property
    def freeze_amt(self):
        return self._freeze_amt

    @freeze_amt.setter
    def freeze_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._freeze_amt = value
        else:
            self._freeze_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
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
    def ip_name(self):
        return self._ip_name

    @ip_name.setter
    def ip_name(self, value):
        self._ip_name = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
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
    def pay_original(self):
        return self._pay_original

    @pay_original.setter
    def pay_original(self, value):
        self._pay_original = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_way(self):
        return self._pay_way

    @pay_way.setter
    def pay_way(self, value):
        self._pay_way = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        self._payer_account = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def received_amt(self):
        return self._received_amt

    @received_amt.setter
    def received_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._received_amt = value
        else:
            self._received_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def service_amt(self):
        return self._service_amt

    @service_amt.setter
    def service_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._service_amt = value
        else:
            self._service_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def sign_ip_id(self):
        return self._sign_ip_id

    @sign_ip_id.setter
    def sign_ip_id(self, value):
        self._sign_ip_id = value
    @property
    def sign_ip_role_id(self):
        return self._sign_ip_role_id

    @sign_ip_role_id.setter
    def sign_ip_role_id(self, value):
        self._sign_ip_role_id = value
    @property
    def stl_ip_role_id(self):
        return self._stl_ip_role_id

    @stl_ip_role_id.setter
    def stl_ip_role_id(self, value):
        self._stl_ip_role_id = value
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amt = value
        else:
            self._tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def to_writeoff_detail_count(self):
        return self._to_writeoff_detail_count

    @to_writeoff_detail_count.setter
    def to_writeoff_detail_count(self, value):
        self._to_writeoff_detail_count = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def writeoff_detail_dount(self):
        return self._writeoff_detail_dount

    @writeoff_detail_dount.setter
    def writeoff_detail_dount(self, value):
        self._writeoff_detail_dount = value
    @property
    def writingoff_amt(self):
        return self._writingoff_amt

    @writingoff_amt.setter
    def writingoff_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._writingoff_amt = value
        else:
            self._writingoff_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.account_day:
            if hasattr(self.account_day, 'to_alipay_dict'):
                params['account_day'] = self.account_day.to_alipay_dict()
            else:
                params['account_day'] = self.account_day
        if self.accrued_date:
            if hasattr(self.accrued_date, 'to_alipay_dict'):
                params['accrued_date'] = self.accrued_date.to_alipay_dict()
            else:
                params['accrued_date'] = self.accrued_date
        if self.adjust_amt:
            if hasattr(self.adjust_amt, 'to_alipay_dict'):
                params['adjust_amt'] = self.adjust_amt.to_alipay_dict()
            else:
                params['adjust_amt'] = self.adjust_amt
        if self.analysis_dmsn_1:
            if hasattr(self.analysis_dmsn_1, 'to_alipay_dict'):
                params['analysis_dmsn_1'] = self.analysis_dmsn_1.to_alipay_dict()
            else:
                params['analysis_dmsn_1'] = self.analysis_dmsn_1
        if self.analysis_dmsn_2:
            if hasattr(self.analysis_dmsn_2, 'to_alipay_dict'):
                params['analysis_dmsn_2'] = self.analysis_dmsn_2.to_alipay_dict()
            else:
                params['analysis_dmsn_2'] = self.analysis_dmsn_2
        if self.analysis_dmsn_3:
            if hasattr(self.analysis_dmsn_3, 'to_alipay_dict'):
                params['analysis_dmsn_3'] = self.analysis_dmsn_3.to_alipay_dict()
            else:
                params['analysis_dmsn_3'] = self.analysis_dmsn_3
        if self.analysis_dmsn_4:
            if hasattr(self.analysis_dmsn_4, 'to_alipay_dict'):
                params['analysis_dmsn_4'] = self.analysis_dmsn_4.to_alipay_dict()
            else:
                params['analysis_dmsn_4'] = self.analysis_dmsn_4
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.bill_amt:
            if hasattr(self.bill_amt, 'to_alipay_dict'):
                params['bill_amt'] = self.bill_amt.to_alipay_dict()
            else:
                params['bill_amt'] = self.bill_amt
        if self.bill_end_date:
            if hasattr(self.bill_end_date, 'to_alipay_dict'):
                params['bill_end_date'] = self.bill_end_date.to_alipay_dict()
            else:
                params['bill_end_date'] = self.bill_end_date
        if self.bill_month:
            if hasattr(self.bill_month, 'to_alipay_dict'):
                params['bill_month'] = self.bill_month.to_alipay_dict()
            else:
                params['bill_month'] = self.bill_month
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_start_date:
            if hasattr(self.bill_start_date, 'to_alipay_dict'):
                params['bill_start_date'] = self.bill_start_date.to_alipay_dict()
            else:
                params['bill_start_date'] = self.bill_start_date
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.charge_item_code:
            if hasattr(self.charge_item_code, 'to_alipay_dict'):
                params['charge_item_code'] = self.charge_item_code.to_alipay_dict()
            else:
                params['charge_item_code'] = self.charge_item_code
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.check_status:
            if hasattr(self.check_status, 'to_alipay_dict'):
                params['check_status'] = self.check_status.to_alipay_dict()
            else:
                params['check_status'] = self.check_status
        if self.checked_amt:
            if hasattr(self.checked_amt, 'to_alipay_dict'):
                params['checked_amt'] = self.checked_amt.to_alipay_dict()
            else:
                params['checked_amt'] = self.checked_amt
        if self.checking_amt:
            if hasattr(self.checking_amt, 'to_alipay_dict'):
                params['checking_amt'] = self.checking_amt.to_alipay_dict()
            else:
                params['checking_amt'] = self.checking_amt
        if self.clcn_basic_amt:
            if hasattr(self.clcn_basic_amt, 'to_alipay_dict'):
                params['clcn_basic_amt'] = self.clcn_basic_amt.to_alipay_dict()
            else:
                params['clcn_basic_amt'] = self.clcn_basic_amt
        if self.clcn_basic_type:
            if hasattr(self.clcn_basic_type, 'to_alipay_dict'):
                params['clcn_basic_type'] = self.clcn_basic_type.to_alipay_dict()
            else:
                params['clcn_basic_type'] = self.clcn_basic_type
        if self.clcn_method:
            if hasattr(self.clcn_method, 'to_alipay_dict'):
                params['clcn_method'] = self.clcn_method.to_alipay_dict()
            else:
                params['clcn_method'] = self.clcn_method
        if self.freeze_amt:
            if hasattr(self.freeze_amt, 'to_alipay_dict'):
                params['freeze_amt'] = self.freeze_amt.to_alipay_dict()
            else:
                params['freeze_amt'] = self.freeze_amt
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
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
        if self.ip_name:
            if hasattr(self.ip_name, 'to_alipay_dict'):
                params['ip_name'] = self.ip_name.to_alipay_dict()
            else:
                params['ip_name'] = self.ip_name
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.link_invoice_amt:
            if hasattr(self.link_invoice_amt, 'to_alipay_dict'):
                params['link_invoice_amt'] = self.link_invoice_amt.to_alipay_dict()
            else:
                params['link_invoice_amt'] = self.link_invoice_amt
        if self.pay_original:
            if hasattr(self.pay_original, 'to_alipay_dict'):
                params['pay_original'] = self.pay_original.to_alipay_dict()
            else:
                params['pay_original'] = self.pay_original
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_way:
            if hasattr(self.pay_way, 'to_alipay_dict'):
                params['pay_way'] = self.pay_way.to_alipay_dict()
            else:
                params['pay_way'] = self.pay_way
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.received_amt:
            if hasattr(self.received_amt, 'to_alipay_dict'):
                params['received_amt'] = self.received_amt.to_alipay_dict()
            else:
                params['received_amt'] = self.received_amt
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.service_amt:
            if hasattr(self.service_amt, 'to_alipay_dict'):
                params['service_amt'] = self.service_amt.to_alipay_dict()
            else:
                params['service_amt'] = self.service_amt
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.sign_ip_id:
            if hasattr(self.sign_ip_id, 'to_alipay_dict'):
                params['sign_ip_id'] = self.sign_ip_id.to_alipay_dict()
            else:
                params['sign_ip_id'] = self.sign_ip_id
        if self.sign_ip_role_id:
            if hasattr(self.sign_ip_role_id, 'to_alipay_dict'):
                params['sign_ip_role_id'] = self.sign_ip_role_id.to_alipay_dict()
            else:
                params['sign_ip_role_id'] = self.sign_ip_role_id
        if self.stl_ip_role_id:
            if hasattr(self.stl_ip_role_id, 'to_alipay_dict'):
                params['stl_ip_role_id'] = self.stl_ip_role_id.to_alipay_dict()
            else:
                params['stl_ip_role_id'] = self.stl_ip_role_id
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
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
        if self.to_writeoff_detail_count:
            if hasattr(self.to_writeoff_detail_count, 'to_alipay_dict'):
                params['to_writeoff_detail_count'] = self.to_writeoff_detail_count.to_alipay_dict()
            else:
                params['to_writeoff_detail_count'] = self.to_writeoff_detail_count
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.writeoff_detail_dount:
            if hasattr(self.writeoff_detail_dount, 'to_alipay_dict'):
                params['writeoff_detail_dount'] = self.writeoff_detail_dount.to_alipay_dict()
            else:
                params['writeoff_detail_dount'] = self.writeoff_detail_dount
        if self.writingoff_amt:
            if hasattr(self.writingoff_amt, 'to_alipay_dict'):
                params['writingoff_amt'] = self.writingoff_amt.to_alipay_dict()
            else:
                params['writingoff_amt'] = self.writingoff_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArMonthlyBillDTO()
        if 'account_day' in d:
            o.account_day = d['account_day']
        if 'accrued_date' in d:
            o.accrued_date = d['accrued_date']
        if 'adjust_amt' in d:
            o.adjust_amt = d['adjust_amt']
        if 'analysis_dmsn_1' in d:
            o.analysis_dmsn_1 = d['analysis_dmsn_1']
        if 'analysis_dmsn_2' in d:
            o.analysis_dmsn_2 = d['analysis_dmsn_2']
        if 'analysis_dmsn_3' in d:
            o.analysis_dmsn_3 = d['analysis_dmsn_3']
        if 'analysis_dmsn_4' in d:
            o.analysis_dmsn_4 = d['analysis_dmsn_4']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_amt' in d:
            o.bill_amt = d['bill_amt']
        if 'bill_end_date' in d:
            o.bill_end_date = d['bill_end_date']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_start_date' in d:
            o.bill_start_date = d['bill_start_date']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'charge_item_code' in d:
            o.charge_item_code = d['charge_item_code']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'check_status' in d:
            o.check_status = d['check_status']
        if 'checked_amt' in d:
            o.checked_amt = d['checked_amt']
        if 'checking_amt' in d:
            o.checking_amt = d['checking_amt']
        if 'clcn_basic_amt' in d:
            o.clcn_basic_amt = d['clcn_basic_amt']
        if 'clcn_basic_type' in d:
            o.clcn_basic_type = d['clcn_basic_type']
        if 'clcn_method' in d:
            o.clcn_method = d['clcn_method']
        if 'freeze_amt' in d:
            o.freeze_amt = d['freeze_amt']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_name' in d:
            o.ip_name = d['ip_name']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'link_invoice_amt' in d:
            o.link_invoice_amt = d['link_invoice_amt']
        if 'pay_original' in d:
            o.pay_original = d['pay_original']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_way' in d:
            o.pay_way = d['pay_way']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'received_amt' in d:
            o.received_amt = d['received_amt']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'service_amt' in d:
            o.service_amt = d['service_amt']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'sign_ip_id' in d:
            o.sign_ip_id = d['sign_ip_id']
        if 'sign_ip_role_id' in d:
            o.sign_ip_role_id = d['sign_ip_role_id']
        if 'stl_ip_role_id' in d:
            o.stl_ip_role_id = d['stl_ip_role_id']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'to_writeoff_detail_count' in d:
            o.to_writeoff_detail_count = d['to_writeoff_detail_count']
        if 'type' in d:
            o.type = d['type']
        if 'writeoff_detail_dount' in d:
            o.writeoff_detail_dount = d['writeoff_detail_dount']
        if 'writingoff_amt' in d:
            o.writingoff_amt = d['writingoff_amt']
        return o



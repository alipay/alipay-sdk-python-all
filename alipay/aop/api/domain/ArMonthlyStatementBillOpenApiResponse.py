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


class ArMonthlyStatementBillOpenApiResponse(object):

    def __init__(self):
        self._accounting_time_zone = None
        self._accrued_date = None
        self._adjust_amt = None
        self._analysis_dmsn = None
        self._analysis_dmsn_1 = None
        self._analysis_dmsn_2 = None
        self._analysis_dmsn_3 = None
        self._analysis_dmsn_4 = None
        self._applying_invoice_amt = None
        self._arrangement_no = None
        self._bill_amt = None
        self._bill_end_date = None
        self._bill_month = None
        self._bill_no = None
        self._bill_start_date = None
        self._charge_item_code = None
        self._charge_type = None
        self._charge_type_name = None
        self._check_state = None
        self._clcn_basic_amt = None
        self._clcn_basic_type = None
        self._clcn_basic_type_name = None
        self._clcn_method = None
        self._clcn_method_name = None
        self._detail_bill_adj_amt = None
        self._detail_bill_adj_reason = None
        self._env_source = None
        self._inst_id = None
        self._inter_trade_flag = None
        self._invoice_amt = None
        self._invoice_status = None
        self._invoiced_amt = None
        self._ip_id = None
        self._ip_role_id = None
        self._link_invoice_amt = None
        self._memo = None
        self._metadata_source = None
        self._monthly_bill_no = None
        self._paid_amt = None
        self._past_pay_flag = None
        self._pay_status = None
        self._pay_way = None
        self._payable_amt = None
        self._payable_flag = None
        self._payee_account = None
        self._payer_account_no = None
        self._payer_ip_role_id = None
        self._price_policy_id = None
        self._prod_code = None
        self._product_name = None
        self._received_amt = None
        self._rel_rcpt_list = None
        self._settle_period = None
        self._settle_time_zone = None
        self._settle_type = None
        self._sign_ip_id = None
        self._sign_ip_id_name = None
        self._sign_ip_role_id = None
        self._tax_amt = None
        self._tax_rate = None
        self._tax_tp = None
        self._tnt_inst_id = None
        self._to_writeoff_detail_count = None
        self._type = None
        self._type_name = None
        self._writeoff_detail_count = None

    @property
    def accounting_time_zone(self):
        return self._accounting_time_zone

    @accounting_time_zone.setter
    def accounting_time_zone(self, value):
        self._accounting_time_zone = value
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
    def analysis_dmsn(self):
        return self._analysis_dmsn

    @analysis_dmsn.setter
    def analysis_dmsn(self, value):
        self._analysis_dmsn = value
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
    def applying_invoice_amt(self):
        return self._applying_invoice_amt

    @applying_invoice_amt.setter
    def applying_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._applying_invoice_amt = value
        else:
            self._applying_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def charge_type_name(self):
        return self._charge_type_name

    @charge_type_name.setter
    def charge_type_name(self, value):
        self._charge_type_name = value
    @property
    def check_state(self):
        return self._check_state

    @check_state.setter
    def check_state(self, value):
        self._check_state = value
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
    def clcn_basic_type_name(self):
        return self._clcn_basic_type_name

    @clcn_basic_type_name.setter
    def clcn_basic_type_name(self, value):
        self._clcn_basic_type_name = value
    @property
    def clcn_method(self):
        return self._clcn_method

    @clcn_method.setter
    def clcn_method(self, value):
        self._clcn_method = value
    @property
    def clcn_method_name(self):
        return self._clcn_method_name

    @clcn_method_name.setter
    def clcn_method_name(self, value):
        self._clcn_method_name = value
    @property
    def detail_bill_adj_amt(self):
        return self._detail_bill_adj_amt

    @detail_bill_adj_amt.setter
    def detail_bill_adj_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._detail_bill_adj_amt = value
        else:
            self._detail_bill_adj_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def detail_bill_adj_reason(self):
        return self._detail_bill_adj_reason

    @detail_bill_adj_reason.setter
    def detail_bill_adj_reason(self, value):
        self._detail_bill_adj_reason = value
    @property
    def env_source(self):
        return self._env_source

    @env_source.setter
    def env_source(self, value):
        self._env_source = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inter_trade_flag(self):
        return self._inter_trade_flag

    @inter_trade_flag.setter
    def inter_trade_flag(self, value):
        self._inter_trade_flag = value
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
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def metadata_source(self):
        return self._metadata_source

    @metadata_source.setter
    def metadata_source(self, value):
        self._metadata_source = value
    @property
    def monthly_bill_no(self):
        return self._monthly_bill_no

    @monthly_bill_no.setter
    def monthly_bill_no(self, value):
        self._monthly_bill_no = value
    @property
    def paid_amt(self):
        return self._paid_amt

    @paid_amt.setter
    def paid_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._paid_amt = value
        else:
            self._paid_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def past_pay_flag(self):
        return self._past_pay_flag

    @past_pay_flag.setter
    def past_pay_flag(self, value):
        self._past_pay_flag = value
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
    def payable_amt(self):
        return self._payable_amt

    @payable_amt.setter
    def payable_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._payable_amt = value
        else:
            self._payable_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def payable_flag(self):
        return self._payable_flag

    @payable_flag.setter
    def payable_flag(self, value):
        self._payable_flag = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def price_policy_id(self):
        return self._price_policy_id

    @price_policy_id.setter
    def price_policy_id(self, value):
        self._price_policy_id = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
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
    def rel_rcpt_list(self):
        return self._rel_rcpt_list

    @rel_rcpt_list.setter
    def rel_rcpt_list(self, value):
        if isinstance(value, list):
            self._rel_rcpt_list = list()
            for i in value:
                self._rel_rcpt_list.append(i)
    @property
    def settle_period(self):
        return self._settle_period

    @settle_period.setter
    def settle_period(self, value):
        self._settle_period = value
    @property
    def settle_time_zone(self):
        return self._settle_time_zone

    @settle_time_zone.setter
    def settle_time_zone(self, value):
        self._settle_time_zone = value
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
    def sign_ip_id_name(self):
        return self._sign_ip_id_name

    @sign_ip_id_name.setter
    def sign_ip_id_name(self, value):
        self._sign_ip_id_name = value
    @property
    def sign_ip_role_id(self):
        return self._sign_ip_role_id

    @sign_ip_role_id.setter
    def sign_ip_role_id(self, value):
        self._sign_ip_role_id = value
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
    def tax_tp(self):
        return self._tax_tp

    @tax_tp.setter
    def tax_tp(self, value):
        self._tax_tp = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
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
    def type_name(self):
        return self._type_name

    @type_name.setter
    def type_name(self, value):
        self._type_name = value
    @property
    def writeoff_detail_count(self):
        return self._writeoff_detail_count

    @writeoff_detail_count.setter
    def writeoff_detail_count(self, value):
        self._writeoff_detail_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_time_zone:
            if hasattr(self.accounting_time_zone, 'to_alipay_dict'):
                params['accounting_time_zone'] = self.accounting_time_zone.to_alipay_dict()
            else:
                params['accounting_time_zone'] = self.accounting_time_zone
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
        if self.analysis_dmsn:
            if hasattr(self.analysis_dmsn, 'to_alipay_dict'):
                params['analysis_dmsn'] = self.analysis_dmsn.to_alipay_dict()
            else:
                params['analysis_dmsn'] = self.analysis_dmsn
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
        if self.applying_invoice_amt:
            if hasattr(self.applying_invoice_amt, 'to_alipay_dict'):
                params['applying_invoice_amt'] = self.applying_invoice_amt.to_alipay_dict()
            else:
                params['applying_invoice_amt'] = self.applying_invoice_amt
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
        if self.charge_type_name:
            if hasattr(self.charge_type_name, 'to_alipay_dict'):
                params['charge_type_name'] = self.charge_type_name.to_alipay_dict()
            else:
                params['charge_type_name'] = self.charge_type_name
        if self.check_state:
            if hasattr(self.check_state, 'to_alipay_dict'):
                params['check_state'] = self.check_state.to_alipay_dict()
            else:
                params['check_state'] = self.check_state
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
        if self.clcn_basic_type_name:
            if hasattr(self.clcn_basic_type_name, 'to_alipay_dict'):
                params['clcn_basic_type_name'] = self.clcn_basic_type_name.to_alipay_dict()
            else:
                params['clcn_basic_type_name'] = self.clcn_basic_type_name
        if self.clcn_method:
            if hasattr(self.clcn_method, 'to_alipay_dict'):
                params['clcn_method'] = self.clcn_method.to_alipay_dict()
            else:
                params['clcn_method'] = self.clcn_method
        if self.clcn_method_name:
            if hasattr(self.clcn_method_name, 'to_alipay_dict'):
                params['clcn_method_name'] = self.clcn_method_name.to_alipay_dict()
            else:
                params['clcn_method_name'] = self.clcn_method_name
        if self.detail_bill_adj_amt:
            if hasattr(self.detail_bill_adj_amt, 'to_alipay_dict'):
                params['detail_bill_adj_amt'] = self.detail_bill_adj_amt.to_alipay_dict()
            else:
                params['detail_bill_adj_amt'] = self.detail_bill_adj_amt
        if self.detail_bill_adj_reason:
            if hasattr(self.detail_bill_adj_reason, 'to_alipay_dict'):
                params['detail_bill_adj_reason'] = self.detail_bill_adj_reason.to_alipay_dict()
            else:
                params['detail_bill_adj_reason'] = self.detail_bill_adj_reason
        if self.env_source:
            if hasattr(self.env_source, 'to_alipay_dict'):
                params['env_source'] = self.env_source.to_alipay_dict()
            else:
                params['env_source'] = self.env_source
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inter_trade_flag:
            if hasattr(self.inter_trade_flag, 'to_alipay_dict'):
                params['inter_trade_flag'] = self.inter_trade_flag.to_alipay_dict()
            else:
                params['inter_trade_flag'] = self.inter_trade_flag
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.metadata_source:
            if hasattr(self.metadata_source, 'to_alipay_dict'):
                params['metadata_source'] = self.metadata_source.to_alipay_dict()
            else:
                params['metadata_source'] = self.metadata_source
        if self.monthly_bill_no:
            if hasattr(self.monthly_bill_no, 'to_alipay_dict'):
                params['monthly_bill_no'] = self.monthly_bill_no.to_alipay_dict()
            else:
                params['monthly_bill_no'] = self.monthly_bill_no
        if self.paid_amt:
            if hasattr(self.paid_amt, 'to_alipay_dict'):
                params['paid_amt'] = self.paid_amt.to_alipay_dict()
            else:
                params['paid_amt'] = self.paid_amt
        if self.past_pay_flag:
            if hasattr(self.past_pay_flag, 'to_alipay_dict'):
                params['past_pay_flag'] = self.past_pay_flag.to_alipay_dict()
            else:
                params['past_pay_flag'] = self.past_pay_flag
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
        if self.payable_amt:
            if hasattr(self.payable_amt, 'to_alipay_dict'):
                params['payable_amt'] = self.payable_amt.to_alipay_dict()
            else:
                params['payable_amt'] = self.payable_amt
        if self.payable_flag:
            if hasattr(self.payable_flag, 'to_alipay_dict'):
                params['payable_flag'] = self.payable_flag.to_alipay_dict()
            else:
                params['payable_flag'] = self.payable_flag
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.price_policy_id:
            if hasattr(self.price_policy_id, 'to_alipay_dict'):
                params['price_policy_id'] = self.price_policy_id.to_alipay_dict()
            else:
                params['price_policy_id'] = self.price_policy_id
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.received_amt:
            if hasattr(self.received_amt, 'to_alipay_dict'):
                params['received_amt'] = self.received_amt.to_alipay_dict()
            else:
                params['received_amt'] = self.received_amt
        if self.rel_rcpt_list:
            if isinstance(self.rel_rcpt_list, list):
                for i in range(0, len(self.rel_rcpt_list)):
                    element = self.rel_rcpt_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rel_rcpt_list[i] = element.to_alipay_dict()
            if hasattr(self.rel_rcpt_list, 'to_alipay_dict'):
                params['rel_rcpt_list'] = self.rel_rcpt_list.to_alipay_dict()
            else:
                params['rel_rcpt_list'] = self.rel_rcpt_list
        if self.settle_period:
            if hasattr(self.settle_period, 'to_alipay_dict'):
                params['settle_period'] = self.settle_period.to_alipay_dict()
            else:
                params['settle_period'] = self.settle_period
        if self.settle_time_zone:
            if hasattr(self.settle_time_zone, 'to_alipay_dict'):
                params['settle_time_zone'] = self.settle_time_zone.to_alipay_dict()
            else:
                params['settle_time_zone'] = self.settle_time_zone
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
        if self.sign_ip_id_name:
            if hasattr(self.sign_ip_id_name, 'to_alipay_dict'):
                params['sign_ip_id_name'] = self.sign_ip_id_name.to_alipay_dict()
            else:
                params['sign_ip_id_name'] = self.sign_ip_id_name
        if self.sign_ip_role_id:
            if hasattr(self.sign_ip_role_id, 'to_alipay_dict'):
                params['sign_ip_role_id'] = self.sign_ip_role_id.to_alipay_dict()
            else:
                params['sign_ip_role_id'] = self.sign_ip_role_id
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
        if self.tax_tp:
            if hasattr(self.tax_tp, 'to_alipay_dict'):
                params['tax_tp'] = self.tax_tp.to_alipay_dict()
            else:
                params['tax_tp'] = self.tax_tp
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
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
        if self.type_name:
            if hasattr(self.type_name, 'to_alipay_dict'):
                params['type_name'] = self.type_name.to_alipay_dict()
            else:
                params['type_name'] = self.type_name
        if self.writeoff_detail_count:
            if hasattr(self.writeoff_detail_count, 'to_alipay_dict'):
                params['writeoff_detail_count'] = self.writeoff_detail_count.to_alipay_dict()
            else:
                params['writeoff_detail_count'] = self.writeoff_detail_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArMonthlyStatementBillOpenApiResponse()
        if 'accounting_time_zone' in d:
            o.accounting_time_zone = d['accounting_time_zone']
        if 'accrued_date' in d:
            o.accrued_date = d['accrued_date']
        if 'adjust_amt' in d:
            o.adjust_amt = d['adjust_amt']
        if 'analysis_dmsn' in d:
            o.analysis_dmsn = d['analysis_dmsn']
        if 'analysis_dmsn_1' in d:
            o.analysis_dmsn_1 = d['analysis_dmsn_1']
        if 'analysis_dmsn_2' in d:
            o.analysis_dmsn_2 = d['analysis_dmsn_2']
        if 'analysis_dmsn_3' in d:
            o.analysis_dmsn_3 = d['analysis_dmsn_3']
        if 'analysis_dmsn_4' in d:
            o.analysis_dmsn_4 = d['analysis_dmsn_4']
        if 'applying_invoice_amt' in d:
            o.applying_invoice_amt = d['applying_invoice_amt']
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
        if 'charge_item_code' in d:
            o.charge_item_code = d['charge_item_code']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'charge_type_name' in d:
            o.charge_type_name = d['charge_type_name']
        if 'check_state' in d:
            o.check_state = d['check_state']
        if 'clcn_basic_amt' in d:
            o.clcn_basic_amt = d['clcn_basic_amt']
        if 'clcn_basic_type' in d:
            o.clcn_basic_type = d['clcn_basic_type']
        if 'clcn_basic_type_name' in d:
            o.clcn_basic_type_name = d['clcn_basic_type_name']
        if 'clcn_method' in d:
            o.clcn_method = d['clcn_method']
        if 'clcn_method_name' in d:
            o.clcn_method_name = d['clcn_method_name']
        if 'detail_bill_adj_amt' in d:
            o.detail_bill_adj_amt = d['detail_bill_adj_amt']
        if 'detail_bill_adj_reason' in d:
            o.detail_bill_adj_reason = d['detail_bill_adj_reason']
        if 'env_source' in d:
            o.env_source = d['env_source']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inter_trade_flag' in d:
            o.inter_trade_flag = d['inter_trade_flag']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'link_invoice_amt' in d:
            o.link_invoice_amt = d['link_invoice_amt']
        if 'memo' in d:
            o.memo = d['memo']
        if 'metadata_source' in d:
            o.metadata_source = d['metadata_source']
        if 'monthly_bill_no' in d:
            o.monthly_bill_no = d['monthly_bill_no']
        if 'paid_amt' in d:
            o.paid_amt = d['paid_amt']
        if 'past_pay_flag' in d:
            o.past_pay_flag = d['past_pay_flag']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_way' in d:
            o.pay_way = d['pay_way']
        if 'payable_amt' in d:
            o.payable_amt = d['payable_amt']
        if 'payable_flag' in d:
            o.payable_flag = d['payable_flag']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'price_policy_id' in d:
            o.price_policy_id = d['price_policy_id']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'received_amt' in d:
            o.received_amt = d['received_amt']
        if 'rel_rcpt_list' in d:
            o.rel_rcpt_list = d['rel_rcpt_list']
        if 'settle_period' in d:
            o.settle_period = d['settle_period']
        if 'settle_time_zone' in d:
            o.settle_time_zone = d['settle_time_zone']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'sign_ip_id' in d:
            o.sign_ip_id = d['sign_ip_id']
        if 'sign_ip_id_name' in d:
            o.sign_ip_id_name = d['sign_ip_id_name']
        if 'sign_ip_role_id' in d:
            o.sign_ip_role_id = d['sign_ip_role_id']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_tp' in d:
            o.tax_tp = d['tax_tp']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'to_writeoff_detail_count' in d:
            o.to_writeoff_detail_count = d['to_writeoff_detail_count']
        if 'type' in d:
            o.type = d['type']
        if 'type_name' in d:
            o.type_name = d['type_name']
        if 'writeoff_detail_count' in d:
            o.writeoff_detail_count = d['writeoff_detail_count']
        return o



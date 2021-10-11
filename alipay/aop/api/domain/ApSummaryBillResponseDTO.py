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
from alipay.aop.api.domain.MapTypeParam import MapTypeParam
from alipay.aop.api.domain.MapTypeParam import MapTypeParam
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ApSummaryBillResponseDTO(object):

    def __init__(self):
        self._adjust_amount = None
        self._arrangement_no = None
        self._auto_confirm_date = None
        self._bill_amount = None
        self._bill_end_date = None
        self._bill_month = None
        self._bill_no = None
        self._bill_start_date = None
        self._bill_status = None
        self._bill_status_name = None
        self._biz_module = None
        self._biz_pd_code = None
        self._ccy = None
        self._ccy_code = None
        self._charge_item_code = None
        self._charge_off_period = None
        self._charge_off_period_type = None
        self._charge_off_period_type_name = None
        self._check_date = None
        self._clcn_basic_amount = None
        self._clcn_basic_type = None
        self._clcn_basic_type_name = None
        self._confirmed_amount = None
        self._exclude_tax_amount = None
        self._fund_settle_time = None
        self._inner_trade_flag = None
        self._inst_id = None
        self._invoice_status_desc = None
        self._invoiced_amount = None
        self._invoiced_amt = None
        self._payee_account_ext_info = None
        self._payee_account_no = None
        self._payee_account_type = None
        self._payee_account_type_name = None
        self._payee_ip_role_id = None
        self._payee_ip_role_id_source = None
        self._payer_account_ext_info = None
        self._payer_account_no = None
        self._payer_account_type = None
        self._payer_account_type_name = None
        self._payer_ip_role_id = None
        self._payer_ip_role_id_source = None
        self._real_bill_amount = None
        self._reconciliation_status = None
        self._reconciliation_status_name = None
        self._sales_product_code = None
        self._sales_product_name = None
        self._settle_biz_type = None
        self._settle_biz_type_name = None
        self._settle_ip_role_id = None
        self._settle_ip_role_id_source = None
        self._settle_ip_role_name = None
        self._settle_merchant_id = None
        self._settle_merchant_id_source = None
        self._settle_merchant_name = None
        self._settle_status = None
        self._settle_status_name = None
        self._settle_time_type = None
        self._settle_time_type_name = None
        self._settled_amount = None
        self._sign_ip_role_id = None
        self._sign_ip_role_id_source = None
        self._sign_merchant_id = None
        self._sign_merchant_id_source = None
        self._summary_dmsn_1 = None
        self._summary_dmsn_2 = None
        self._summary_dmsn_3 = None
        self._summary_dmsn_4 = None
        self._summary_dmsn_5 = None
        self._summary_dmsn_6 = None
        self._summary_dmsn_7 = None
        self._summary_dmsn_value = None
        self._tax_amount = None
        self._tax_rate = None
        self._tax_type = None
        self._tnt_inst_id = None
        self._un_confirmed_amount = None
        self._un_invoice_amt = None
        self._un_settled_amount = None
        self._version_flag = None

    @property
    def adjust_amount(self):
        return self._adjust_amount

    @adjust_amount.setter
    def adjust_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._adjust_amount = value
        else:
            self._adjust_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def auto_confirm_date(self):
        return self._auto_confirm_date

    @auto_confirm_date.setter
    def auto_confirm_date(self, value):
        self._auto_confirm_date = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amount = value
        else:
            self._bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def bill_status_name(self):
        return self._bill_status_name

    @bill_status_name.setter
    def bill_status_name(self, value):
        self._bill_status_name = value
    @property
    def biz_module(self):
        return self._biz_module

    @biz_module.setter
    def biz_module(self, value):
        self._biz_module = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def ccy(self):
        return self._ccy

    @ccy.setter
    def ccy(self, value):
        self._ccy = value
    @property
    def ccy_code(self):
        return self._ccy_code

    @ccy_code.setter
    def ccy_code(self, value):
        self._ccy_code = value
    @property
    def charge_item_code(self):
        return self._charge_item_code

    @charge_item_code.setter
    def charge_item_code(self, value):
        self._charge_item_code = value
    @property
    def charge_off_period(self):
        return self._charge_off_period

    @charge_off_period.setter
    def charge_off_period(self, value):
        self._charge_off_period = value
    @property
    def charge_off_period_type(self):
        return self._charge_off_period_type

    @charge_off_period_type.setter
    def charge_off_period_type(self, value):
        self._charge_off_period_type = value
    @property
    def charge_off_period_type_name(self):
        return self._charge_off_period_type_name

    @charge_off_period_type_name.setter
    def charge_off_period_type_name(self, value):
        self._charge_off_period_type_name = value
    @property
    def check_date(self):
        return self._check_date

    @check_date.setter
    def check_date(self, value):
        self._check_date = value
    @property
    def clcn_basic_amount(self):
        return self._clcn_basic_amount

    @clcn_basic_amount.setter
    def clcn_basic_amount(self, value):
        self._clcn_basic_amount = value
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
    def confirmed_amount(self):
        return self._confirmed_amount

    @confirmed_amount.setter
    def confirmed_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._confirmed_amount = value
        else:
            self._confirmed_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def exclude_tax_amount(self):
        return self._exclude_tax_amount

    @exclude_tax_amount.setter
    def exclude_tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._exclude_tax_amount = value
        else:
            self._exclude_tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def fund_settle_time(self):
        return self._fund_settle_time

    @fund_settle_time.setter
    def fund_settle_time(self, value):
        self._fund_settle_time = value
    @property
    def inner_trade_flag(self):
        return self._inner_trade_flag

    @inner_trade_flag.setter
    def inner_trade_flag(self, value):
        self._inner_trade_flag = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_status_desc(self):
        return self._invoice_status_desc

    @invoice_status_desc.setter
    def invoice_status_desc(self, value):
        self._invoice_status_desc = value
    @property
    def invoiced_amount(self):
        return self._invoiced_amount

    @invoiced_amount.setter
    def invoiced_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoiced_amount = value
        else:
            self._invoiced_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def payee_account_ext_info(self):
        return self._payee_account_ext_info

    @payee_account_ext_info.setter
    def payee_account_ext_info(self, value):
        if isinstance(value, MapTypeParam):
            self._payee_account_ext_info = value
        else:
            self._payee_account_ext_info = MapTypeParam.from_alipay_dict(value)
    @property
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_account_type_name(self):
        return self._payee_account_type_name

    @payee_account_type_name.setter
    def payee_account_type_name(self, value):
        self._payee_account_type_name = value
    @property
    def payee_ip_role_id(self):
        return self._payee_ip_role_id

    @payee_ip_role_id.setter
    def payee_ip_role_id(self, value):
        self._payee_ip_role_id = value
    @property
    def payee_ip_role_id_source(self):
        return self._payee_ip_role_id_source

    @payee_ip_role_id_source.setter
    def payee_ip_role_id_source(self, value):
        self._payee_ip_role_id_source = value
    @property
    def payer_account_ext_info(self):
        return self._payer_account_ext_info

    @payer_account_ext_info.setter
    def payer_account_ext_info(self, value):
        if isinstance(value, MapTypeParam):
            self._payer_account_ext_info = value
        else:
            self._payer_account_ext_info = MapTypeParam.from_alipay_dict(value)
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def payer_account_type_name(self):
        return self._payer_account_type_name

    @payer_account_type_name.setter
    def payer_account_type_name(self, value):
        self._payer_account_type_name = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def payer_ip_role_id_source(self):
        return self._payer_ip_role_id_source

    @payer_ip_role_id_source.setter
    def payer_ip_role_id_source(self, value):
        self._payer_ip_role_id_source = value
    @property
    def real_bill_amount(self):
        return self._real_bill_amount

    @real_bill_amount.setter
    def real_bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._real_bill_amount = value
        else:
            self._real_bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def reconciliation_status(self):
        return self._reconciliation_status

    @reconciliation_status.setter
    def reconciliation_status(self, value):
        self._reconciliation_status = value
    @property
    def reconciliation_status_name(self):
        return self._reconciliation_status_name

    @reconciliation_status_name.setter
    def reconciliation_status_name(self, value):
        self._reconciliation_status_name = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def sales_product_name(self):
        return self._sales_product_name

    @sales_product_name.setter
    def sales_product_name(self, value):
        self._sales_product_name = value
    @property
    def settle_biz_type(self):
        return self._settle_biz_type

    @settle_biz_type.setter
    def settle_biz_type(self, value):
        self._settle_biz_type = value
    @property
    def settle_biz_type_name(self):
        return self._settle_biz_type_name

    @settle_biz_type_name.setter
    def settle_biz_type_name(self, value):
        self._settle_biz_type_name = value
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def settle_ip_role_id_source(self):
        return self._settle_ip_role_id_source

    @settle_ip_role_id_source.setter
    def settle_ip_role_id_source(self, value):
        self._settle_ip_role_id_source = value
    @property
    def settle_ip_role_name(self):
        return self._settle_ip_role_name

    @settle_ip_role_name.setter
    def settle_ip_role_name(self, value):
        self._settle_ip_role_name = value
    @property
    def settle_merchant_id(self):
        return self._settle_merchant_id

    @settle_merchant_id.setter
    def settle_merchant_id(self, value):
        self._settle_merchant_id = value
    @property
    def settle_merchant_id_source(self):
        return self._settle_merchant_id_source

    @settle_merchant_id_source.setter
    def settle_merchant_id_source(self, value):
        self._settle_merchant_id_source = value
    @property
    def settle_merchant_name(self):
        return self._settle_merchant_name

    @settle_merchant_name.setter
    def settle_merchant_name(self, value):
        self._settle_merchant_name = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_status_name(self):
        return self._settle_status_name

    @settle_status_name.setter
    def settle_status_name(self, value):
        self._settle_status_name = value
    @property
    def settle_time_type(self):
        return self._settle_time_type

    @settle_time_type.setter
    def settle_time_type(self, value):
        self._settle_time_type = value
    @property
    def settle_time_type_name(self):
        return self._settle_time_type_name

    @settle_time_type_name.setter
    def settle_time_type_name(self, value):
        self._settle_time_type_name = value
    @property
    def settled_amount(self):
        return self._settled_amount

    @settled_amount.setter
    def settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settled_amount = value
        else:
            self._settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def sign_ip_role_id(self):
        return self._sign_ip_role_id

    @sign_ip_role_id.setter
    def sign_ip_role_id(self, value):
        self._sign_ip_role_id = value
    @property
    def sign_ip_role_id_source(self):
        return self._sign_ip_role_id_source

    @sign_ip_role_id_source.setter
    def sign_ip_role_id_source(self, value):
        self._sign_ip_role_id_source = value
    @property
    def sign_merchant_id(self):
        return self._sign_merchant_id

    @sign_merchant_id.setter
    def sign_merchant_id(self, value):
        self._sign_merchant_id = value
    @property
    def sign_merchant_id_source(self):
        return self._sign_merchant_id_source

    @sign_merchant_id_source.setter
    def sign_merchant_id_source(self, value):
        self._sign_merchant_id_source = value
    @property
    def summary_dmsn_1(self):
        return self._summary_dmsn_1

    @summary_dmsn_1.setter
    def summary_dmsn_1(self, value):
        self._summary_dmsn_1 = value
    @property
    def summary_dmsn_2(self):
        return self._summary_dmsn_2

    @summary_dmsn_2.setter
    def summary_dmsn_2(self, value):
        self._summary_dmsn_2 = value
    @property
    def summary_dmsn_3(self):
        return self._summary_dmsn_3

    @summary_dmsn_3.setter
    def summary_dmsn_3(self, value):
        self._summary_dmsn_3 = value
    @property
    def summary_dmsn_4(self):
        return self._summary_dmsn_4

    @summary_dmsn_4.setter
    def summary_dmsn_4(self, value):
        self._summary_dmsn_4 = value
    @property
    def summary_dmsn_5(self):
        return self._summary_dmsn_5

    @summary_dmsn_5.setter
    def summary_dmsn_5(self, value):
        self._summary_dmsn_5 = value
    @property
    def summary_dmsn_6(self):
        return self._summary_dmsn_6

    @summary_dmsn_6.setter
    def summary_dmsn_6(self, value):
        self._summary_dmsn_6 = value
    @property
    def summary_dmsn_7(self):
        return self._summary_dmsn_7

    @summary_dmsn_7.setter
    def summary_dmsn_7(self, value):
        self._summary_dmsn_7 = value
    @property
    def summary_dmsn_value(self):
        return self._summary_dmsn_value

    @summary_dmsn_value.setter
    def summary_dmsn_value(self, value):
        self._summary_dmsn_value = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amount = value
        else:
            self._tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def un_confirmed_amount(self):
        return self._un_confirmed_amount

    @un_confirmed_amount.setter
    def un_confirmed_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_confirmed_amount = value
        else:
            self._un_confirmed_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def un_invoice_amt(self):
        return self._un_invoice_amt

    @un_invoice_amt.setter
    def un_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_invoice_amt = value
        else:
            self._un_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def un_settled_amount(self):
        return self._un_settled_amount

    @un_settled_amount.setter
    def un_settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_settled_amount = value
        else:
            self._un_settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def version_flag(self):
        return self._version_flag

    @version_flag.setter
    def version_flag(self, value):
        self._version_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_amount:
            if hasattr(self.adjust_amount, 'to_alipay_dict'):
                params['adjust_amount'] = self.adjust_amount.to_alipay_dict()
            else:
                params['adjust_amount'] = self.adjust_amount
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.auto_confirm_date:
            if hasattr(self.auto_confirm_date, 'to_alipay_dict'):
                params['auto_confirm_date'] = self.auto_confirm_date.to_alipay_dict()
            else:
                params['auto_confirm_date'] = self.auto_confirm_date
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
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
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.bill_status_name:
            if hasattr(self.bill_status_name, 'to_alipay_dict'):
                params['bill_status_name'] = self.bill_status_name.to_alipay_dict()
            else:
                params['bill_status_name'] = self.bill_status_name
        if self.biz_module:
            if hasattr(self.biz_module, 'to_alipay_dict'):
                params['biz_module'] = self.biz_module.to_alipay_dict()
            else:
                params['biz_module'] = self.biz_module
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.ccy:
            if hasattr(self.ccy, 'to_alipay_dict'):
                params['ccy'] = self.ccy.to_alipay_dict()
            else:
                params['ccy'] = self.ccy
        if self.ccy_code:
            if hasattr(self.ccy_code, 'to_alipay_dict'):
                params['ccy_code'] = self.ccy_code.to_alipay_dict()
            else:
                params['ccy_code'] = self.ccy_code
        if self.charge_item_code:
            if hasattr(self.charge_item_code, 'to_alipay_dict'):
                params['charge_item_code'] = self.charge_item_code.to_alipay_dict()
            else:
                params['charge_item_code'] = self.charge_item_code
        if self.charge_off_period:
            if hasattr(self.charge_off_period, 'to_alipay_dict'):
                params['charge_off_period'] = self.charge_off_period.to_alipay_dict()
            else:
                params['charge_off_period'] = self.charge_off_period
        if self.charge_off_period_type:
            if hasattr(self.charge_off_period_type, 'to_alipay_dict'):
                params['charge_off_period_type'] = self.charge_off_period_type.to_alipay_dict()
            else:
                params['charge_off_period_type'] = self.charge_off_period_type
        if self.charge_off_period_type_name:
            if hasattr(self.charge_off_period_type_name, 'to_alipay_dict'):
                params['charge_off_period_type_name'] = self.charge_off_period_type_name.to_alipay_dict()
            else:
                params['charge_off_period_type_name'] = self.charge_off_period_type_name
        if self.check_date:
            if hasattr(self.check_date, 'to_alipay_dict'):
                params['check_date'] = self.check_date.to_alipay_dict()
            else:
                params['check_date'] = self.check_date
        if self.clcn_basic_amount:
            if hasattr(self.clcn_basic_amount, 'to_alipay_dict'):
                params['clcn_basic_amount'] = self.clcn_basic_amount.to_alipay_dict()
            else:
                params['clcn_basic_amount'] = self.clcn_basic_amount
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
        if self.confirmed_amount:
            if hasattr(self.confirmed_amount, 'to_alipay_dict'):
                params['confirmed_amount'] = self.confirmed_amount.to_alipay_dict()
            else:
                params['confirmed_amount'] = self.confirmed_amount
        if self.exclude_tax_amount:
            if hasattr(self.exclude_tax_amount, 'to_alipay_dict'):
                params['exclude_tax_amount'] = self.exclude_tax_amount.to_alipay_dict()
            else:
                params['exclude_tax_amount'] = self.exclude_tax_amount
        if self.fund_settle_time:
            if hasattr(self.fund_settle_time, 'to_alipay_dict'):
                params['fund_settle_time'] = self.fund_settle_time.to_alipay_dict()
            else:
                params['fund_settle_time'] = self.fund_settle_time
        if self.inner_trade_flag:
            if hasattr(self.inner_trade_flag, 'to_alipay_dict'):
                params['inner_trade_flag'] = self.inner_trade_flag.to_alipay_dict()
            else:
                params['inner_trade_flag'] = self.inner_trade_flag
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_status_desc:
            if hasattr(self.invoice_status_desc, 'to_alipay_dict'):
                params['invoice_status_desc'] = self.invoice_status_desc.to_alipay_dict()
            else:
                params['invoice_status_desc'] = self.invoice_status_desc
        if self.invoiced_amount:
            if hasattr(self.invoiced_amount, 'to_alipay_dict'):
                params['invoiced_amount'] = self.invoiced_amount.to_alipay_dict()
            else:
                params['invoiced_amount'] = self.invoiced_amount
        if self.invoiced_amt:
            if hasattr(self.invoiced_amt, 'to_alipay_dict'):
                params['invoiced_amt'] = self.invoiced_amt.to_alipay_dict()
            else:
                params['invoiced_amt'] = self.invoiced_amt
        if self.payee_account_ext_info:
            if hasattr(self.payee_account_ext_info, 'to_alipay_dict'):
                params['payee_account_ext_info'] = self.payee_account_ext_info.to_alipay_dict()
            else:
                params['payee_account_ext_info'] = self.payee_account_ext_info
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_account_type_name:
            if hasattr(self.payee_account_type_name, 'to_alipay_dict'):
                params['payee_account_type_name'] = self.payee_account_type_name.to_alipay_dict()
            else:
                params['payee_account_type_name'] = self.payee_account_type_name
        if self.payee_ip_role_id:
            if hasattr(self.payee_ip_role_id, 'to_alipay_dict'):
                params['payee_ip_role_id'] = self.payee_ip_role_id.to_alipay_dict()
            else:
                params['payee_ip_role_id'] = self.payee_ip_role_id
        if self.payee_ip_role_id_source:
            if hasattr(self.payee_ip_role_id_source, 'to_alipay_dict'):
                params['payee_ip_role_id_source'] = self.payee_ip_role_id_source.to_alipay_dict()
            else:
                params['payee_ip_role_id_source'] = self.payee_ip_role_id_source
        if self.payer_account_ext_info:
            if hasattr(self.payer_account_ext_info, 'to_alipay_dict'):
                params['payer_account_ext_info'] = self.payer_account_ext_info.to_alipay_dict()
            else:
                params['payer_account_ext_info'] = self.payer_account_ext_info
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.payer_account_type_name:
            if hasattr(self.payer_account_type_name, 'to_alipay_dict'):
                params['payer_account_type_name'] = self.payer_account_type_name.to_alipay_dict()
            else:
                params['payer_account_type_name'] = self.payer_account_type_name
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.payer_ip_role_id_source:
            if hasattr(self.payer_ip_role_id_source, 'to_alipay_dict'):
                params['payer_ip_role_id_source'] = self.payer_ip_role_id_source.to_alipay_dict()
            else:
                params['payer_ip_role_id_source'] = self.payer_ip_role_id_source
        if self.real_bill_amount:
            if hasattr(self.real_bill_amount, 'to_alipay_dict'):
                params['real_bill_amount'] = self.real_bill_amount.to_alipay_dict()
            else:
                params['real_bill_amount'] = self.real_bill_amount
        if self.reconciliation_status:
            if hasattr(self.reconciliation_status, 'to_alipay_dict'):
                params['reconciliation_status'] = self.reconciliation_status.to_alipay_dict()
            else:
                params['reconciliation_status'] = self.reconciliation_status
        if self.reconciliation_status_name:
            if hasattr(self.reconciliation_status_name, 'to_alipay_dict'):
                params['reconciliation_status_name'] = self.reconciliation_status_name.to_alipay_dict()
            else:
                params['reconciliation_status_name'] = self.reconciliation_status_name
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.sales_product_name:
            if hasattr(self.sales_product_name, 'to_alipay_dict'):
                params['sales_product_name'] = self.sales_product_name.to_alipay_dict()
            else:
                params['sales_product_name'] = self.sales_product_name
        if self.settle_biz_type:
            if hasattr(self.settle_biz_type, 'to_alipay_dict'):
                params['settle_biz_type'] = self.settle_biz_type.to_alipay_dict()
            else:
                params['settle_biz_type'] = self.settle_biz_type
        if self.settle_biz_type_name:
            if hasattr(self.settle_biz_type_name, 'to_alipay_dict'):
                params['settle_biz_type_name'] = self.settle_biz_type_name.to_alipay_dict()
            else:
                params['settle_biz_type_name'] = self.settle_biz_type_name
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.settle_ip_role_id_source:
            if hasattr(self.settle_ip_role_id_source, 'to_alipay_dict'):
                params['settle_ip_role_id_source'] = self.settle_ip_role_id_source.to_alipay_dict()
            else:
                params['settle_ip_role_id_source'] = self.settle_ip_role_id_source
        if self.settle_ip_role_name:
            if hasattr(self.settle_ip_role_name, 'to_alipay_dict'):
                params['settle_ip_role_name'] = self.settle_ip_role_name.to_alipay_dict()
            else:
                params['settle_ip_role_name'] = self.settle_ip_role_name
        if self.settle_merchant_id:
            if hasattr(self.settle_merchant_id, 'to_alipay_dict'):
                params['settle_merchant_id'] = self.settle_merchant_id.to_alipay_dict()
            else:
                params['settle_merchant_id'] = self.settle_merchant_id
        if self.settle_merchant_id_source:
            if hasattr(self.settle_merchant_id_source, 'to_alipay_dict'):
                params['settle_merchant_id_source'] = self.settle_merchant_id_source.to_alipay_dict()
            else:
                params['settle_merchant_id_source'] = self.settle_merchant_id_source
        if self.settle_merchant_name:
            if hasattr(self.settle_merchant_name, 'to_alipay_dict'):
                params['settle_merchant_name'] = self.settle_merchant_name.to_alipay_dict()
            else:
                params['settle_merchant_name'] = self.settle_merchant_name
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_status_name:
            if hasattr(self.settle_status_name, 'to_alipay_dict'):
                params['settle_status_name'] = self.settle_status_name.to_alipay_dict()
            else:
                params['settle_status_name'] = self.settle_status_name
        if self.settle_time_type:
            if hasattr(self.settle_time_type, 'to_alipay_dict'):
                params['settle_time_type'] = self.settle_time_type.to_alipay_dict()
            else:
                params['settle_time_type'] = self.settle_time_type
        if self.settle_time_type_name:
            if hasattr(self.settle_time_type_name, 'to_alipay_dict'):
                params['settle_time_type_name'] = self.settle_time_type_name.to_alipay_dict()
            else:
                params['settle_time_type_name'] = self.settle_time_type_name
        if self.settled_amount:
            if hasattr(self.settled_amount, 'to_alipay_dict'):
                params['settled_amount'] = self.settled_amount.to_alipay_dict()
            else:
                params['settled_amount'] = self.settled_amount
        if self.sign_ip_role_id:
            if hasattr(self.sign_ip_role_id, 'to_alipay_dict'):
                params['sign_ip_role_id'] = self.sign_ip_role_id.to_alipay_dict()
            else:
                params['sign_ip_role_id'] = self.sign_ip_role_id
        if self.sign_ip_role_id_source:
            if hasattr(self.sign_ip_role_id_source, 'to_alipay_dict'):
                params['sign_ip_role_id_source'] = self.sign_ip_role_id_source.to_alipay_dict()
            else:
                params['sign_ip_role_id_source'] = self.sign_ip_role_id_source
        if self.sign_merchant_id:
            if hasattr(self.sign_merchant_id, 'to_alipay_dict'):
                params['sign_merchant_id'] = self.sign_merchant_id.to_alipay_dict()
            else:
                params['sign_merchant_id'] = self.sign_merchant_id
        if self.sign_merchant_id_source:
            if hasattr(self.sign_merchant_id_source, 'to_alipay_dict'):
                params['sign_merchant_id_source'] = self.sign_merchant_id_source.to_alipay_dict()
            else:
                params['sign_merchant_id_source'] = self.sign_merchant_id_source
        if self.summary_dmsn_1:
            if hasattr(self.summary_dmsn_1, 'to_alipay_dict'):
                params['summary_dmsn_1'] = self.summary_dmsn_1.to_alipay_dict()
            else:
                params['summary_dmsn_1'] = self.summary_dmsn_1
        if self.summary_dmsn_2:
            if hasattr(self.summary_dmsn_2, 'to_alipay_dict'):
                params['summary_dmsn_2'] = self.summary_dmsn_2.to_alipay_dict()
            else:
                params['summary_dmsn_2'] = self.summary_dmsn_2
        if self.summary_dmsn_3:
            if hasattr(self.summary_dmsn_3, 'to_alipay_dict'):
                params['summary_dmsn_3'] = self.summary_dmsn_3.to_alipay_dict()
            else:
                params['summary_dmsn_3'] = self.summary_dmsn_3
        if self.summary_dmsn_4:
            if hasattr(self.summary_dmsn_4, 'to_alipay_dict'):
                params['summary_dmsn_4'] = self.summary_dmsn_4.to_alipay_dict()
            else:
                params['summary_dmsn_4'] = self.summary_dmsn_4
        if self.summary_dmsn_5:
            if hasattr(self.summary_dmsn_5, 'to_alipay_dict'):
                params['summary_dmsn_5'] = self.summary_dmsn_5.to_alipay_dict()
            else:
                params['summary_dmsn_5'] = self.summary_dmsn_5
        if self.summary_dmsn_6:
            if hasattr(self.summary_dmsn_6, 'to_alipay_dict'):
                params['summary_dmsn_6'] = self.summary_dmsn_6.to_alipay_dict()
            else:
                params['summary_dmsn_6'] = self.summary_dmsn_6
        if self.summary_dmsn_7:
            if hasattr(self.summary_dmsn_7, 'to_alipay_dict'):
                params['summary_dmsn_7'] = self.summary_dmsn_7.to_alipay_dict()
            else:
                params['summary_dmsn_7'] = self.summary_dmsn_7
        if self.summary_dmsn_value:
            if hasattr(self.summary_dmsn_value, 'to_alipay_dict'):
                params['summary_dmsn_value'] = self.summary_dmsn_value.to_alipay_dict()
            else:
                params['summary_dmsn_value'] = self.summary_dmsn_value
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
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
        if self.un_confirmed_amount:
            if hasattr(self.un_confirmed_amount, 'to_alipay_dict'):
                params['un_confirmed_amount'] = self.un_confirmed_amount.to_alipay_dict()
            else:
                params['un_confirmed_amount'] = self.un_confirmed_amount
        if self.un_invoice_amt:
            if hasattr(self.un_invoice_amt, 'to_alipay_dict'):
                params['un_invoice_amt'] = self.un_invoice_amt.to_alipay_dict()
            else:
                params['un_invoice_amt'] = self.un_invoice_amt
        if self.un_settled_amount:
            if hasattr(self.un_settled_amount, 'to_alipay_dict'):
                params['un_settled_amount'] = self.un_settled_amount.to_alipay_dict()
            else:
                params['un_settled_amount'] = self.un_settled_amount
        if self.version_flag:
            if hasattr(self.version_flag, 'to_alipay_dict'):
                params['version_flag'] = self.version_flag.to_alipay_dict()
            else:
                params['version_flag'] = self.version_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApSummaryBillResponseDTO()
        if 'adjust_amount' in d:
            o.adjust_amount = d['adjust_amount']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'auto_confirm_date' in d:
            o.auto_confirm_date = d['auto_confirm_date']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_end_date' in d:
            o.bill_end_date = d['bill_end_date']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_start_date' in d:
            o.bill_start_date = d['bill_start_date']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'bill_status_name' in d:
            o.bill_status_name = d['bill_status_name']
        if 'biz_module' in d:
            o.biz_module = d['biz_module']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'ccy' in d:
            o.ccy = d['ccy']
        if 'ccy_code' in d:
            o.ccy_code = d['ccy_code']
        if 'charge_item_code' in d:
            o.charge_item_code = d['charge_item_code']
        if 'charge_off_period' in d:
            o.charge_off_period = d['charge_off_period']
        if 'charge_off_period_type' in d:
            o.charge_off_period_type = d['charge_off_period_type']
        if 'charge_off_period_type_name' in d:
            o.charge_off_period_type_name = d['charge_off_period_type_name']
        if 'check_date' in d:
            o.check_date = d['check_date']
        if 'clcn_basic_amount' in d:
            o.clcn_basic_amount = d['clcn_basic_amount']
        if 'clcn_basic_type' in d:
            o.clcn_basic_type = d['clcn_basic_type']
        if 'clcn_basic_type_name' in d:
            o.clcn_basic_type_name = d['clcn_basic_type_name']
        if 'confirmed_amount' in d:
            o.confirmed_amount = d['confirmed_amount']
        if 'exclude_tax_amount' in d:
            o.exclude_tax_amount = d['exclude_tax_amount']
        if 'fund_settle_time' in d:
            o.fund_settle_time = d['fund_settle_time']
        if 'inner_trade_flag' in d:
            o.inner_trade_flag = d['inner_trade_flag']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_status_desc' in d:
            o.invoice_status_desc = d['invoice_status_desc']
        if 'invoiced_amount' in d:
            o.invoiced_amount = d['invoiced_amount']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'payee_account_ext_info' in d:
            o.payee_account_ext_info = d['payee_account_ext_info']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_account_type_name' in d:
            o.payee_account_type_name = d['payee_account_type_name']
        if 'payee_ip_role_id' in d:
            o.payee_ip_role_id = d['payee_ip_role_id']
        if 'payee_ip_role_id_source' in d:
            o.payee_ip_role_id_source = d['payee_ip_role_id_source']
        if 'payer_account_ext_info' in d:
            o.payer_account_ext_info = d['payer_account_ext_info']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'payer_account_type_name' in d:
            o.payer_account_type_name = d['payer_account_type_name']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'payer_ip_role_id_source' in d:
            o.payer_ip_role_id_source = d['payer_ip_role_id_source']
        if 'real_bill_amount' in d:
            o.real_bill_amount = d['real_bill_amount']
        if 'reconciliation_status' in d:
            o.reconciliation_status = d['reconciliation_status']
        if 'reconciliation_status_name' in d:
            o.reconciliation_status_name = d['reconciliation_status_name']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'sales_product_name' in d:
            o.sales_product_name = d['sales_product_name']
        if 'settle_biz_type' in d:
            o.settle_biz_type = d['settle_biz_type']
        if 'settle_biz_type_name' in d:
            o.settle_biz_type_name = d['settle_biz_type_name']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'settle_ip_role_id_source' in d:
            o.settle_ip_role_id_source = d['settle_ip_role_id_source']
        if 'settle_ip_role_name' in d:
            o.settle_ip_role_name = d['settle_ip_role_name']
        if 'settle_merchant_id' in d:
            o.settle_merchant_id = d['settle_merchant_id']
        if 'settle_merchant_id_source' in d:
            o.settle_merchant_id_source = d['settle_merchant_id_source']
        if 'settle_merchant_name' in d:
            o.settle_merchant_name = d['settle_merchant_name']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_status_name' in d:
            o.settle_status_name = d['settle_status_name']
        if 'settle_time_type' in d:
            o.settle_time_type = d['settle_time_type']
        if 'settle_time_type_name' in d:
            o.settle_time_type_name = d['settle_time_type_name']
        if 'settled_amount' in d:
            o.settled_amount = d['settled_amount']
        if 'sign_ip_role_id' in d:
            o.sign_ip_role_id = d['sign_ip_role_id']
        if 'sign_ip_role_id_source' in d:
            o.sign_ip_role_id_source = d['sign_ip_role_id_source']
        if 'sign_merchant_id' in d:
            o.sign_merchant_id = d['sign_merchant_id']
        if 'sign_merchant_id_source' in d:
            o.sign_merchant_id_source = d['sign_merchant_id_source']
        if 'summary_dmsn_1' in d:
            o.summary_dmsn_1 = d['summary_dmsn_1']
        if 'summary_dmsn_2' in d:
            o.summary_dmsn_2 = d['summary_dmsn_2']
        if 'summary_dmsn_3' in d:
            o.summary_dmsn_3 = d['summary_dmsn_3']
        if 'summary_dmsn_4' in d:
            o.summary_dmsn_4 = d['summary_dmsn_4']
        if 'summary_dmsn_5' in d:
            o.summary_dmsn_5 = d['summary_dmsn_5']
        if 'summary_dmsn_6' in d:
            o.summary_dmsn_6 = d['summary_dmsn_6']
        if 'summary_dmsn_7' in d:
            o.summary_dmsn_7 = d['summary_dmsn_7']
        if 'summary_dmsn_value' in d:
            o.summary_dmsn_value = d['summary_dmsn_value']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'un_confirmed_amount' in d:
            o.un_confirmed_amount = d['un_confirmed_amount']
        if 'un_invoice_amt' in d:
            o.un_invoice_amt = d['un_invoice_amt']
        if 'un_settled_amount' in d:
            o.un_settled_amount = d['un_settled_amount']
        if 'version_flag' in d:
            o.version_flag = d['version_flag']
        return o



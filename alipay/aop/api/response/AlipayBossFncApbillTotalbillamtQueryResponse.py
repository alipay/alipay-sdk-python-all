#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
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
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncApbillTotalbillamtQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncApbillTotalbillamtQueryResponse, self).__init__()
        self._agr_adj_amt = None
        self._agr_adj_chk_amt = None
        self._analysis_dmsn_1 = None
        self._analysis_dmsn_2 = None
        self._analysis_dmsn_3 = None
        self._analysis_dmsn_4 = None
        self._ar_no = None
        self._auth_invoice_amt = None
        self._bill_amt = None
        self._bill_check_status = None
        self._bill_chk_amt = None
        self._bill_end_date = None
        self._bill_invoice_link_status = None
        self._bill_month = None
        self._bill_no = None
        self._bill_start_date = None
        self._biz_type = None
        self._dtl_adj_amt = None
        self._dtl_adj_chk_amt = None
        self._end_date = None
        self._exchange_rate = None
        self._exn_inf = None
        self._fbd_pay_amt = None
        self._fbd_pay_chk_amt = None
        self._inst_id = None
        self._intransit_amt = None
        self._invoice_amt = None
        self._ip_role_id = None
        self._mid = None
        self._new_can_invoice_amt = None
        self._paid_amt = None
        self._pay_channel = None
        self._pay_status = None
        self._pd_code = None
        self._pd_name = None
        self._pre_wrtof_amt = None
        self._price_id = None
        self._price_policy_id = None
        self._price_policy_name = None
        self._real_bill_amt = None
        self._real_bill_chk_amt = None
        self._settle_type = None
        self._start_date = None
        self._tax_amt = None
        self._tax_included_amt = None
        self._withhold_tax_amt = None
        self._withhold_tax_chk_amt = None

    @property
    def agr_adj_amt(self):
        return self._agr_adj_amt

    @agr_adj_amt.setter
    def agr_adj_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._agr_adj_amt = value
        else:
            self._agr_adj_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def agr_adj_chk_amt(self):
        return self._agr_adj_chk_amt

    @agr_adj_chk_amt.setter
    def agr_adj_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._agr_adj_chk_amt = value
        else:
            self._agr_adj_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def auth_invoice_amt(self):
        return self._auth_invoice_amt

    @auth_invoice_amt.setter
    def auth_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._auth_invoice_amt = value
        else:
            self._auth_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def bill_check_status(self):
        return self._bill_check_status

    @bill_check_status.setter
    def bill_check_status(self, value):
        self._bill_check_status = value
    @property
    def bill_chk_amt(self):
        return self._bill_chk_amt

    @bill_chk_amt.setter
    def bill_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_chk_amt = value
        else:
            self._bill_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_end_date(self):
        return self._bill_end_date

    @bill_end_date.setter
    def bill_end_date(self, value):
        self._bill_end_date = value
    @property
    def bill_invoice_link_status(self):
        return self._bill_invoice_link_status

    @bill_invoice_link_status.setter
    def bill_invoice_link_status(self, value):
        self._bill_invoice_link_status = value
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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def dtl_adj_amt(self):
        return self._dtl_adj_amt

    @dtl_adj_amt.setter
    def dtl_adj_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._dtl_adj_amt = value
        else:
            self._dtl_adj_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def dtl_adj_chk_amt(self):
        return self._dtl_adj_chk_amt

    @dtl_adj_chk_amt.setter
    def dtl_adj_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._dtl_adj_chk_amt = value
        else:
            self._dtl_adj_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def exn_inf(self):
        return self._exn_inf

    @exn_inf.setter
    def exn_inf(self, value):
        self._exn_inf = value
    @property
    def fbd_pay_amt(self):
        return self._fbd_pay_amt

    @fbd_pay_amt.setter
    def fbd_pay_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._fbd_pay_amt = value
        else:
            self._fbd_pay_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def fbd_pay_chk_amt(self):
        return self._fbd_pay_chk_amt

    @fbd_pay_chk_amt.setter
    def fbd_pay_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._fbd_pay_chk_amt = value
        else:
            self._fbd_pay_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def intransit_amt(self):
        return self._intransit_amt

    @intransit_amt.setter
    def intransit_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._intransit_amt = value
        else:
            self._intransit_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def new_can_invoice_amt(self):
        return self._new_can_invoice_amt

    @new_can_invoice_amt.setter
    def new_can_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._new_can_invoice_amt = value
        else:
            self._new_can_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def pd_name(self):
        return self._pd_name

    @pd_name.setter
    def pd_name(self, value):
        self._pd_name = value
    @property
    def pre_wrtof_amt(self):
        return self._pre_wrtof_amt

    @pre_wrtof_amt.setter
    def pre_wrtof_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._pre_wrtof_amt = value
        else:
            self._pre_wrtof_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def price_policy_id(self):
        return self._price_policy_id

    @price_policy_id.setter
    def price_policy_id(self, value):
        self._price_policy_id = value
    @property
    def price_policy_name(self):
        return self._price_policy_name

    @price_policy_name.setter
    def price_policy_name(self, value):
        self._price_policy_name = value
    @property
    def real_bill_amt(self):
        return self._real_bill_amt

    @real_bill_amt.setter
    def real_bill_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._real_bill_amt = value
        else:
            self._real_bill_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def real_bill_chk_amt(self):
        return self._real_bill_chk_amt

    @real_bill_chk_amt.setter
    def real_bill_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._real_bill_chk_amt = value
        else:
            self._real_bill_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
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
    def tax_included_amt(self):
        return self._tax_included_amt

    @tax_included_amt.setter
    def tax_included_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_included_amt = value
        else:
            self._tax_included_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def withhold_tax_amt(self):
        return self._withhold_tax_amt

    @withhold_tax_amt.setter
    def withhold_tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._withhold_tax_amt = value
        else:
            self._withhold_tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def withhold_tax_chk_amt(self):
        return self._withhold_tax_chk_amt

    @withhold_tax_chk_amt.setter
    def withhold_tax_chk_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._withhold_tax_chk_amt = value
        else:
            self._withhold_tax_chk_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncApbillTotalbillamtQueryResponse, self).parse_response_content(response_content)
        if 'agr_adj_amt' in response:
            self.agr_adj_amt = response['agr_adj_amt']
        if 'agr_adj_chk_amt' in response:
            self.agr_adj_chk_amt = response['agr_adj_chk_amt']
        if 'analysis_dmsn_1' in response:
            self.analysis_dmsn_1 = response['analysis_dmsn_1']
        if 'analysis_dmsn_2' in response:
            self.analysis_dmsn_2 = response['analysis_dmsn_2']
        if 'analysis_dmsn_3' in response:
            self.analysis_dmsn_3 = response['analysis_dmsn_3']
        if 'analysis_dmsn_4' in response:
            self.analysis_dmsn_4 = response['analysis_dmsn_4']
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'auth_invoice_amt' in response:
            self.auth_invoice_amt = response['auth_invoice_amt']
        if 'bill_amt' in response:
            self.bill_amt = response['bill_amt']
        if 'bill_check_status' in response:
            self.bill_check_status = response['bill_check_status']
        if 'bill_chk_amt' in response:
            self.bill_chk_amt = response['bill_chk_amt']
        if 'bill_end_date' in response:
            self.bill_end_date = response['bill_end_date']
        if 'bill_invoice_link_status' in response:
            self.bill_invoice_link_status = response['bill_invoice_link_status']
        if 'bill_month' in response:
            self.bill_month = response['bill_month']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'bill_start_date' in response:
            self.bill_start_date = response['bill_start_date']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'dtl_adj_amt' in response:
            self.dtl_adj_amt = response['dtl_adj_amt']
        if 'dtl_adj_chk_amt' in response:
            self.dtl_adj_chk_amt = response['dtl_adj_chk_amt']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'exchange_rate' in response:
            self.exchange_rate = response['exchange_rate']
        if 'exn_inf' in response:
            self.exn_inf = response['exn_inf']
        if 'fbd_pay_amt' in response:
            self.fbd_pay_amt = response['fbd_pay_amt']
        if 'fbd_pay_chk_amt' in response:
            self.fbd_pay_chk_amt = response['fbd_pay_chk_amt']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'intransit_amt' in response:
            self.intransit_amt = response['intransit_amt']
        if 'invoice_amt' in response:
            self.invoice_amt = response['invoice_amt']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'mid' in response:
            self.mid = response['mid']
        if 'new_can_invoice_amt' in response:
            self.new_can_invoice_amt = response['new_can_invoice_amt']
        if 'paid_amt' in response:
            self.paid_amt = response['paid_amt']
        if 'pay_channel' in response:
            self.pay_channel = response['pay_channel']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pd_code' in response:
            self.pd_code = response['pd_code']
        if 'pd_name' in response:
            self.pd_name = response['pd_name']
        if 'pre_wrtof_amt' in response:
            self.pre_wrtof_amt = response['pre_wrtof_amt']
        if 'price_id' in response:
            self.price_id = response['price_id']
        if 'price_policy_id' in response:
            self.price_policy_id = response['price_policy_id']
        if 'price_policy_name' in response:
            self.price_policy_name = response['price_policy_name']
        if 'real_bill_amt' in response:
            self.real_bill_amt = response['real_bill_amt']
        if 'real_bill_chk_amt' in response:
            self.real_bill_chk_amt = response['real_bill_chk_amt']
        if 'settle_type' in response:
            self.settle_type = response['settle_type']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'tax_amt' in response:
            self.tax_amt = response['tax_amt']
        if 'tax_included_amt' in response:
            self.tax_included_amt = response['tax_included_amt']
        if 'withhold_tax_amt' in response:
            self.withhold_tax_amt = response['withhold_tax_amt']
        if 'withhold_tax_chk_amt' in response:
            self.withhold_tax_chk_amt = response['withhold_tax_chk_amt']

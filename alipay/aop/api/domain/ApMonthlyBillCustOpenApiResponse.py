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


class ApMonthlyBillCustOpenApiResponse(object):

    def __init__(self):
        self._analysis_dmsn_1 = None
        self._analysis_dmsn_2 = None
        self._analysis_dmsn_3 = None
        self._analysis_dmsn_4 = None
        self._ar_no = None
        self._auth_invoice_amt = None
        self._bill_invoice_link_status = None
        self._bill_month = None
        self._bill_no = None
        self._biz_type = None
        self._end_date = None
        self._fbd_pay_amt = None
        self._fbd_pay_type = None
        self._inst_id = None
        self._invoice_amt = None
        self._ip_role_id = None
        self._ip_role_name = None
        self._mid = None
        self._new_can_invoice_amt = None
        self._paid_amt = None
        self._pay_channel = None
        self._pay_status = None
        self._pd_code = None
        self._pd_name = None
        self._price_id = None
        self._price_name = None
        self._price_policy_id = None
        self._price_policy_name = None
        self._real_bill_amt = None
        self._settle_type = None
        self._start_date = None
        self._tax_amt = None

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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
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
    def fbd_pay_type(self):
        return self._fbd_pay_type

    @fbd_pay_type.setter
    def fbd_pay_type(self, value):
        self._fbd_pay_type = value
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
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_name(self):
        return self._ip_role_name

    @ip_role_name.setter
    def ip_role_name(self, value):
        self._ip_role_name = value
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
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def price_name(self):
        return self._price_name

    @price_name.setter
    def price_name(self, value):
        self._price_name = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.auth_invoice_amt:
            if hasattr(self.auth_invoice_amt, 'to_alipay_dict'):
                params['auth_invoice_amt'] = self.auth_invoice_amt.to_alipay_dict()
            else:
                params['auth_invoice_amt'] = self.auth_invoice_amt
        if self.bill_invoice_link_status:
            if hasattr(self.bill_invoice_link_status, 'to_alipay_dict'):
                params['bill_invoice_link_status'] = self.bill_invoice_link_status.to_alipay_dict()
            else:
                params['bill_invoice_link_status'] = self.bill_invoice_link_status
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
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.fbd_pay_amt:
            if hasattr(self.fbd_pay_amt, 'to_alipay_dict'):
                params['fbd_pay_amt'] = self.fbd_pay_amt.to_alipay_dict()
            else:
                params['fbd_pay_amt'] = self.fbd_pay_amt
        if self.fbd_pay_type:
            if hasattr(self.fbd_pay_type, 'to_alipay_dict'):
                params['fbd_pay_type'] = self.fbd_pay_type.to_alipay_dict()
            else:
                params['fbd_pay_type'] = self.fbd_pay_type
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
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_name:
            if hasattr(self.ip_role_name, 'to_alipay_dict'):
                params['ip_role_name'] = self.ip_role_name.to_alipay_dict()
            else:
                params['ip_role_name'] = self.ip_role_name
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.new_can_invoice_amt:
            if hasattr(self.new_can_invoice_amt, 'to_alipay_dict'):
                params['new_can_invoice_amt'] = self.new_can_invoice_amt.to_alipay_dict()
            else:
                params['new_can_invoice_amt'] = self.new_can_invoice_amt
        if self.paid_amt:
            if hasattr(self.paid_amt, 'to_alipay_dict'):
                params['paid_amt'] = self.paid_amt.to_alipay_dict()
            else:
                params['paid_amt'] = self.paid_amt
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.pd_name:
            if hasattr(self.pd_name, 'to_alipay_dict'):
                params['pd_name'] = self.pd_name.to_alipay_dict()
            else:
                params['pd_name'] = self.pd_name
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.price_name:
            if hasattr(self.price_name, 'to_alipay_dict'):
                params['price_name'] = self.price_name.to_alipay_dict()
            else:
                params['price_name'] = self.price_name
        if self.price_policy_id:
            if hasattr(self.price_policy_id, 'to_alipay_dict'):
                params['price_policy_id'] = self.price_policy_id.to_alipay_dict()
            else:
                params['price_policy_id'] = self.price_policy_id
        if self.price_policy_name:
            if hasattr(self.price_policy_name, 'to_alipay_dict'):
                params['price_policy_name'] = self.price_policy_name.to_alipay_dict()
            else:
                params['price_policy_name'] = self.price_policy_name
        if self.real_bill_amt:
            if hasattr(self.real_bill_amt, 'to_alipay_dict'):
                params['real_bill_amt'] = self.real_bill_amt.to_alipay_dict()
            else:
                params['real_bill_amt'] = self.real_bill_amt
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApMonthlyBillCustOpenApiResponse()
        if 'analysis_dmsn_1' in d:
            o.analysis_dmsn_1 = d['analysis_dmsn_1']
        if 'analysis_dmsn_2' in d:
            o.analysis_dmsn_2 = d['analysis_dmsn_2']
        if 'analysis_dmsn_3' in d:
            o.analysis_dmsn_3 = d['analysis_dmsn_3']
        if 'analysis_dmsn_4' in d:
            o.analysis_dmsn_4 = d['analysis_dmsn_4']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'auth_invoice_amt' in d:
            o.auth_invoice_amt = d['auth_invoice_amt']
        if 'bill_invoice_link_status' in d:
            o.bill_invoice_link_status = d['bill_invoice_link_status']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'fbd_pay_amt' in d:
            o.fbd_pay_amt = d['fbd_pay_amt']
        if 'fbd_pay_type' in d:
            o.fbd_pay_type = d['fbd_pay_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_name' in d:
            o.ip_role_name = d['ip_role_name']
        if 'mid' in d:
            o.mid = d['mid']
        if 'new_can_invoice_amt' in d:
            o.new_can_invoice_amt = d['new_can_invoice_amt']
        if 'paid_amt' in d:
            o.paid_amt = d['paid_amt']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'pd_name' in d:
            o.pd_name = d['pd_name']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'price_name' in d:
            o.price_name = d['price_name']
        if 'price_policy_id' in d:
            o.price_policy_id = d['price_policy_id']
        if 'price_policy_name' in d:
            o.price_policy_name = d['price_policy_name']
        if 'real_bill_amt' in d:
            o.real_bill_amt = d['real_bill_amt']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        return o



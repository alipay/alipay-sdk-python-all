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


class SummaryBillOpenApiDTO(object):

    def __init__(self):
        self._adjust_amount = None
        self._bill_amount = None
        self._bill_month = None
        self._bill_no = None
        self._bill_status = None
        self._biz_pd_code = None
        self._fund_settle_time = None
        self._inst_id = None
        self._invoiced_amt = None
        self._invoicing_amt = None
        self._payee_ip_role_id = None
        self._real_bill_amount = None
        self._settle_ip_role_id = None
        self._settle_status = None
        self._settle_time_type = None
        self._settled_amount = None
        self._source = None
        self._summary_dmsn_1 = None
        self._summary_dmsn_2 = None
        self._summary_dmsn_3 = None
        self._summary_dmsn_4 = None
        self._summary_dmsn_5 = None
        self._summary_dmsn_6 = None
        self._summary_dmsn_7 = None
        self._tax_rate = None
        self._un_invoice_amt = None

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
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amount = value
        else:
            self._bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def fund_settle_time(self):
        return self._fund_settle_time

    @fund_settle_time.setter
    def fund_settle_time(self, value):
        self._fund_settle_time = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
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
    def invoicing_amt(self):
        return self._invoicing_amt

    @invoicing_amt.setter
    def invoicing_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoicing_amt = value
        else:
            self._invoicing_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def payee_ip_role_id(self):
        return self._payee_ip_role_id

    @payee_ip_role_id.setter
    def payee_ip_role_id(self, value):
        self._payee_ip_role_id = value
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
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_time_type(self):
        return self._settle_time_type

    @settle_time_type.setter
    def settle_time_type(self, value):
        self._settle_time_type = value
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
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
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def un_invoice_amt(self):
        return self._un_invoice_amt

    @un_invoice_amt.setter
    def un_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_invoice_amt = value
        else:
            self._un_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_amount:
            if hasattr(self.adjust_amount, 'to_alipay_dict'):
                params['adjust_amount'] = self.adjust_amount.to_alipay_dict()
            else:
                params['adjust_amount'] = self.adjust_amount
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
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
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.fund_settle_time:
            if hasattr(self.fund_settle_time, 'to_alipay_dict'):
                params['fund_settle_time'] = self.fund_settle_time.to_alipay_dict()
            else:
                params['fund_settle_time'] = self.fund_settle_time
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoiced_amt:
            if hasattr(self.invoiced_amt, 'to_alipay_dict'):
                params['invoiced_amt'] = self.invoiced_amt.to_alipay_dict()
            else:
                params['invoiced_amt'] = self.invoiced_amt
        if self.invoicing_amt:
            if hasattr(self.invoicing_amt, 'to_alipay_dict'):
                params['invoicing_amt'] = self.invoicing_amt.to_alipay_dict()
            else:
                params['invoicing_amt'] = self.invoicing_amt
        if self.payee_ip_role_id:
            if hasattr(self.payee_ip_role_id, 'to_alipay_dict'):
                params['payee_ip_role_id'] = self.payee_ip_role_id.to_alipay_dict()
            else:
                params['payee_ip_role_id'] = self.payee_ip_role_id
        if self.real_bill_amount:
            if hasattr(self.real_bill_amount, 'to_alipay_dict'):
                params['real_bill_amount'] = self.real_bill_amount.to_alipay_dict()
            else:
                params['real_bill_amount'] = self.real_bill_amount
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_time_type:
            if hasattr(self.settle_time_type, 'to_alipay_dict'):
                params['settle_time_type'] = self.settle_time_type.to_alipay_dict()
            else:
                params['settle_time_type'] = self.settle_time_type
        if self.settled_amount:
            if hasattr(self.settled_amount, 'to_alipay_dict'):
                params['settled_amount'] = self.settled_amount.to_alipay_dict()
            else:
                params['settled_amount'] = self.settled_amount
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.un_invoice_amt:
            if hasattr(self.un_invoice_amt, 'to_alipay_dict'):
                params['un_invoice_amt'] = self.un_invoice_amt.to_alipay_dict()
            else:
                params['un_invoice_amt'] = self.un_invoice_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryBillOpenApiDTO()
        if 'adjust_amount' in d:
            o.adjust_amount = d['adjust_amount']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'fund_settle_time' in d:
            o.fund_settle_time = d['fund_settle_time']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoiced_amt' in d:
            o.invoiced_amt = d['invoiced_amt']
        if 'invoicing_amt' in d:
            o.invoicing_amt = d['invoicing_amt']
        if 'payee_ip_role_id' in d:
            o.payee_ip_role_id = d['payee_ip_role_id']
        if 'real_bill_amount' in d:
            o.real_bill_amount = d['real_bill_amount']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time_type' in d:
            o.settle_time_type = d['settle_time_type']
        if 'settled_amount' in d:
            o.settled_amount = d['settled_amount']
        if 'source' in d:
            o.source = d['source']
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
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'un_invoice_amt' in d:
            o.un_invoice_amt = d['un_invoice_amt']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MapParameter import MapParameter
from alipay.aop.api.domain.MapParameter import MapParameter
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class SettlementBillCreateOrder(object):

    def __init__(self):
        self._ar_no = None
        self._ar_source = None
        self._business_period = None
        self._business_period_offset = None
        self._business_recognize_ext = None
        self._exn_info = None
        self._inst_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._payee_account = None
        self._payee_account_type = None
        self._payer_account = None
        self._payer_account_type = None
        self._pd_code = None
        self._pd_source = None
        self._service_begin_date = None
        self._service_end_date = None
        self._settle_amount = None
        self._settle_basis = None
        self._settle_rate = None
        self._settlement_basic_type = None
        self._settlement_type = None
        self._sign_ip_role_id = None
        self._source = None
        self._time_zone = None
        self._user_source = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def ar_source(self):
        return self._ar_source

    @ar_source.setter
    def ar_source(self, value):
        self._ar_source = value
    @property
    def business_period(self):
        return self._business_period

    @business_period.setter
    def business_period(self, value):
        self._business_period = value
    @property
    def business_period_offset(self):
        return self._business_period_offset

    @business_period_offset.setter
    def business_period_offset(self, value):
        self._business_period_offset = value
    @property
    def business_recognize_ext(self):
        return self._business_recognize_ext

    @business_recognize_ext.setter
    def business_recognize_ext(self, value):
        if isinstance(value, MapParameter):
            self._business_recognize_ext = value
        else:
            self._business_recognize_ext = MapParameter.from_alipay_dict(value)
    @property
    def exn_info(self):
        return self._exn_info

    @exn_info.setter
    def exn_info(self, value):
        if isinstance(value, MapParameter):
            self._exn_info = value
        else:
            self._exn_info = MapParameter.from_alipay_dict(value)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        self._payer_account = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def pd_source(self):
        return self._pd_source

    @pd_source.setter
    def pd_source(self, value):
        self._pd_source = value
    @property
    def service_begin_date(self):
        return self._service_begin_date

    @service_begin_date.setter
    def service_begin_date(self, value):
        self._service_begin_date = value
    @property
    def service_end_date(self):
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, value):
        self._service_end_date = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settle_amount = value
        else:
            self._settle_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_basis(self):
        return self._settle_basis

    @settle_basis.setter
    def settle_basis(self, value):
        self._settle_basis = value
    @property
    def settle_rate(self):
        return self._settle_rate

    @settle_rate.setter
    def settle_rate(self, value):
        self._settle_rate = value
    @property
    def settlement_basic_type(self):
        return self._settlement_basic_type

    @settlement_basic_type.setter
    def settlement_basic_type(self, value):
        self._settlement_basic_type = value
    @property
    def settlement_type(self):
        return self._settlement_type

    @settlement_type.setter
    def settlement_type(self, value):
        self._settlement_type = value
    @property
    def sign_ip_role_id(self):
        return self._sign_ip_role_id

    @sign_ip_role_id.setter
    def sign_ip_role_id(self, value):
        self._sign_ip_role_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def user_source(self):
        return self._user_source

    @user_source.setter
    def user_source(self, value):
        self._user_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.ar_source:
            if hasattr(self.ar_source, 'to_alipay_dict'):
                params['ar_source'] = self.ar_source.to_alipay_dict()
            else:
                params['ar_source'] = self.ar_source
        if self.business_period:
            if hasattr(self.business_period, 'to_alipay_dict'):
                params['business_period'] = self.business_period.to_alipay_dict()
            else:
                params['business_period'] = self.business_period
        if self.business_period_offset:
            if hasattr(self.business_period_offset, 'to_alipay_dict'):
                params['business_period_offset'] = self.business_period_offset.to_alipay_dict()
            else:
                params['business_period_offset'] = self.business_period_offset
        if self.business_recognize_ext:
            if hasattr(self.business_recognize_ext, 'to_alipay_dict'):
                params['business_recognize_ext'] = self.business_recognize_ext.to_alipay_dict()
            else:
                params['business_recognize_ext'] = self.business_recognize_ext
        if self.exn_info:
            if hasattr(self.exn_info, 'to_alipay_dict'):
                params['exn_info'] = self.exn_info.to_alipay_dict()
            else:
                params['exn_info'] = self.exn_info
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.pd_source:
            if hasattr(self.pd_source, 'to_alipay_dict'):
                params['pd_source'] = self.pd_source.to_alipay_dict()
            else:
                params['pd_source'] = self.pd_source
        if self.service_begin_date:
            if hasattr(self.service_begin_date, 'to_alipay_dict'):
                params['service_begin_date'] = self.service_begin_date.to_alipay_dict()
            else:
                params['service_begin_date'] = self.service_begin_date
        if self.service_end_date:
            if hasattr(self.service_end_date, 'to_alipay_dict'):
                params['service_end_date'] = self.service_end_date.to_alipay_dict()
            else:
                params['service_end_date'] = self.service_end_date
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_basis:
            if hasattr(self.settle_basis, 'to_alipay_dict'):
                params['settle_basis'] = self.settle_basis.to_alipay_dict()
            else:
                params['settle_basis'] = self.settle_basis
        if self.settle_rate:
            if hasattr(self.settle_rate, 'to_alipay_dict'):
                params['settle_rate'] = self.settle_rate.to_alipay_dict()
            else:
                params['settle_rate'] = self.settle_rate
        if self.settlement_basic_type:
            if hasattr(self.settlement_basic_type, 'to_alipay_dict'):
                params['settlement_basic_type'] = self.settlement_basic_type.to_alipay_dict()
            else:
                params['settlement_basic_type'] = self.settlement_basic_type
        if self.settlement_type:
            if hasattr(self.settlement_type, 'to_alipay_dict'):
                params['settlement_type'] = self.settlement_type.to_alipay_dict()
            else:
                params['settlement_type'] = self.settlement_type
        if self.sign_ip_role_id:
            if hasattr(self.sign_ip_role_id, 'to_alipay_dict'):
                params['sign_ip_role_id'] = self.sign_ip_role_id.to_alipay_dict()
            else:
                params['sign_ip_role_id'] = self.sign_ip_role_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        if self.user_source:
            if hasattr(self.user_source, 'to_alipay_dict'):
                params['user_source'] = self.user_source.to_alipay_dict()
            else:
                params['user_source'] = self.user_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettlementBillCreateOrder()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'ar_source' in d:
            o.ar_source = d['ar_source']
        if 'business_period' in d:
            o.business_period = d['business_period']
        if 'business_period_offset' in d:
            o.business_period_offset = d['business_period_offset']
        if 'business_recognize_ext' in d:
            o.business_recognize_ext = d['business_recognize_ext']
        if 'exn_info' in d:
            o.exn_info = d['exn_info']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'pd_source' in d:
            o.pd_source = d['pd_source']
        if 'service_begin_date' in d:
            o.service_begin_date = d['service_begin_date']
        if 'service_end_date' in d:
            o.service_end_date = d['service_end_date']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_basis' in d:
            o.settle_basis = d['settle_basis']
        if 'settle_rate' in d:
            o.settle_rate = d['settle_rate']
        if 'settlement_basic_type' in d:
            o.settlement_basic_type = d['settlement_basic_type']
        if 'settlement_type' in d:
            o.settlement_type = d['settlement_type']
        if 'sign_ip_role_id' in d:
            o.sign_ip_role_id = d['sign_ip_role_id']
        if 'source' in d:
            o.source = d['source']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'user_source' in d:
            o.user_source = d['user_source']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsurancePayExtendParams import InsurancePayExtendParams
from alipay.aop.api.domain.SubsidyAmountParam import SubsidyAmountParam


class AlipayCommerceMedicalTradeCreateandpayModel(object):

    def __init__(self):
        self._account_amount = None
        self._alipay_user_id = None
        self._callback_url = None
        self._ch_info = None
        self._chrg_bch_no = None
        self._extend_params = None
        self._gmt_out_create = None
        self._gmt_time_expire = None
        self._gov_amount = None
        self._industry = None
        self._insurance_pay_scene = None
        self._med_org_ord = None
        self._open_id = None
        self._order_type = None
        self._org_no = None
        self._other_amount = None
        self._out_trade_no = None
        self._pay_auth_no = None
        self._pay_order_id = None
        self._real_amount = None
        self._request_content = None
        self._result_notify_url = None
        self._shop_id = None
        self._store_id = None
        self._subject = None
        self._subsidy_amount_params = None
        self._total_amount = None

    @property
    def account_amount(self):
        return self._account_amount

    @account_amount.setter
    def account_amount(self, value):
        self._account_amount = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def chrg_bch_no(self):
        return self._chrg_bch_no

    @chrg_bch_no.setter
    def chrg_bch_no(self, value):
        self._chrg_bch_no = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, InsurancePayExtendParams):
            self._extend_params = value
        else:
            self._extend_params = InsurancePayExtendParams.from_alipay_dict(value)
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gmt_time_expire(self):
        return self._gmt_time_expire

    @gmt_time_expire.setter
    def gmt_time_expire(self, value):
        self._gmt_time_expire = value
    @property
    def gov_amount(self):
        return self._gov_amount

    @gov_amount.setter
    def gov_amount(self, value):
        self._gov_amount = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def insurance_pay_scene(self):
        return self._insurance_pay_scene

    @insurance_pay_scene.setter
    def insurance_pay_scene(self, value):
        self._insurance_pay_scene = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_auth_no(self):
        return self._pay_auth_no

    @pay_auth_no.setter
    def pay_auth_no(self, value):
        self._pay_auth_no = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def request_content(self):
        return self._request_content

    @request_content.setter
    def request_content(self, value):
        self._request_content = value
    @property
    def result_notify_url(self):
        return self._result_notify_url

    @result_notify_url.setter
    def result_notify_url(self, value):
        self._result_notify_url = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def subsidy_amount_params(self):
        return self._subsidy_amount_params

    @subsidy_amount_params.setter
    def subsidy_amount_params(self, value):
        if isinstance(value, list):
            self._subsidy_amount_params = list()
            for i in value:
                if isinstance(i, SubsidyAmountParam):
                    self._subsidy_amount_params.append(i)
                else:
                    self._subsidy_amount_params.append(SubsidyAmountParam.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_amount:
            if hasattr(self.account_amount, 'to_alipay_dict'):
                params['account_amount'] = self.account_amount.to_alipay_dict()
            else:
                params['account_amount'] = self.account_amount
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.chrg_bch_no:
            if hasattr(self.chrg_bch_no, 'to_alipay_dict'):
                params['chrg_bch_no'] = self.chrg_bch_no.to_alipay_dict()
            else:
                params['chrg_bch_no'] = self.chrg_bch_no
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.gmt_out_create:
            if hasattr(self.gmt_out_create, 'to_alipay_dict'):
                params['gmt_out_create'] = self.gmt_out_create.to_alipay_dict()
            else:
                params['gmt_out_create'] = self.gmt_out_create
        if self.gmt_time_expire:
            if hasattr(self.gmt_time_expire, 'to_alipay_dict'):
                params['gmt_time_expire'] = self.gmt_time_expire.to_alipay_dict()
            else:
                params['gmt_time_expire'] = self.gmt_time_expire
        if self.gov_amount:
            if hasattr(self.gov_amount, 'to_alipay_dict'):
                params['gov_amount'] = self.gov_amount.to_alipay_dict()
            else:
                params['gov_amount'] = self.gov_amount
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.insurance_pay_scene:
            if hasattr(self.insurance_pay_scene, 'to_alipay_dict'):
                params['insurance_pay_scene'] = self.insurance_pay_scene.to_alipay_dict()
            else:
                params['insurance_pay_scene'] = self.insurance_pay_scene
        if self.med_org_ord:
            if hasattr(self.med_org_ord, 'to_alipay_dict'):
                params['med_org_ord'] = self.med_org_ord.to_alipay_dict()
            else:
                params['med_org_ord'] = self.med_org_ord
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_auth_no:
            if hasattr(self.pay_auth_no, 'to_alipay_dict'):
                params['pay_auth_no'] = self.pay_auth_no.to_alipay_dict()
            else:
                params['pay_auth_no'] = self.pay_auth_no
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.request_content:
            if hasattr(self.request_content, 'to_alipay_dict'):
                params['request_content'] = self.request_content.to_alipay_dict()
            else:
                params['request_content'] = self.request_content
        if self.result_notify_url:
            if hasattr(self.result_notify_url, 'to_alipay_dict'):
                params['result_notify_url'] = self.result_notify_url.to_alipay_dict()
            else:
                params['result_notify_url'] = self.result_notify_url
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.subsidy_amount_params:
            if isinstance(self.subsidy_amount_params, list):
                for i in range(0, len(self.subsidy_amount_params)):
                    element = self.subsidy_amount_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subsidy_amount_params[i] = element.to_alipay_dict()
            if hasattr(self.subsidy_amount_params, 'to_alipay_dict'):
                params['subsidy_amount_params'] = self.subsidy_amount_params.to_alipay_dict()
            else:
                params['subsidy_amount_params'] = self.subsidy_amount_params
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalTradeCreateandpayModel()
        if 'account_amount' in d:
            o.account_amount = d['account_amount']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'chrg_bch_no' in d:
            o.chrg_bch_no = d['chrg_bch_no']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'gmt_out_create' in d:
            o.gmt_out_create = d['gmt_out_create']
        if 'gmt_time_expire' in d:
            o.gmt_time_expire = d['gmt_time_expire']
        if 'gov_amount' in d:
            o.gov_amount = d['gov_amount']
        if 'industry' in d:
            o.industry = d['industry']
        if 'insurance_pay_scene' in d:
            o.insurance_pay_scene = d['insurance_pay_scene']
        if 'med_org_ord' in d:
            o.med_org_ord = d['med_org_ord']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_auth_no' in d:
            o.pay_auth_no = d['pay_auth_no']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'request_content' in d:
            o.request_content = d['request_content']
        if 'result_notify_url' in d:
            o.result_notify_url = d['result_notify_url']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'subsidy_amount_params' in d:
            o.subsidy_amount_params = d['subsidy_amount_params']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



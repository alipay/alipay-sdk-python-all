#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorLendadmitConsultModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._api_model_score_map = None
        self._api_user_tag_map = None
        self._apply_no = None
        self._bank_card_id = None
        self._channel_customer_id = None
        self._coupon_no = None
        self._loan_amount = None
        self._loan_use = None
        self._open_id = None
        self._out_trace_id = None
        self._product_code = None
        self._repay_method = None
        self._request_source = None
        self._risk_info = None
        self._sign_flag = None
        self._total_term = None
        self._trial_serial_no = None
        self._verify_callback_url = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def api_model_score_map(self):
        return self._api_model_score_map

    @api_model_score_map.setter
    def api_model_score_map(self, value):
        self._api_model_score_map = value
    @property
    def api_user_tag_map(self):
        return self._api_user_tag_map

    @api_user_tag_map.setter
    def api_user_tag_map(self, value):
        self._api_user_tag_map = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def bank_card_id(self):
        return self._bank_card_id

    @bank_card_id.setter
    def bank_card_id(self, value):
        self._bank_card_id = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_use(self):
        return self._loan_use

    @loan_use.setter
    def loan_use(self, value):
        self._loan_use = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trace_id(self):
        return self._out_trace_id

    @out_trace_id.setter
    def out_trace_id(self, value):
        self._out_trace_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value
    @property
    def sign_flag(self):
        return self._sign_flag

    @sign_flag.setter
    def sign_flag(self, value):
        self._sign_flag = value
    @property
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value
    @property
    def trial_serial_no(self):
        return self._trial_serial_no

    @trial_serial_no.setter
    def trial_serial_no(self, value):
        self._trial_serial_no = value
    @property
    def verify_callback_url(self):
        return self._verify_callback_url

    @verify_callback_url.setter
    def verify_callback_url(self, value):
        self._verify_callback_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.api_model_score_map:
            if hasattr(self.api_model_score_map, 'to_alipay_dict'):
                params['api_model_score_map'] = self.api_model_score_map.to_alipay_dict()
            else:
                params['api_model_score_map'] = self.api_model_score_map
        if self.api_user_tag_map:
            if hasattr(self.api_user_tag_map, 'to_alipay_dict'):
                params['api_user_tag_map'] = self.api_user_tag_map.to_alipay_dict()
            else:
                params['api_user_tag_map'] = self.api_user_tag_map
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.bank_card_id:
            if hasattr(self.bank_card_id, 'to_alipay_dict'):
                params['bank_card_id'] = self.bank_card_id.to_alipay_dict()
            else:
                params['bank_card_id'] = self.bank_card_id
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.coupon_no:
            if hasattr(self.coupon_no, 'to_alipay_dict'):
                params['coupon_no'] = self.coupon_no.to_alipay_dict()
            else:
                params['coupon_no'] = self.coupon_no
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_use:
            if hasattr(self.loan_use, 'to_alipay_dict'):
                params['loan_use'] = self.loan_use.to_alipay_dict()
            else:
                params['loan_use'] = self.loan_use
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trace_id:
            if hasattr(self.out_trace_id, 'to_alipay_dict'):
                params['out_trace_id'] = self.out_trace_id.to_alipay_dict()
            else:
                params['out_trace_id'] = self.out_trace_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repay_method:
            if hasattr(self.repay_method, 'to_alipay_dict'):
                params['repay_method'] = self.repay_method.to_alipay_dict()
            else:
                params['repay_method'] = self.repay_method
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        if self.sign_flag:
            if hasattr(self.sign_flag, 'to_alipay_dict'):
                params['sign_flag'] = self.sign_flag.to_alipay_dict()
            else:
                params['sign_flag'] = self.sign_flag
        if self.total_term:
            if hasattr(self.total_term, 'to_alipay_dict'):
                params['total_term'] = self.total_term.to_alipay_dict()
            else:
                params['total_term'] = self.total_term
        if self.trial_serial_no:
            if hasattr(self.trial_serial_no, 'to_alipay_dict'):
                params['trial_serial_no'] = self.trial_serial_no.to_alipay_dict()
            else:
                params['trial_serial_no'] = self.trial_serial_no
        if self.verify_callback_url:
            if hasattr(self.verify_callback_url, 'to_alipay_dict'):
                params['verify_callback_url'] = self.verify_callback_url.to_alipay_dict()
            else:
                params['verify_callback_url'] = self.verify_callback_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorLendadmitConsultModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'api_model_score_map' in d:
            o.api_model_score_map = d['api_model_score_map']
        if 'api_user_tag_map' in d:
            o.api_user_tag_map = d['api_user_tag_map']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'bank_card_id' in d:
            o.bank_card_id = d['bank_card_id']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'coupon_no' in d:
            o.coupon_no = d['coupon_no']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_use' in d:
            o.loan_use = d['loan_use']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repay_method' in d:
            o.repay_method = d['repay_method']
        if 'request_source' in d:
            o.request_source = d['request_source']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'sign_flag' in d:
            o.sign_flag = d['sign_flag']
        if 'total_term' in d:
            o.total_term = d['total_term']
        if 'trial_serial_no' in d:
            o.trial_serial_no = d['trial_serial_no']
        if 'verify_callback_url' in d:
            o.verify_callback_url = d['verify_callback_url']
        return o



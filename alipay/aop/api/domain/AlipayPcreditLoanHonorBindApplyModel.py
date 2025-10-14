#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorBindApplyModel(object):

    def __init__(self):
        self._agreement_consult_serial_no = None
        self._alipay_user_id = None
        self._api_model_score_map = None
        self._api_user_tag_map = None
        self._channel_customer_id = None
        self._open_id = None
        self._out_trace_id = None
        self._product_code = None
        self._request_source = None
        self._risk_info = None
        self._verify_callback_url = None

    @property
    def agreement_consult_serial_no(self):
        return self._agreement_consult_serial_no

    @agreement_consult_serial_no.setter
    def agreement_consult_serial_no(self, value):
        self._agreement_consult_serial_no = value
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
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
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
    def verify_callback_url(self):
        return self._verify_callback_url

    @verify_callback_url.setter
    def verify_callback_url(self, value):
        self._verify_callback_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_consult_serial_no:
            if hasattr(self.agreement_consult_serial_no, 'to_alipay_dict'):
                params['agreement_consult_serial_no'] = self.agreement_consult_serial_no.to_alipay_dict()
            else:
                params['agreement_consult_serial_no'] = self.agreement_consult_serial_no
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
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
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
        o = AlipayPcreditLoanHonorBindApplyModel()
        if 'agreement_consult_serial_no' in d:
            o.agreement_consult_serial_no = d['agreement_consult_serial_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'api_model_score_map' in d:
            o.api_model_score_map = d['api_model_score_map']
        if 'api_user_tag_map' in d:
            o.api_user_tag_map = d['api_user_tag_map']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_source' in d:
            o.request_source = d['request_source']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'verify_callback_url' in d:
            o.verify_callback_url = d['verify_callback_url']
        return o



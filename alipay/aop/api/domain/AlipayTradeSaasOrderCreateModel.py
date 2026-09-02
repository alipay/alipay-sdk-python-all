#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaasBusinessParams import SaasBusinessParams
from alipay.aop.api.domain.SaasBuyerInfo import SaasBuyerInfo
from alipay.aop.api.domain.SaasExtendParams import SaasExtendParams
from alipay.aop.api.domain.SaasGoodsDetail import SaasGoodsDetail


class AlipayTradeSaasOrderCreateModel(object):

    def __init__(self):
        self._additional_options = None
        self._business_params = None
        self._buyer_info = None
        self._extend_params = None
        self._goods_detail = None
        self._memo = None
        self._out_trade_no = None
        self._passback_params = None
        self._pay_channels = None
        self._promo_params = None
        self._query_options = None
        self._redirect_url = None
        self._security_params = None
        self._subject = None
        self._time_expire = None
        self._timeout_express = None
        self._total_amount = None

    @property
    def additional_options(self):
        return self._additional_options

    @additional_options.setter
    def additional_options(self, value):
        if isinstance(value, list):
            self._additional_options = list()
            for i in value:
                self._additional_options.append(i)
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, SaasBusinessParams):
            self._business_params = value
        else:
            self._business_params = SaasBusinessParams.from_alipay_dict(value)
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, SaasBuyerInfo):
            self._buyer_info = value
        else:
            self._buyer_info = SaasBuyerInfo.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, SaasExtendParams):
            self._extend_params = value
        else:
            self._extend_params = SaasExtendParams.from_alipay_dict(value)
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, SaasGoodsDetail):
            self._goods_detail = value
        else:
            self._goods_detail = SaasGoodsDetail.from_alipay_dict(value)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def pay_channels(self):
        return self._pay_channels

    @pay_channels.setter
    def pay_channels(self, value):
        self._pay_channels = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        self._query_options = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def security_params(self):
        return self._security_params

    @security_params.setter
    def security_params(self, value):
        self._security_params = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_options:
            if isinstance(self.additional_options, list):
                for i in range(0, len(self.additional_options)):
                    element = self.additional_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.additional_options[i] = element.to_alipay_dict()
            if hasattr(self.additional_options, 'to_alipay_dict'):
                params['additional_options'] = self.additional_options.to_alipay_dict()
            else:
                params['additional_options'] = self.additional_options
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.goods_detail:
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.passback_params:
            if hasattr(self.passback_params, 'to_alipay_dict'):
                params['passback_params'] = self.passback_params.to_alipay_dict()
            else:
                params['passback_params'] = self.passback_params
        if self.pay_channels:
            if hasattr(self.pay_channels, 'to_alipay_dict'):
                params['pay_channels'] = self.pay_channels.to_alipay_dict()
            else:
                params['pay_channels'] = self.pay_channels
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.query_options:
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.security_params:
            if hasattr(self.security_params, 'to_alipay_dict'):
                params['security_params'] = self.security_params.to_alipay_dict()
            else:
                params['security_params'] = self.security_params
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
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
        o = AlipayTradeSaasOrderCreateModel()
        if 'additional_options' in d:
            o.additional_options = d['additional_options']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'passback_params' in d:
            o.passback_params = d['passback_params']
        if 'pay_channels' in d:
            o.pay_channels = d['pay_channels']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'query_options' in d:
            o.query_options = d['query_options']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'security_params' in d:
            o.security_params = d['security_params']
        if 'subject' in d:
            o.subject = d['subject']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



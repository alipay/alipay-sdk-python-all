#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerEnvInfo import VoyagerEnvInfo
from alipay.aop.api.domain.VoyagerOrderInfoDTO import VoyagerOrderInfoDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.VoyagerPaymentMethod import VoyagerPaymentMethod
from alipay.aop.api.domain.SettlementStrategyDTO import SettlementStrategyDTO


class AlipayVoyagerPaymentsPayModel(object):

    def __init__(self):
        self._env = None
        self._expire_time = None
        self._industry = None
        self._open_id = None
        self._order = None
        self._payment_amount = None
        self._payment_method = None
        self._payment_notify_url = None
        self._payment_redirect_url = None
        self._payment_request_id = None
        self._settlement_strategy = None
        self._user_id = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        if isinstance(value, VoyagerEnvInfo):
            self._env = value
        else:
            self._env = VoyagerEnvInfo.from_alipay_dict(value)
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if isinstance(value, VoyagerOrderInfoDTO):
            self._order = value
        else:
            self._order = VoyagerOrderInfoDTO.from_alipay_dict(value)
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._payment_amount = value
        else:
            self._payment_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        if isinstance(value, VoyagerPaymentMethod):
            self._payment_method = value
        else:
            self._payment_method = VoyagerPaymentMethod.from_alipay_dict(value)
    @property
    def payment_notify_url(self):
        return self._payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self._payment_notify_url = value
    @property
    def payment_redirect_url(self):
        return self._payment_redirect_url

    @payment_redirect_url.setter
    def payment_redirect_url(self, value):
        self._payment_redirect_url = value
    @property
    def payment_request_id(self):
        return self._payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self._payment_request_id = value
    @property
    def settlement_strategy(self):
        return self._settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        if isinstance(value, SettlementStrategyDTO):
            self._settlement_strategy = value
        else:
            self._settlement_strategy = SettlementStrategyDTO.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.payment_notify_url:
            if hasattr(self.payment_notify_url, 'to_alipay_dict'):
                params['payment_notify_url'] = self.payment_notify_url.to_alipay_dict()
            else:
                params['payment_notify_url'] = self.payment_notify_url
        if self.payment_redirect_url:
            if hasattr(self.payment_redirect_url, 'to_alipay_dict'):
                params['payment_redirect_url'] = self.payment_redirect_url.to_alipay_dict()
            else:
                params['payment_redirect_url'] = self.payment_redirect_url
        if self.payment_request_id:
            if hasattr(self.payment_request_id, 'to_alipay_dict'):
                params['payment_request_id'] = self.payment_request_id.to_alipay_dict()
            else:
                params['payment_request_id'] = self.payment_request_id
        if self.settlement_strategy:
            if hasattr(self.settlement_strategy, 'to_alipay_dict'):
                params['settlement_strategy'] = self.settlement_strategy.to_alipay_dict()
            else:
                params['settlement_strategy'] = self.settlement_strategy
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayVoyagerPaymentsPayModel()
        if 'env' in d:
            o.env = d['env']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'industry' in d:
            o.industry = d['industry']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order' in d:
            o.order = d['order']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'payment_notify_url' in d:
            o.payment_notify_url = d['payment_notify_url']
        if 'payment_redirect_url' in d:
            o.payment_redirect_url = d['payment_redirect_url']
        if 'payment_request_id' in d:
            o.payment_request_id = d['payment_request_id']
        if 'settlement_strategy' in d:
            o.settlement_strategy = d['settlement_strategy']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



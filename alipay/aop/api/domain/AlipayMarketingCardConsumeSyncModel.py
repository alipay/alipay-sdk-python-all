#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCard import MerchantCard
from alipay.aop.api.domain.BenefitInfoDetail import BenefitInfoDetail
from alipay.aop.api.domain.BenefitInfoDetail import BenefitInfoDetail


class AlipayMarketingCardConsumeSyncModel(object):

    def __init__(self):
        self._act_pay_amount = None
        self._card_info = None
        self._gain_benefit_list = None
        self._memo = None
        self._shop_code = None
        self._swipe_cert_type = None
        self._target_card_no = None
        self._target_card_no_type = None
        self._trade_amount = None
        self._trade_name = None
        self._trade_no = None
        self._trade_time = None
        self._trade_type = None
        self._use_benefit_list = None

    @property
    def act_pay_amount(self):
        return self._act_pay_amount

    @act_pay_amount.setter
    def act_pay_amount(self, value):
        self._act_pay_amount = value
    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_info = value
        else:
            self._card_info = MerchantCard.from_alipay_dict(value)
    @property
    def gain_benefit_list(self):
        return self._gain_benefit_list

    @gain_benefit_list.setter
    def gain_benefit_list(self, value):
        if isinstance(value, list):
            self._gain_benefit_list = list()
            for i in value:
                if isinstance(i, BenefitInfoDetail):
                    self._gain_benefit_list.append(i)
                else:
                    self._gain_benefit_list.append(BenefitInfoDetail.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def swipe_cert_type(self):
        return self._swipe_cert_type

    @swipe_cert_type.setter
    def swipe_cert_type(self, value):
        self._swipe_cert_type = value
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_name(self):
        return self._trade_name

    @trade_name.setter
    def trade_name(self, value):
        self._trade_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def use_benefit_list(self):
        return self._use_benefit_list

    @use_benefit_list.setter
    def use_benefit_list(self, value):
        if isinstance(value, list):
            self._use_benefit_list = list()
            for i in value:
                if isinstance(i, BenefitInfoDetail):
                    self._use_benefit_list.append(i)
                else:
                    self._use_benefit_list.append(BenefitInfoDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.act_pay_amount:
            if hasattr(self.act_pay_amount, 'to_alipay_dict'):
                params['act_pay_amount'] = self.act_pay_amount.to_alipay_dict()
            else:
                params['act_pay_amount'] = self.act_pay_amount
        if self.card_info:
            if hasattr(self.card_info, 'to_alipay_dict'):
                params['card_info'] = self.card_info.to_alipay_dict()
            else:
                params['card_info'] = self.card_info
        if self.gain_benefit_list:
            if isinstance(self.gain_benefit_list, list):
                for i in range(0, len(self.gain_benefit_list)):
                    element = self.gain_benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gain_benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.gain_benefit_list, 'to_alipay_dict'):
                params['gain_benefit_list'] = self.gain_benefit_list.to_alipay_dict()
            else:
                params['gain_benefit_list'] = self.gain_benefit_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.swipe_cert_type:
            if hasattr(self.swipe_cert_type, 'to_alipay_dict'):
                params['swipe_cert_type'] = self.swipe_cert_type.to_alipay_dict()
            else:
                params['swipe_cert_type'] = self.swipe_cert_type
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_name:
            if hasattr(self.trade_name, 'to_alipay_dict'):
                params['trade_name'] = self.trade_name.to_alipay_dict()
            else:
                params['trade_name'] = self.trade_name
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.use_benefit_list:
            if isinstance(self.use_benefit_list, list):
                for i in range(0, len(self.use_benefit_list)):
                    element = self.use_benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.use_benefit_list, 'to_alipay_dict'):
                params['use_benefit_list'] = self.use_benefit_list.to_alipay_dict()
            else:
                params['use_benefit_list'] = self.use_benefit_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardConsumeSyncModel()
        if 'act_pay_amount' in d:
            o.act_pay_amount = d['act_pay_amount']
        if 'card_info' in d:
            o.card_info = d['card_info']
        if 'gain_benefit_list' in d:
            o.gain_benefit_list = d['gain_benefit_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'swipe_cert_type' in d:
            o.swipe_cert_type = d['swipe_cert_type']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_name' in d:
            o.trade_name = d['trade_name']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'use_benefit_list' in d:
            o.use_benefit_list = d['use_benefit_list']
        return o



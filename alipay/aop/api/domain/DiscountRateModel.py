#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountDstCampPrizeModel import DiscountDstCampPrizeModel
from alipay.aop.api.domain.ReduceDstCampPrizeModel import ReduceDstCampPrizeModel
from alipay.aop.api.domain.ReduceToAmtDstCampPrizeModel import ReduceToAmtDstCampPrizeModel
from alipay.aop.api.domain.SingleDstCampPrizeModel import SingleDstCampPrizeModel


class DiscountRateModel(object):

    def __init__(self):
        self._discount_dst_camp_prize_model = None
        self._lower_trade_fee = None
        self._prize_type = None
        self._reduce_dst_camp_prize_model = None
        self._reduce_to_amt_dst_camp_prize_model = None
        self._single_dst_camp_prize_model = None
        self._upper_trade_fee = None

    @property
    def discount_dst_camp_prize_model(self):
        return self._discount_dst_camp_prize_model

    @discount_dst_camp_prize_model.setter
    def discount_dst_camp_prize_model(self, value):
        if isinstance(value, DiscountDstCampPrizeModel):
            self._discount_dst_camp_prize_model = value
        else:
            self._discount_dst_camp_prize_model = DiscountDstCampPrizeModel.from_alipay_dict(value)
    @property
    def lower_trade_fee(self):
        return self._lower_trade_fee

    @lower_trade_fee.setter
    def lower_trade_fee(self, value):
        self._lower_trade_fee = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def reduce_dst_camp_prize_model(self):
        return self._reduce_dst_camp_prize_model

    @reduce_dst_camp_prize_model.setter
    def reduce_dst_camp_prize_model(self, value):
        if isinstance(value, ReduceDstCampPrizeModel):
            self._reduce_dst_camp_prize_model = value
        else:
            self._reduce_dst_camp_prize_model = ReduceDstCampPrizeModel.from_alipay_dict(value)
    @property
    def reduce_to_amt_dst_camp_prize_model(self):
        return self._reduce_to_amt_dst_camp_prize_model

    @reduce_to_amt_dst_camp_prize_model.setter
    def reduce_to_amt_dst_camp_prize_model(self, value):
        if isinstance(value, ReduceToAmtDstCampPrizeModel):
            self._reduce_to_amt_dst_camp_prize_model = value
        else:
            self._reduce_to_amt_dst_camp_prize_model = ReduceToAmtDstCampPrizeModel.from_alipay_dict(value)
    @property
    def single_dst_camp_prize_model(self):
        return self._single_dst_camp_prize_model

    @single_dst_camp_prize_model.setter
    def single_dst_camp_prize_model(self, value):
        if isinstance(value, SingleDstCampPrizeModel):
            self._single_dst_camp_prize_model = value
        else:
            self._single_dst_camp_prize_model = SingleDstCampPrizeModel.from_alipay_dict(value)
    @property
    def upper_trade_fee(self):
        return self._upper_trade_fee

    @upper_trade_fee.setter
    def upper_trade_fee(self, value):
        self._upper_trade_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_dst_camp_prize_model:
            if hasattr(self.discount_dst_camp_prize_model, 'to_alipay_dict'):
                params['discount_dst_camp_prize_model'] = self.discount_dst_camp_prize_model.to_alipay_dict()
            else:
                params['discount_dst_camp_prize_model'] = self.discount_dst_camp_prize_model
        if self.lower_trade_fee:
            if hasattr(self.lower_trade_fee, 'to_alipay_dict'):
                params['lower_trade_fee'] = self.lower_trade_fee.to_alipay_dict()
            else:
                params['lower_trade_fee'] = self.lower_trade_fee
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.reduce_dst_camp_prize_model:
            if hasattr(self.reduce_dst_camp_prize_model, 'to_alipay_dict'):
                params['reduce_dst_camp_prize_model'] = self.reduce_dst_camp_prize_model.to_alipay_dict()
            else:
                params['reduce_dst_camp_prize_model'] = self.reduce_dst_camp_prize_model
        if self.reduce_to_amt_dst_camp_prize_model:
            if hasattr(self.reduce_to_amt_dst_camp_prize_model, 'to_alipay_dict'):
                params['reduce_to_amt_dst_camp_prize_model'] = self.reduce_to_amt_dst_camp_prize_model.to_alipay_dict()
            else:
                params['reduce_to_amt_dst_camp_prize_model'] = self.reduce_to_amt_dst_camp_prize_model
        if self.single_dst_camp_prize_model:
            if hasattr(self.single_dst_camp_prize_model, 'to_alipay_dict'):
                params['single_dst_camp_prize_model'] = self.single_dst_camp_prize_model.to_alipay_dict()
            else:
                params['single_dst_camp_prize_model'] = self.single_dst_camp_prize_model
        if self.upper_trade_fee:
            if hasattr(self.upper_trade_fee, 'to_alipay_dict'):
                params['upper_trade_fee'] = self.upper_trade_fee.to_alipay_dict()
            else:
                params['upper_trade_fee'] = self.upper_trade_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountRateModel()
        if 'discount_dst_camp_prize_model' in d:
            o.discount_dst_camp_prize_model = d['discount_dst_camp_prize_model']
        if 'lower_trade_fee' in d:
            o.lower_trade_fee = d['lower_trade_fee']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'reduce_dst_camp_prize_model' in d:
            o.reduce_dst_camp_prize_model = d['reduce_dst_camp_prize_model']
        if 'reduce_to_amt_dst_camp_prize_model' in d:
            o.reduce_to_amt_dst_camp_prize_model = d['reduce_to_amt_dst_camp_prize_model']
        if 'single_dst_camp_prize_model' in d:
            o.single_dst_camp_prize_model = d['single_dst_camp_prize_model']
        if 'upper_trade_fee' in d:
            o.upper_trade_fee = d['upper_trade_fee']
        return o



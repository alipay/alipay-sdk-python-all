#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstalmentPlanTuitionDTO import InstalmentPlanTuitionDTO
from alipay.aop.api.domain.RechargeConfigTuitionDTO import RechargeConfigTuitionDTO


class RechargeOrderTuitionDTO(object):

    def __init__(self):
        self._create_time = None
        self._finished_periods = None
        self._order_id = None
        self._partner_id = None
        self._periods = None
        self._plans = None
        self._recharge_config = None
        self._refund_type = None
        self._smid = None
        self._status = None
        self._total_amount = None
        self._trade_no = None
        self._user_display_name = None
        self._user_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def finished_periods(self):
        return self._finished_periods

    @finished_periods.setter
    def finished_periods(self, value):
        self._finished_periods = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, value):
        self._periods = value
    @property
    def plans(self):
        return self._plans

    @plans.setter
    def plans(self, value):
        if isinstance(value, list):
            self._plans = list()
            for i in value:
                if isinstance(i, InstalmentPlanTuitionDTO):
                    self._plans.append(i)
                else:
                    self._plans.append(InstalmentPlanTuitionDTO.from_alipay_dict(i))
    @property
    def recharge_config(self):
        return self._recharge_config

    @recharge_config.setter
    def recharge_config(self, value):
        if isinstance(value, RechargeConfigTuitionDTO):
            self._recharge_config = value
        else:
            self._recharge_config = RechargeConfigTuitionDTO.from_alipay_dict(value)
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_display_name(self):
        return self._user_display_name

    @user_display_name.setter
    def user_display_name(self, value):
        self._user_display_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.finished_periods:
            if hasattr(self.finished_periods, 'to_alipay_dict'):
                params['finished_periods'] = self.finished_periods.to_alipay_dict()
            else:
                params['finished_periods'] = self.finished_periods
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.periods:
            if hasattr(self.periods, 'to_alipay_dict'):
                params['periods'] = self.periods.to_alipay_dict()
            else:
                params['periods'] = self.periods
        if self.plans:
            if isinstance(self.plans, list):
                for i in range(0, len(self.plans)):
                    element = self.plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plans[i] = element.to_alipay_dict()
            if hasattr(self.plans, 'to_alipay_dict'):
                params['plans'] = self.plans.to_alipay_dict()
            else:
                params['plans'] = self.plans
        if self.recharge_config:
            if hasattr(self.recharge_config, 'to_alipay_dict'):
                params['recharge_config'] = self.recharge_config.to_alipay_dict()
            else:
                params['recharge_config'] = self.recharge_config
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_display_name:
            if hasattr(self.user_display_name, 'to_alipay_dict'):
                params['user_display_name'] = self.user_display_name.to_alipay_dict()
            else:
                params['user_display_name'] = self.user_display_name
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
        o = RechargeOrderTuitionDTO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'finished_periods' in d:
            o.finished_periods = d['finished_periods']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'periods' in d:
            o.periods = d['periods']
        if 'plans' in d:
            o.plans = d['plans']
        if 'recharge_config' in d:
            o.recharge_config = d['recharge_config']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'status' in d:
            o.status = d['status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_display_name' in d:
            o.user_display_name = d['user_display_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



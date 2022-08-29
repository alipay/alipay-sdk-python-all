#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZMGOCycleFlexConfig import ZMGOCycleFlexConfig
from alipay.aop.api.domain.ZMGOCycleWithholdConfig import ZMGOCycleWithholdConfig


class ZMGOSettlementConfig(object):

    def __init__(self):
        self._custom_fee_name = None
        self._cycle_flex_withhold_config = None
        self._cycle_withhold_config = None
        self._exp_stop_delay_days = None
        self._exp_stop_time = None
        self._exp_stop_time_mode = None
        self._fulfilltimes_custom_settlement_plan = None
        self._settlement_type = None

    @property
    def custom_fee_name(self):
        return self._custom_fee_name

    @custom_fee_name.setter
    def custom_fee_name(self, value):
        self._custom_fee_name = value
    @property
    def cycle_flex_withhold_config(self):
        return self._cycle_flex_withhold_config

    @cycle_flex_withhold_config.setter
    def cycle_flex_withhold_config(self, value):
        if isinstance(value, ZMGOCycleFlexConfig):
            self._cycle_flex_withhold_config = value
        else:
            self._cycle_flex_withhold_config = ZMGOCycleFlexConfig.from_alipay_dict(value)
    @property
    def cycle_withhold_config(self):
        return self._cycle_withhold_config

    @cycle_withhold_config.setter
    def cycle_withhold_config(self, value):
        if isinstance(value, ZMGOCycleWithholdConfig):
            self._cycle_withhold_config = value
        else:
            self._cycle_withhold_config = ZMGOCycleWithholdConfig.from_alipay_dict(value)
    @property
    def exp_stop_delay_days(self):
        return self._exp_stop_delay_days

    @exp_stop_delay_days.setter
    def exp_stop_delay_days(self, value):
        self._exp_stop_delay_days = value
    @property
    def exp_stop_time(self):
        return self._exp_stop_time

    @exp_stop_time.setter
    def exp_stop_time(self, value):
        self._exp_stop_time = value
    @property
    def exp_stop_time_mode(self):
        return self._exp_stop_time_mode

    @exp_stop_time_mode.setter
    def exp_stop_time_mode(self, value):
        self._exp_stop_time_mode = value
    @property
    def fulfilltimes_custom_settlement_plan(self):
        return self._fulfilltimes_custom_settlement_plan

    @fulfilltimes_custom_settlement_plan.setter
    def fulfilltimes_custom_settlement_plan(self, value):
        self._fulfilltimes_custom_settlement_plan = value
    @property
    def settlement_type(self):
        return self._settlement_type

    @settlement_type.setter
    def settlement_type(self, value):
        self._settlement_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_fee_name:
            if hasattr(self.custom_fee_name, 'to_alipay_dict'):
                params['custom_fee_name'] = self.custom_fee_name.to_alipay_dict()
            else:
                params['custom_fee_name'] = self.custom_fee_name
        if self.cycle_flex_withhold_config:
            if hasattr(self.cycle_flex_withhold_config, 'to_alipay_dict'):
                params['cycle_flex_withhold_config'] = self.cycle_flex_withhold_config.to_alipay_dict()
            else:
                params['cycle_flex_withhold_config'] = self.cycle_flex_withhold_config
        if self.cycle_withhold_config:
            if hasattr(self.cycle_withhold_config, 'to_alipay_dict'):
                params['cycle_withhold_config'] = self.cycle_withhold_config.to_alipay_dict()
            else:
                params['cycle_withhold_config'] = self.cycle_withhold_config
        if self.exp_stop_delay_days:
            if hasattr(self.exp_stop_delay_days, 'to_alipay_dict'):
                params['exp_stop_delay_days'] = self.exp_stop_delay_days.to_alipay_dict()
            else:
                params['exp_stop_delay_days'] = self.exp_stop_delay_days
        if self.exp_stop_time:
            if hasattr(self.exp_stop_time, 'to_alipay_dict'):
                params['exp_stop_time'] = self.exp_stop_time.to_alipay_dict()
            else:
                params['exp_stop_time'] = self.exp_stop_time
        if self.exp_stop_time_mode:
            if hasattr(self.exp_stop_time_mode, 'to_alipay_dict'):
                params['exp_stop_time_mode'] = self.exp_stop_time_mode.to_alipay_dict()
            else:
                params['exp_stop_time_mode'] = self.exp_stop_time_mode
        if self.fulfilltimes_custom_settlement_plan:
            if hasattr(self.fulfilltimes_custom_settlement_plan, 'to_alipay_dict'):
                params['fulfilltimes_custom_settlement_plan'] = self.fulfilltimes_custom_settlement_plan.to_alipay_dict()
            else:
                params['fulfilltimes_custom_settlement_plan'] = self.fulfilltimes_custom_settlement_plan
        if self.settlement_type:
            if hasattr(self.settlement_type, 'to_alipay_dict'):
                params['settlement_type'] = self.settlement_type.to_alipay_dict()
            else:
                params['settlement_type'] = self.settlement_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOSettlementConfig()
        if 'custom_fee_name' in d:
            o.custom_fee_name = d['custom_fee_name']
        if 'cycle_flex_withhold_config' in d:
            o.cycle_flex_withhold_config = d['cycle_flex_withhold_config']
        if 'cycle_withhold_config' in d:
            o.cycle_withhold_config = d['cycle_withhold_config']
        if 'exp_stop_delay_days' in d:
            o.exp_stop_delay_days = d['exp_stop_delay_days']
        if 'exp_stop_time' in d:
            o.exp_stop_time = d['exp_stop_time']
        if 'exp_stop_time_mode' in d:
            o.exp_stop_time_mode = d['exp_stop_time_mode']
        if 'fulfilltimes_custom_settlement_plan' in d:
            o.fulfilltimes_custom_settlement_plan = d['fulfilltimes_custom_settlement_plan']
        if 'settlement_type' in d:
            o.settlement_type = d['settlement_type']
        return o



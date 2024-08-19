#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitRewardConfig import BenefitRewardConfig


class BenefitRightOrderInfo(object):

    def __init__(self):
        self._order_id = None
        self._reward_config = None
        self._status = None
        self._unavailable_status = None
        self._use_status = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def reward_config(self):
        return self._reward_config

    @reward_config.setter
    def reward_config(self, value):
        if isinstance(value, BenefitRewardConfig):
            self._reward_config = value
        else:
            self._reward_config = BenefitRewardConfig.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unavailable_status(self):
        return self._unavailable_status

    @unavailable_status.setter
    def unavailable_status(self, value):
        self._unavailable_status = value
    @property
    def use_status(self):
        return self._use_status

    @use_status.setter
    def use_status(self, value):
        self._use_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.reward_config:
            if hasattr(self.reward_config, 'to_alipay_dict'):
                params['reward_config'] = self.reward_config.to_alipay_dict()
            else:
                params['reward_config'] = self.reward_config
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unavailable_status:
            if hasattr(self.unavailable_status, 'to_alipay_dict'):
                params['unavailable_status'] = self.unavailable_status.to_alipay_dict()
            else:
                params['unavailable_status'] = self.unavailable_status
        if self.use_status:
            if hasattr(self.use_status, 'to_alipay_dict'):
                params['use_status'] = self.use_status.to_alipay_dict()
            else:
                params['use_status'] = self.use_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRightOrderInfo()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'reward_config' in d:
            o.reward_config = d['reward_config']
        if 'status' in d:
            o.status = d['status']
        if 'unavailable_status' in d:
            o.unavailable_status = d['unavailable_status']
        if 'use_status' in d:
            o.use_status = d['use_status']
        return o



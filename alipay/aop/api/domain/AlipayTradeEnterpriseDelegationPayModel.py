#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeEnterpriseDelegationPayModel(object):

    def __init__(self):
        self._agreement_no = None
        self._enable_pay_channels = None
        self._prepay_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def enable_pay_channels(self):
        return self._enable_pay_channels

    @enable_pay_channels.setter
    def enable_pay_channels(self, value):
        self._enable_pay_channels = value
    @property
    def prepay_id(self):
        return self._prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self._prepay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.enable_pay_channels:
            if hasattr(self.enable_pay_channels, 'to_alipay_dict'):
                params['enable_pay_channels'] = self.enable_pay_channels.to_alipay_dict()
            else:
                params['enable_pay_channels'] = self.enable_pay_channels
        if self.prepay_id:
            if hasattr(self.prepay_id, 'to_alipay_dict'):
                params['prepay_id'] = self.prepay_id.to_alipay_dict()
            else:
                params['prepay_id'] = self.prepay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeEnterpriseDelegationPayModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'enable_pay_channels' in d:
            o.enable_pay_channels = d['enable_pay_channels']
        if 'prepay_id' in d:
            o.prepay_id = d['prepay_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiStagePayLineInfo import MultiStagePayLineInfo


class MultiStagePayInfo(object):

    def __init__(self):
        self._payment_mode = None
        self._stage_lines = None
        self._total_payment_amount = None

    @property
    def payment_mode(self):
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self._payment_mode = value
    @property
    def stage_lines(self):
        return self._stage_lines

    @stage_lines.setter
    def stage_lines(self, value):
        if isinstance(value, list):
            self._stage_lines = list()
            for i in value:
                if isinstance(i, MultiStagePayLineInfo):
                    self._stage_lines.append(i)
                else:
                    self._stage_lines.append(MultiStagePayLineInfo.from_alipay_dict(i))
    @property
    def total_payment_amount(self):
        return self._total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, value):
        self._total_payment_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_mode:
            if hasattr(self.payment_mode, 'to_alipay_dict'):
                params['payment_mode'] = self.payment_mode.to_alipay_dict()
            else:
                params['payment_mode'] = self.payment_mode
        if self.stage_lines:
            if isinstance(self.stage_lines, list):
                for i in range(0, len(self.stage_lines)):
                    element = self.stage_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stage_lines[i] = element.to_alipay_dict()
            if hasattr(self.stage_lines, 'to_alipay_dict'):
                params['stage_lines'] = self.stage_lines.to_alipay_dict()
            else:
                params['stage_lines'] = self.stage_lines
        if self.total_payment_amount:
            if hasattr(self.total_payment_amount, 'to_alipay_dict'):
                params['total_payment_amount'] = self.total_payment_amount.to_alipay_dict()
            else:
                params['total_payment_amount'] = self.total_payment_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiStagePayInfo()
        if 'payment_mode' in d:
            o.payment_mode = d['payment_mode']
        if 'stage_lines' in d:
            o.stage_lines = d['stage_lines']
        if 'total_payment_amount' in d:
            o.total_payment_amount = d['total_payment_amount']
        return o



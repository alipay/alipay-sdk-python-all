#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtravelHotelSupplyPriceDTO import EtravelHotelSupplyPriceDTO


class CancelInfoDTO(object):

    def __init__(self):
        self._cancel_code = None
        self._cancel_reason = None
        self._cancel_time = None
        self._penalty_amount = None

    @property
    def cancel_code(self):
        return self._cancel_code

    @cancel_code.setter
    def cancel_code(self, value):
        self._cancel_code = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def penalty_amount(self):
        return self._penalty_amount

    @penalty_amount.setter
    def penalty_amount(self, value):
        if isinstance(value, EtravelHotelSupplyPriceDTO):
            self._penalty_amount = value
        else:
            self._penalty_amount = EtravelHotelSupplyPriceDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_code:
            if hasattr(self.cancel_code, 'to_alipay_dict'):
                params['cancel_code'] = self.cancel_code.to_alipay_dict()
            else:
                params['cancel_code'] = self.cancel_code
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.penalty_amount:
            if hasattr(self.penalty_amount, 'to_alipay_dict'):
                params['penalty_amount'] = self.penalty_amount.to_alipay_dict()
            else:
                params['penalty_amount'] = self.penalty_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CancelInfoDTO()
        if 'cancel_code' in d:
            o.cancel_code = d['cancel_code']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'penalty_amount' in d:
            o.penalty_amount = d['penalty_amount']
        return o



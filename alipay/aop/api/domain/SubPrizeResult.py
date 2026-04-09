#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubPrizeResult(object):

    def __init__(self):
        self._reduce_amount = None
        self._sub_prize_status = None
        self._threshold_amount = None
        self._voucher_id = None

    @property
    def reduce_amount(self):
        return self._reduce_amount

    @reduce_amount.setter
    def reduce_amount(self, value):
        self._reduce_amount = value
    @property
    def sub_prize_status(self):
        return self._sub_prize_status

    @sub_prize_status.setter
    def sub_prize_status(self, value):
        self._sub_prize_status = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.reduce_amount:
            if hasattr(self.reduce_amount, 'to_alipay_dict'):
                params['reduce_amount'] = self.reduce_amount.to_alipay_dict()
            else:
                params['reduce_amount'] = self.reduce_amount
        if self.sub_prize_status:
            if hasattr(self.sub_prize_status, 'to_alipay_dict'):
                params['sub_prize_status'] = self.sub_prize_status.to_alipay_dict()
            else:
                params['sub_prize_status'] = self.sub_prize_status
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubPrizeResult()
        if 'reduce_amount' in d:
            o.reduce_amount = d['reduce_amount']
        if 'sub_prize_status' in d:
            o.sub_prize_status = d['sub_prize_status']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o



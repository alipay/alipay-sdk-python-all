#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferAmount import TransferAmount


class TransactionRequest(object):

    def __init__(self):
        self._biz_extend_info = None
        self._ref_transfer_id = None
        self._settle_amount = None

    @property
    def biz_extend_info(self):
        return self._biz_extend_info

    @biz_extend_info.setter
    def biz_extend_info(self, value):
        self._biz_extend_info = value
    @property
    def ref_transfer_id(self):
        return self._ref_transfer_id

    @ref_transfer_id.setter
    def ref_transfer_id(self, value):
        self._ref_transfer_id = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        if isinstance(value, TransferAmount):
            self._settle_amount = value
        else:
            self._settle_amount = TransferAmount.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_extend_info:
            if hasattr(self.biz_extend_info, 'to_alipay_dict'):
                params['biz_extend_info'] = self.biz_extend_info.to_alipay_dict()
            else:
                params['biz_extend_info'] = self.biz_extend_info
        if self.ref_transfer_id:
            if hasattr(self.ref_transfer_id, 'to_alipay_dict'):
                params['ref_transfer_id'] = self.ref_transfer_id.to_alipay_dict()
            else:
                params['ref_transfer_id'] = self.ref_transfer_id
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransactionRequest()
        if 'biz_extend_info' in d:
            o.biz_extend_info = d['biz_extend_info']
        if 'ref_transfer_id' in d:
            o.ref_transfer_id = d['ref_transfer_id']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        return o



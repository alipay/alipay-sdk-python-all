#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTailpaymentCancelModel(object):

    def __init__(self):
        self._cancel_reason = None
        self._tail_payment_id = None

    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def tail_payment_id(self):
        return self._tail_payment_id

    @tail_payment_id.setter
    def tail_payment_id(self, value):
        self._tail_payment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.tail_payment_id:
            if hasattr(self.tail_payment_id, 'to_alipay_dict'):
                params['tail_payment_id'] = self.tail_payment_id.to_alipay_dict()
            else:
                params['tail_payment_id'] = self.tail_payment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTailpaymentCancelModel()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'tail_payment_id' in d:
            o.tail_payment_id = d['tail_payment_id']
        return o



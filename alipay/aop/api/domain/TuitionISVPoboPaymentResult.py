#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVPoboImageDTO import TuitionISVPoboImageDTO


class TuitionISVPoboPaymentResult(object):

    def __init__(self):
        self._payment_id = None
        self._proof_list = None
        self._reason = None
        self._status = None

    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @property
    def proof_list(self):
        return self._proof_list

    @proof_list.setter
    def proof_list(self, value):
        if isinstance(value, list):
            self._proof_list = list()
            for i in value:
                if isinstance(i, TuitionISVPoboImageDTO):
                    self._proof_list.append(i)
                else:
                    self._proof_list.append(TuitionISVPoboImageDTO.from_alipay_dict(i))
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = self.payment_id.to_alipay_dict()
            else:
                params['payment_id'] = self.payment_id
        if self.proof_list:
            if isinstance(self.proof_list, list):
                for i in range(0, len(self.proof_list)):
                    element = self.proof_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.proof_list[i] = element.to_alipay_dict()
            if hasattr(self.proof_list, 'to_alipay_dict'):
                params['proof_list'] = self.proof_list.to_alipay_dict()
            else:
                params['proof_list'] = self.proof_list
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVPoboPaymentResult()
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'proof_list' in d:
            o.proof_list = d['proof_list']
        if 'reason' in d:
            o.reason = d['reason']
        if 'status' in d:
            o.status = d['status']
        return o



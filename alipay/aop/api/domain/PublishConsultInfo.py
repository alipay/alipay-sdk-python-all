#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PublishConsultInfo(object):

    def __init__(self):
        self._amount = None
        self._entity_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PublishConsultInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantServiceconsultQueryModel(object):

    def __init__(self):
        self._consult_event_id = None

    @property
    def consult_event_id(self):
        return self._consult_event_id

    @consult_event_id.setter
    def consult_event_id(self, value):
        self._consult_event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_event_id:
            if hasattr(self.consult_event_id, 'to_alipay_dict'):
                params['consult_event_id'] = self.consult_event_id.to_alipay_dict()
            else:
                params['consult_event_id'] = self.consult_event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantServiceconsultQueryModel()
        if 'consult_event_id' in d:
            o.consult_event_id = d['consult_event_id']
        return o



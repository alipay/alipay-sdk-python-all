#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantTradecomplainQueryModel(object):

    def __init__(self):
        self._complain_event_id = None

    @property
    def complain_event_id(self):
        return self._complain_event_id

    @complain_event_id.setter
    def complain_event_id(self, value):
        self._complain_event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_event_id:
            if hasattr(self.complain_event_id, 'to_alipay_dict'):
                params['complain_event_id'] = self.complain_event_id.to_alipay_dict()
            else:
                params['complain_event_id'] = self.complain_event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantTradecomplainQueryModel()
        if 'complain_event_id' in d:
            o.complain_event_id = d['complain_event_id']
        return o



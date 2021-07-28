#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeTicketUsedRefundModel(object):

    def __init__(self):
        self._request_id = None
        self._ticket_code = None
        self._trans_id = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value
    @property
    def trans_id(self):
        return self._trans_id

    @trans_id.setter
    def trans_id(self, value):
        self._trans_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.ticket_code:
            if hasattr(self.ticket_code, 'to_alipay_dict'):
                params['ticket_code'] = self.ticket_code.to_alipay_dict()
            else:
                params['ticket_code'] = self.ticket_code
        if self.trans_id:
            if hasattr(self.trans_id, 'to_alipay_dict'):
                params['trans_id'] = self.trans_id.to_alipay_dict()
            else:
                params['trans_id'] = self.trans_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeTicketUsedRefundModel()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'ticket_code' in d:
            o.ticket_code = d['ticket_code']
        if 'trans_id' in d:
            o.trans_id = d['trans_id']
        return o



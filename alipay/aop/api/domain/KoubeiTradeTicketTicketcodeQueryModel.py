#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeTicketTicketcodeQueryModel(object):

    def __init__(self):
        self._shop_id = None
        self._ticket_code = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.ticket_code:
            if hasattr(self.ticket_code, 'to_alipay_dict'):
                params['ticket_code'] = self.ticket_code.to_alipay_dict()
            else:
                params['ticket_code'] = self.ticket_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeTicketTicketcodeQueryModel()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'ticket_code' in d:
            o.ticket_code = d['ticket_code']
        return o



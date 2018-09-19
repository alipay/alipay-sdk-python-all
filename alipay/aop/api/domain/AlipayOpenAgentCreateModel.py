#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactModel import ContactModel


class AlipayOpenAgentCreateModel(object):

    def __init__(self):
        self._account = None
        self._contact_info = None
        self._order_ticket = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ContactModel):
            self._contact_info = value
        else:
            self._contact_info = ContactModel.from_alipay_dict(value)
    @property
    def order_ticket(self):
        return self._order_ticket

    @order_ticket.setter
    def order_ticket(self, value):
        self._order_ticket = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.order_ticket:
            if hasattr(self.order_ticket, 'to_alipay_dict'):
                params['order_ticket'] = self.order_ticket.to_alipay_dict()
            else:
                params['order_ticket'] = self.order_ticket
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentCreateModel()
        if 'account' in d:
            o.account = d['account']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'order_ticket' in d:
            o.order_ticket = d['order_ticket']
        return o



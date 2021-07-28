#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasRemitFundInitializeModel(object):

    def __init__(self):
        self._bc_remit_id = None
        self._compliance_mid = None
        self._extend_info = None
        self._quote_route_info = None
        self._receiver_amount = None
        self._receiver_currency = None
        self._receiver_info = None
        self._receiver_mid = None
        self._remark = None
        self._remit_purpose = None
        self._send_date = None
        self._sender_address = None
        self._sender_amount = None
        self._sender_currency = None
        self._sender_id = None
        self._sender_info = None
        self._sender_mid = None
        self._sender_nationality = None
        self._trans_currency = None

    @property
    def bc_remit_id(self):
        return self._bc_remit_id

    @bc_remit_id.setter
    def bc_remit_id(self, value):
        self._bc_remit_id = value
    @property
    def compliance_mid(self):
        return self._compliance_mid

    @compliance_mid.setter
    def compliance_mid(self, value):
        self._compliance_mid = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def quote_route_info(self):
        return self._quote_route_info

    @quote_route_info.setter
    def quote_route_info(self, value):
        self._quote_route_info = value
    @property
    def receiver_amount(self):
        return self._receiver_amount

    @receiver_amount.setter
    def receiver_amount(self, value):
        self._receiver_amount = value
    @property
    def receiver_currency(self):
        return self._receiver_currency

    @receiver_currency.setter
    def receiver_currency(self, value):
        self._receiver_currency = value
    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, value):
        self._receiver_info = value
    @property
    def receiver_mid(self):
        return self._receiver_mid

    @receiver_mid.setter
    def receiver_mid(self, value):
        self._receiver_mid = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def remit_purpose(self):
        return self._remit_purpose

    @remit_purpose.setter
    def remit_purpose(self, value):
        self._remit_purpose = value
    @property
    def send_date(self):
        return self._send_date

    @send_date.setter
    def send_date(self, value):
        self._send_date = value
    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, value):
        self._sender_address = value
    @property
    def sender_amount(self):
        return self._sender_amount

    @sender_amount.setter
    def sender_amount(self, value):
        self._sender_amount = value
    @property
    def sender_currency(self):
        return self._sender_currency

    @sender_currency.setter
    def sender_currency(self, value):
        self._sender_currency = value
    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value
    @property
    def sender_info(self):
        return self._sender_info

    @sender_info.setter
    def sender_info(self, value):
        self._sender_info = value
    @property
    def sender_mid(self):
        return self._sender_mid

    @sender_mid.setter
    def sender_mid(self, value):
        self._sender_mid = value
    @property
    def sender_nationality(self):
        return self._sender_nationality

    @sender_nationality.setter
    def sender_nationality(self, value):
        self._sender_nationality = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.bc_remit_id:
            if hasattr(self.bc_remit_id, 'to_alipay_dict'):
                params['bc_remit_id'] = self.bc_remit_id.to_alipay_dict()
            else:
                params['bc_remit_id'] = self.bc_remit_id
        if self.compliance_mid:
            if hasattr(self.compliance_mid, 'to_alipay_dict'):
                params['compliance_mid'] = self.compliance_mid.to_alipay_dict()
            else:
                params['compliance_mid'] = self.compliance_mid
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.quote_route_info:
            if hasattr(self.quote_route_info, 'to_alipay_dict'):
                params['quote_route_info'] = self.quote_route_info.to_alipay_dict()
            else:
                params['quote_route_info'] = self.quote_route_info
        if self.receiver_amount:
            if hasattr(self.receiver_amount, 'to_alipay_dict'):
                params['receiver_amount'] = self.receiver_amount.to_alipay_dict()
            else:
                params['receiver_amount'] = self.receiver_amount
        if self.receiver_currency:
            if hasattr(self.receiver_currency, 'to_alipay_dict'):
                params['receiver_currency'] = self.receiver_currency.to_alipay_dict()
            else:
                params['receiver_currency'] = self.receiver_currency
        if self.receiver_info:
            if hasattr(self.receiver_info, 'to_alipay_dict'):
                params['receiver_info'] = self.receiver_info.to_alipay_dict()
            else:
                params['receiver_info'] = self.receiver_info
        if self.receiver_mid:
            if hasattr(self.receiver_mid, 'to_alipay_dict'):
                params['receiver_mid'] = self.receiver_mid.to_alipay_dict()
            else:
                params['receiver_mid'] = self.receiver_mid
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.remit_purpose:
            if hasattr(self.remit_purpose, 'to_alipay_dict'):
                params['remit_purpose'] = self.remit_purpose.to_alipay_dict()
            else:
                params['remit_purpose'] = self.remit_purpose
        if self.send_date:
            if hasattr(self.send_date, 'to_alipay_dict'):
                params['send_date'] = self.send_date.to_alipay_dict()
            else:
                params['send_date'] = self.send_date
        if self.sender_address:
            if hasattr(self.sender_address, 'to_alipay_dict'):
                params['sender_address'] = self.sender_address.to_alipay_dict()
            else:
                params['sender_address'] = self.sender_address
        if self.sender_amount:
            if hasattr(self.sender_amount, 'to_alipay_dict'):
                params['sender_amount'] = self.sender_amount.to_alipay_dict()
            else:
                params['sender_amount'] = self.sender_amount
        if self.sender_currency:
            if hasattr(self.sender_currency, 'to_alipay_dict'):
                params['sender_currency'] = self.sender_currency.to_alipay_dict()
            else:
                params['sender_currency'] = self.sender_currency
        if self.sender_id:
            if hasattr(self.sender_id, 'to_alipay_dict'):
                params['sender_id'] = self.sender_id.to_alipay_dict()
            else:
                params['sender_id'] = self.sender_id
        if self.sender_info:
            if hasattr(self.sender_info, 'to_alipay_dict'):
                params['sender_info'] = self.sender_info.to_alipay_dict()
            else:
                params['sender_info'] = self.sender_info
        if self.sender_mid:
            if hasattr(self.sender_mid, 'to_alipay_dict'):
                params['sender_mid'] = self.sender_mid.to_alipay_dict()
            else:
                params['sender_mid'] = self.sender_mid
        if self.sender_nationality:
            if hasattr(self.sender_nationality, 'to_alipay_dict'):
                params['sender_nationality'] = self.sender_nationality.to_alipay_dict()
            else:
                params['sender_nationality'] = self.sender_nationality
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitFundInitializeModel()
        if 'bc_remit_id' in d:
            o.bc_remit_id = d['bc_remit_id']
        if 'compliance_mid' in d:
            o.compliance_mid = d['compliance_mid']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'quote_route_info' in d:
            o.quote_route_info = d['quote_route_info']
        if 'receiver_amount' in d:
            o.receiver_amount = d['receiver_amount']
        if 'receiver_currency' in d:
            o.receiver_currency = d['receiver_currency']
        if 'receiver_info' in d:
            o.receiver_info = d['receiver_info']
        if 'receiver_mid' in d:
            o.receiver_mid = d['receiver_mid']
        if 'remark' in d:
            o.remark = d['remark']
        if 'remit_purpose' in d:
            o.remit_purpose = d['remit_purpose']
        if 'send_date' in d:
            o.send_date = d['send_date']
        if 'sender_address' in d:
            o.sender_address = d['sender_address']
        if 'sender_amount' in d:
            o.sender_amount = d['sender_amount']
        if 'sender_currency' in d:
            o.sender_currency = d['sender_currency']
        if 'sender_id' in d:
            o.sender_id = d['sender_id']
        if 'sender_info' in d:
            o.sender_info = d['sender_info']
        if 'sender_mid' in d:
            o.sender_mid = d['sender_mid']
        if 'sender_nationality' in d:
            o.sender_nationality = d['sender_nationality']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        return o



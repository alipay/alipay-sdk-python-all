#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo


class GFAOpenAPIEventAcceptance(object):

    def __init__(self):
        self._agent_participant = None
        self._ar_no = None
        self._bill_amount = None
        self._currency = None
        self._event_code = None
        self._gmt_biz_trigger = None
        self._high_precision_bill_amount = None
        self._nonpayment_amount = None
        self._payee_participant = None
        self._payer_participant = None
        self._properties = None
        self._real_amount = None
        self._service_amount = None
        self._settle_participant = None
        self._sign_participant = None
        self._system_origin = None
        self._tax_amount = None
        self._trigger_pattern = None

    @property
    def agent_participant(self):
        return self._agent_participant

    @agent_participant.setter
    def agent_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._agent_participant = value
        else:
            self._agent_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def gmt_biz_trigger(self):
        return self._gmt_biz_trigger

    @gmt_biz_trigger.setter
    def gmt_biz_trigger(self, value):
        self._gmt_biz_trigger = value
    @property
    def high_precision_bill_amount(self):
        return self._high_precision_bill_amount

    @high_precision_bill_amount.setter
    def high_precision_bill_amount(self, value):
        self._high_precision_bill_amount = value
    @property
    def nonpayment_amount(self):
        return self._nonpayment_amount

    @nonpayment_amount.setter
    def nonpayment_amount(self, value):
        self._nonpayment_amount = value
    @property
    def payee_participant(self):
        return self._payee_participant

    @payee_participant.setter
    def payee_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._payee_participant = value
        else:
            self._payee_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def payer_participant(self):
        return self._payer_participant

    @payer_participant.setter
    def payer_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._payer_participant = value
        else:
            self._payer_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def settle_participant(self):
        return self._settle_participant

    @settle_participant.setter
    def settle_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._settle_participant = value
        else:
            self._settle_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def sign_participant(self):
        return self._sign_participant

    @sign_participant.setter
    def sign_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._sign_participant = value
        else:
            self._sign_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def system_origin(self):
        return self._system_origin

    @system_origin.setter
    def system_origin(self, value):
        self._system_origin = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def trigger_pattern(self):
        return self._trigger_pattern

    @trigger_pattern.setter
    def trigger_pattern(self, value):
        self._trigger_pattern = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_participant:
            if hasattr(self.agent_participant, 'to_alipay_dict'):
                params['agent_participant'] = self.agent_participant.to_alipay_dict()
            else:
                params['agent_participant'] = self.agent_participant
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.gmt_biz_trigger:
            if hasattr(self.gmt_biz_trigger, 'to_alipay_dict'):
                params['gmt_biz_trigger'] = self.gmt_biz_trigger.to_alipay_dict()
            else:
                params['gmt_biz_trigger'] = self.gmt_biz_trigger
        if self.high_precision_bill_amount:
            if hasattr(self.high_precision_bill_amount, 'to_alipay_dict'):
                params['high_precision_bill_amount'] = self.high_precision_bill_amount.to_alipay_dict()
            else:
                params['high_precision_bill_amount'] = self.high_precision_bill_amount
        if self.nonpayment_amount:
            if hasattr(self.nonpayment_amount, 'to_alipay_dict'):
                params['nonpayment_amount'] = self.nonpayment_amount.to_alipay_dict()
            else:
                params['nonpayment_amount'] = self.nonpayment_amount
        if self.payee_participant:
            if hasattr(self.payee_participant, 'to_alipay_dict'):
                params['payee_participant'] = self.payee_participant.to_alipay_dict()
            else:
                params['payee_participant'] = self.payee_participant
        if self.payer_participant:
            if hasattr(self.payer_participant, 'to_alipay_dict'):
                params['payer_participant'] = self.payer_participant.to_alipay_dict()
            else:
                params['payer_participant'] = self.payer_participant
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.settle_participant:
            if hasattr(self.settle_participant, 'to_alipay_dict'):
                params['settle_participant'] = self.settle_participant.to_alipay_dict()
            else:
                params['settle_participant'] = self.settle_participant
        if self.sign_participant:
            if hasattr(self.sign_participant, 'to_alipay_dict'):
                params['sign_participant'] = self.sign_participant.to_alipay_dict()
            else:
                params['sign_participant'] = self.sign_participant
        if self.system_origin:
            if hasattr(self.system_origin, 'to_alipay_dict'):
                params['system_origin'] = self.system_origin.to_alipay_dict()
            else:
                params['system_origin'] = self.system_origin
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.trigger_pattern:
            if hasattr(self.trigger_pattern, 'to_alipay_dict'):
                params['trigger_pattern'] = self.trigger_pattern.to_alipay_dict()
            else:
                params['trigger_pattern'] = self.trigger_pattern
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIEventAcceptance()
        if 'agent_participant' in d:
            o.agent_participant = d['agent_participant']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'gmt_biz_trigger' in d:
            o.gmt_biz_trigger = d['gmt_biz_trigger']
        if 'high_precision_bill_amount' in d:
            o.high_precision_bill_amount = d['high_precision_bill_amount']
        if 'nonpayment_amount' in d:
            o.nonpayment_amount = d['nonpayment_amount']
        if 'payee_participant' in d:
            o.payee_participant = d['payee_participant']
        if 'payer_participant' in d:
            o.payer_participant = d['payer_participant']
        if 'properties' in d:
            o.properties = d['properties']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'settle_participant' in d:
            o.settle_participant = d['settle_participant']
        if 'sign_participant' in d:
            o.sign_participant = d['sign_participant']
        if 'system_origin' in d:
            o.system_origin = d['system_origin']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'trigger_pattern' in d:
            o.trigger_pattern = d['trigger_pattern']
        return o



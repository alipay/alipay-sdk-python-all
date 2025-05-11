#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreightFlowParticipantInfo import FreightFlowParticipantInfo
from alipay.aop.api.domain.FreightFlowParticipantInfo import FreightFlowParticipantInfo


class AlipayCommerceLogisticsFreightflowTransferApplyModel(object):

    def __init__(self):
        self._amount = None
        self._biz_no = None
        self._currency = None
        self._logistics_code = None
        self._memo = None
        self._mode = None
        self._partner_id = None
        self._payee_participant = None
        self._payer_participant = None
        self._request_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def payee_participant(self):
        return self._payee_participant

    @payee_participant.setter
    def payee_participant(self, value):
        if isinstance(value, FreightFlowParticipantInfo):
            self._payee_participant = value
        else:
            self._payee_participant = FreightFlowParticipantInfo.from_alipay_dict(value)
    @property
    def payer_participant(self):
        return self._payer_participant

    @payer_participant.setter
    def payer_participant(self, value):
        if isinstance(value, FreightFlowParticipantInfo):
            self._payer_participant = value
        else:
            self._payer_participant = FreightFlowParticipantInfo.from_alipay_dict(value)
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
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
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowTransferApplyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mode' in d:
            o.mode = d['mode']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'payee_participant' in d:
            o.payee_participant = d['payee_participant']
        if 'payer_participant' in d:
            o.payer_participant = d['payer_participant']
        if 'request_time' in d:
            o.request_time = d['request_time']
        return o



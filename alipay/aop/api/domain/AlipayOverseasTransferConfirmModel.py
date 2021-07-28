#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.Money import Money


class AlipayOverseasTransferConfirmModel(object):

    def __init__(self):
        self._additional_transfer_details = None
        self._beneficiary_agent_id = None
        self._beneficiary_receipt_method = None
        self._biz_scene_type = None
        self._instructed_amount_type = None
        self._pass_through_info = None
        self._payer_agent_id = None
        self._payer_payment_method = None
        self._transfer_from_amount = None
        self._transfer_notify_url = None
        self._transfer_quote = None
        self._transfer_request_id = None
        self._transfer_to_amount = None

    @property
    def additional_transfer_details(self):
        return self._additional_transfer_details

    @additional_transfer_details.setter
    def additional_transfer_details(self, value):
        self._additional_transfer_details = value
    @property
    def beneficiary_agent_id(self):
        return self._beneficiary_agent_id

    @beneficiary_agent_id.setter
    def beneficiary_agent_id(self, value):
        self._beneficiary_agent_id = value
    @property
    def beneficiary_receipt_method(self):
        return self._beneficiary_receipt_method

    @beneficiary_receipt_method.setter
    def beneficiary_receipt_method(self, value):
        self._beneficiary_receipt_method = value
    @property
    def biz_scene_type(self):
        return self._biz_scene_type

    @biz_scene_type.setter
    def biz_scene_type(self, value):
        self._biz_scene_type = value
    @property
    def instructed_amount_type(self):
        return self._instructed_amount_type

    @instructed_amount_type.setter
    def instructed_amount_type(self, value):
        self._instructed_amount_type = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def payer_agent_id(self):
        return self._payer_agent_id

    @payer_agent_id.setter
    def payer_agent_id(self, value):
        self._payer_agent_id = value
    @property
    def payer_payment_method(self):
        return self._payer_payment_method

    @payer_payment_method.setter
    def payer_payment_method(self, value):
        self._payer_payment_method = value
    @property
    def transfer_from_amount(self):
        return self._transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        if isinstance(value, Money):
            self._transfer_from_amount = value
        else:
            self._transfer_from_amount = Money.from_alipay_dict(value)
    @property
    def transfer_notify_url(self):
        return self._transfer_notify_url

    @transfer_notify_url.setter
    def transfer_notify_url(self, value):
        self._transfer_notify_url = value
    @property
    def transfer_quote(self):
        return self._transfer_quote

    @transfer_quote.setter
    def transfer_quote(self, value):
        self._transfer_quote = value
    @property
    def transfer_request_id(self):
        return self._transfer_request_id

    @transfer_request_id.setter
    def transfer_request_id(self, value):
        self._transfer_request_id = value
    @property
    def transfer_to_amount(self):
        return self._transfer_to_amount

    @transfer_to_amount.setter
    def transfer_to_amount(self, value):
        if isinstance(value, Money):
            self._transfer_to_amount = value
        else:
            self._transfer_to_amount = Money.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.additional_transfer_details:
            if hasattr(self.additional_transfer_details, 'to_alipay_dict'):
                params['additional_transfer_details'] = self.additional_transfer_details.to_alipay_dict()
            else:
                params['additional_transfer_details'] = self.additional_transfer_details
        if self.beneficiary_agent_id:
            if hasattr(self.beneficiary_agent_id, 'to_alipay_dict'):
                params['beneficiary_agent_id'] = self.beneficiary_agent_id.to_alipay_dict()
            else:
                params['beneficiary_agent_id'] = self.beneficiary_agent_id
        if self.beneficiary_receipt_method:
            if hasattr(self.beneficiary_receipt_method, 'to_alipay_dict'):
                params['beneficiary_receipt_method'] = self.beneficiary_receipt_method.to_alipay_dict()
            else:
                params['beneficiary_receipt_method'] = self.beneficiary_receipt_method
        if self.biz_scene_type:
            if hasattr(self.biz_scene_type, 'to_alipay_dict'):
                params['biz_scene_type'] = self.biz_scene_type.to_alipay_dict()
            else:
                params['biz_scene_type'] = self.biz_scene_type
        if self.instructed_amount_type:
            if hasattr(self.instructed_amount_type, 'to_alipay_dict'):
                params['instructed_amount_type'] = self.instructed_amount_type.to_alipay_dict()
            else:
                params['instructed_amount_type'] = self.instructed_amount_type
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        if self.payer_agent_id:
            if hasattr(self.payer_agent_id, 'to_alipay_dict'):
                params['payer_agent_id'] = self.payer_agent_id.to_alipay_dict()
            else:
                params['payer_agent_id'] = self.payer_agent_id
        if self.payer_payment_method:
            if hasattr(self.payer_payment_method, 'to_alipay_dict'):
                params['payer_payment_method'] = self.payer_payment_method.to_alipay_dict()
            else:
                params['payer_payment_method'] = self.payer_payment_method
        if self.transfer_from_amount:
            if hasattr(self.transfer_from_amount, 'to_alipay_dict'):
                params['transfer_from_amount'] = self.transfer_from_amount.to_alipay_dict()
            else:
                params['transfer_from_amount'] = self.transfer_from_amount
        if self.transfer_notify_url:
            if hasattr(self.transfer_notify_url, 'to_alipay_dict'):
                params['transfer_notify_url'] = self.transfer_notify_url.to_alipay_dict()
            else:
                params['transfer_notify_url'] = self.transfer_notify_url
        if self.transfer_quote:
            if hasattr(self.transfer_quote, 'to_alipay_dict'):
                params['transfer_quote'] = self.transfer_quote.to_alipay_dict()
            else:
                params['transfer_quote'] = self.transfer_quote
        if self.transfer_request_id:
            if hasattr(self.transfer_request_id, 'to_alipay_dict'):
                params['transfer_request_id'] = self.transfer_request_id.to_alipay_dict()
            else:
                params['transfer_request_id'] = self.transfer_request_id
        if self.transfer_to_amount:
            if hasattr(self.transfer_to_amount, 'to_alipay_dict'):
                params['transfer_to_amount'] = self.transfer_to_amount.to_alipay_dict()
            else:
                params['transfer_to_amount'] = self.transfer_to_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTransferConfirmModel()
        if 'additional_transfer_details' in d:
            o.additional_transfer_details = d['additional_transfer_details']
        if 'beneficiary_agent_id' in d:
            o.beneficiary_agent_id = d['beneficiary_agent_id']
        if 'beneficiary_receipt_method' in d:
            o.beneficiary_receipt_method = d['beneficiary_receipt_method']
        if 'biz_scene_type' in d:
            o.biz_scene_type = d['biz_scene_type']
        if 'instructed_amount_type' in d:
            o.instructed_amount_type = d['instructed_amount_type']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'payer_payment_method' in d:
            o.payer_payment_method = d['payer_payment_method']
        if 'transfer_from_amount' in d:
            o.transfer_from_amount = d['transfer_from_amount']
        if 'transfer_notify_url' in d:
            o.transfer_notify_url = d['transfer_notify_url']
        if 'transfer_quote' in d:
            o.transfer_quote = d['transfer_quote']
        if 'transfer_request_id' in d:
            o.transfer_request_id = d['transfer_request_id']
        if 'transfer_to_amount' in d:
            o.transfer_to_amount = d['transfer_to_amount']
        return o



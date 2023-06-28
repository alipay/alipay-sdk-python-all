#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.Money import Money


class AlipayOverseasRemitNotifyModel(object):

    def __init__(self):
        self._additional_beneficiary_details = None
        self._beneficiary_agent_id = None
        self._compliance_result = None
        self._instructed_amount_type = None
        self._pass_through_info = None
        self._payer_agent_id = None
        self._transfer_from_amount = None
        self._transfer_id = None
        self._transfer_quote = None
        self._transfer_request_id = None
        self._transfer_result = None
        self._transfer_time = None
        self._transfer_to_amount = None

    @property
    def additional_beneficiary_details(self):
        return self._additional_beneficiary_details

    @additional_beneficiary_details.setter
    def additional_beneficiary_details(self, value):
        self._additional_beneficiary_details = value
    @property
    def beneficiary_agent_id(self):
        return self._beneficiary_agent_id

    @beneficiary_agent_id.setter
    def beneficiary_agent_id(self, value):
        self._beneficiary_agent_id = value
    @property
    def compliance_result(self):
        return self._compliance_result

    @compliance_result.setter
    def compliance_result(self, value):
        self._compliance_result = value
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
    def transfer_from_amount(self):
        return self._transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        if isinstance(value, Money):
            self._transfer_from_amount = value
        else:
            self._transfer_from_amount = Money.from_alipay_dict(value)
    @property
    def transfer_id(self):
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, value):
        self._transfer_id = value
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
    def transfer_result(self):
        return self._transfer_result

    @transfer_result.setter
    def transfer_result(self, value):
        self._transfer_result = value
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value
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
        if self.additional_beneficiary_details:
            if hasattr(self.additional_beneficiary_details, 'to_alipay_dict'):
                params['additional_beneficiary_details'] = self.additional_beneficiary_details.to_alipay_dict()
            else:
                params['additional_beneficiary_details'] = self.additional_beneficiary_details
        if self.beneficiary_agent_id:
            if hasattr(self.beneficiary_agent_id, 'to_alipay_dict'):
                params['beneficiary_agent_id'] = self.beneficiary_agent_id.to_alipay_dict()
            else:
                params['beneficiary_agent_id'] = self.beneficiary_agent_id
        if self.compliance_result:
            if hasattr(self.compliance_result, 'to_alipay_dict'):
                params['compliance_result'] = self.compliance_result.to_alipay_dict()
            else:
                params['compliance_result'] = self.compliance_result
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
        if self.transfer_from_amount:
            if hasattr(self.transfer_from_amount, 'to_alipay_dict'):
                params['transfer_from_amount'] = self.transfer_from_amount.to_alipay_dict()
            else:
                params['transfer_from_amount'] = self.transfer_from_amount
        if self.transfer_id:
            if hasattr(self.transfer_id, 'to_alipay_dict'):
                params['transfer_id'] = self.transfer_id.to_alipay_dict()
            else:
                params['transfer_id'] = self.transfer_id
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
        if self.transfer_result:
            if hasattr(self.transfer_result, 'to_alipay_dict'):
                params['transfer_result'] = self.transfer_result.to_alipay_dict()
            else:
                params['transfer_result'] = self.transfer_result
        if self.transfer_time:
            if hasattr(self.transfer_time, 'to_alipay_dict'):
                params['transfer_time'] = self.transfer_time.to_alipay_dict()
            else:
                params['transfer_time'] = self.transfer_time
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
        o = AlipayOverseasRemitNotifyModel()
        if 'additional_beneficiary_details' in d:
            o.additional_beneficiary_details = d['additional_beneficiary_details']
        if 'beneficiary_agent_id' in d:
            o.beneficiary_agent_id = d['beneficiary_agent_id']
        if 'compliance_result' in d:
            o.compliance_result = d['compliance_result']
        if 'instructed_amount_type' in d:
            o.instructed_amount_type = d['instructed_amount_type']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'transfer_from_amount' in d:
            o.transfer_from_amount = d['transfer_from_amount']
        if 'transfer_id' in d:
            o.transfer_id = d['transfer_id']
        if 'transfer_quote' in d:
            o.transfer_quote = d['transfer_quote']
        if 'transfer_request_id' in d:
            o.transfer_request_id = d['transfer_request_id']
        if 'transfer_result' in d:
            o.transfer_result = d['transfer_result']
        if 'transfer_time' in d:
            o.transfer_time = d['transfer_time']
        if 'transfer_to_amount' in d:
            o.transfer_to_amount = d['transfer_to_amount']
        return o



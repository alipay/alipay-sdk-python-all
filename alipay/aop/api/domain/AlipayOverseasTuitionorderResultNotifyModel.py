#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdditionBeneficiary import AdditionBeneficiary
from alipay.aop.api.domain.AdditionalTransferDetail import AdditionalTransferDetail
from alipay.aop.api.domain.Compliance import Compliance
from alipay.aop.api.domain.Promo import Promo
from alipay.aop.api.domain.TransferFromAmount import TransferFromAmount
from alipay.aop.api.domain.RemitTransferQuotew import RemitTransferQuotew
from alipay.aop.api.domain.TransferResultInfow import TransferResultInfow
from alipay.aop.api.domain.TransferToAmount import TransferToAmount


class AlipayOverseasTuitionorderResultNotifyModel(object):

    def __init__(self):
        self._additional_beneficiary_details = None
        self._additional_transfer_to_details = None
        self._beneficiary_agent_id = None
        self._compliance_result = None
        self._fund_out_status = None
        self._instructed_amount_type = None
        self._notify_type = None
        self._payer_agent_id = None
        self._promo_detail = None
        self._transfer_from_amount = None
        self._transfer_id = None
        self._transfer_quote = None
        self._transfer_request_id = None
        self._transfer_result = None
        self._transfer_time = None
        self._transfer_to_amount = None
        self._uetr = None

    @property
    def additional_beneficiary_details(self):
        return self._additional_beneficiary_details

    @additional_beneficiary_details.setter
    def additional_beneficiary_details(self, value):
        if isinstance(value, AdditionBeneficiary):
            self._additional_beneficiary_details = value
        else:
            self._additional_beneficiary_details = AdditionBeneficiary.from_alipay_dict(value)
    @property
    def additional_transfer_to_details(self):
        return self._additional_transfer_to_details

    @additional_transfer_to_details.setter
    def additional_transfer_to_details(self, value):
        if isinstance(value, AdditionalTransferDetail):
            self._additional_transfer_to_details = value
        else:
            self._additional_transfer_to_details = AdditionalTransferDetail.from_alipay_dict(value)
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
        if isinstance(value, Compliance):
            self._compliance_result = value
        else:
            self._compliance_result = Compliance.from_alipay_dict(value)
    @property
    def fund_out_status(self):
        return self._fund_out_status

    @fund_out_status.setter
    def fund_out_status(self, value):
        self._fund_out_status = value
    @property
    def instructed_amount_type(self):
        return self._instructed_amount_type

    @instructed_amount_type.setter
    def instructed_amount_type(self, value):
        self._instructed_amount_type = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def payer_agent_id(self):
        return self._payer_agent_id

    @payer_agent_id.setter
    def payer_agent_id(self, value):
        self._payer_agent_id = value
    @property
    def promo_detail(self):
        return self._promo_detail

    @promo_detail.setter
    def promo_detail(self, value):
        if isinstance(value, Promo):
            self._promo_detail = value
        else:
            self._promo_detail = Promo.from_alipay_dict(value)
    @property
    def transfer_from_amount(self):
        return self._transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        if isinstance(value, TransferFromAmount):
            self._transfer_from_amount = value
        else:
            self._transfer_from_amount = TransferFromAmount.from_alipay_dict(value)
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
        if isinstance(value, RemitTransferQuotew):
            self._transfer_quote = value
        else:
            self._transfer_quote = RemitTransferQuotew.from_alipay_dict(value)
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
        if isinstance(value, TransferResultInfow):
            self._transfer_result = value
        else:
            self._transfer_result = TransferResultInfow.from_alipay_dict(value)
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
        if isinstance(value, TransferToAmount):
            self._transfer_to_amount = value
        else:
            self._transfer_to_amount = TransferToAmount.from_alipay_dict(value)
    @property
    def uetr(self):
        return self._uetr

    @uetr.setter
    def uetr(self, value):
        self._uetr = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_beneficiary_details:
            if hasattr(self.additional_beneficiary_details, 'to_alipay_dict'):
                params['additional_beneficiary_details'] = self.additional_beneficiary_details.to_alipay_dict()
            else:
                params['additional_beneficiary_details'] = self.additional_beneficiary_details
        if self.additional_transfer_to_details:
            if hasattr(self.additional_transfer_to_details, 'to_alipay_dict'):
                params['additional_transfer_to_details'] = self.additional_transfer_to_details.to_alipay_dict()
            else:
                params['additional_transfer_to_details'] = self.additional_transfer_to_details
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
        if self.fund_out_status:
            if hasattr(self.fund_out_status, 'to_alipay_dict'):
                params['fund_out_status'] = self.fund_out_status.to_alipay_dict()
            else:
                params['fund_out_status'] = self.fund_out_status
        if self.instructed_amount_type:
            if hasattr(self.instructed_amount_type, 'to_alipay_dict'):
                params['instructed_amount_type'] = self.instructed_amount_type.to_alipay_dict()
            else:
                params['instructed_amount_type'] = self.instructed_amount_type
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.payer_agent_id:
            if hasattr(self.payer_agent_id, 'to_alipay_dict'):
                params['payer_agent_id'] = self.payer_agent_id.to_alipay_dict()
            else:
                params['payer_agent_id'] = self.payer_agent_id
        if self.promo_detail:
            if hasattr(self.promo_detail, 'to_alipay_dict'):
                params['promo_detail'] = self.promo_detail.to_alipay_dict()
            else:
                params['promo_detail'] = self.promo_detail
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
        if self.uetr:
            if hasattr(self.uetr, 'to_alipay_dict'):
                params['uetr'] = self.uetr.to_alipay_dict()
            else:
                params['uetr'] = self.uetr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTuitionorderResultNotifyModel()
        if 'additional_beneficiary_details' in d:
            o.additional_beneficiary_details = d['additional_beneficiary_details']
        if 'additional_transfer_to_details' in d:
            o.additional_transfer_to_details = d['additional_transfer_to_details']
        if 'beneficiary_agent_id' in d:
            o.beneficiary_agent_id = d['beneficiary_agent_id']
        if 'compliance_result' in d:
            o.compliance_result = d['compliance_result']
        if 'fund_out_status' in d:
            o.fund_out_status = d['fund_out_status']
        if 'instructed_amount_type' in d:
            o.instructed_amount_type = d['instructed_amount_type']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'promo_detail' in d:
            o.promo_detail = d['promo_detail']
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
        if 'uetr' in d:
            o.uetr = d['uetr']
        return o



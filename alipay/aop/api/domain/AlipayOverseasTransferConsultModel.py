#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money


class AlipayOverseasTransferConsultModel(object):

    def __init__(self):
        self._additional_transfer_details = None
        self._beneficiary_receipt_method = None
        self._biz_scene_type = None
        self._pass_through_info = None
        self._payer_agent_id = None
        self._transfer_to_amount = None

    @property
    def additional_transfer_details(self):
        return self._additional_transfer_details

    @additional_transfer_details.setter
    def additional_transfer_details(self, value):
        self._additional_transfer_details = value
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
        o = AlipayOverseasTransferConsultModel()
        if 'additional_transfer_details' in d:
            o.additional_transfer_details = d['additional_transfer_details']
        if 'beneficiary_receipt_method' in d:
            o.beneficiary_receipt_method = d['beneficiary_receipt_method']
        if 'biz_scene_type' in d:
            o.biz_scene_type = d['biz_scene_type']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'transfer_to_amount' in d:
            o.transfer_to_amount = d['transfer_to_amount']
        return o



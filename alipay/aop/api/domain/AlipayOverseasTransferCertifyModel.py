#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.Money import Money


class AlipayOverseasTransferCertifyModel(object):

    def __init__(self):
        self._beneficiary = None
        self._beneficiary_agent_id = None
        self._beneficiary_receipt_method = None
        self._biz_scene_type = None
        self._instructed_amount_type = None
        self._pass_through_info = None
        self._payer = None
        self._payer_agent_id = None
        self._sub_transfer_purpose = None
        self._transfer_from_amount = None
        self._transfer_from_region = None
        self._transfer_purpose = None
        self._transfer_to_amount = None
        self._transfer_to_region = None

    @property
    def beneficiary(self):
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, value):
        self._beneficiary = value
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
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        self._payer = value
    @property
    def payer_agent_id(self):
        return self._payer_agent_id

    @payer_agent_id.setter
    def payer_agent_id(self, value):
        self._payer_agent_id = value
    @property
    def sub_transfer_purpose(self):
        return self._sub_transfer_purpose

    @sub_transfer_purpose.setter
    def sub_transfer_purpose(self, value):
        self._sub_transfer_purpose = value
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
    def transfer_from_region(self):
        return self._transfer_from_region

    @transfer_from_region.setter
    def transfer_from_region(self, value):
        self._transfer_from_region = value
    @property
    def transfer_purpose(self):
        return self._transfer_purpose

    @transfer_purpose.setter
    def transfer_purpose(self, value):
        self._transfer_purpose = value
    @property
    def transfer_to_amount(self):
        return self._transfer_to_amount

    @transfer_to_amount.setter
    def transfer_to_amount(self, value):
        if isinstance(value, Money):
            self._transfer_to_amount = value
        else:
            self._transfer_to_amount = Money.from_alipay_dict(value)
    @property
    def transfer_to_region(self):
        return self._transfer_to_region

    @transfer_to_region.setter
    def transfer_to_region(self, value):
        self._transfer_to_region = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary:
            if hasattr(self.beneficiary, 'to_alipay_dict'):
                params['beneficiary'] = self.beneficiary.to_alipay_dict()
            else:
                params['beneficiary'] = self.beneficiary
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
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        if self.payer_agent_id:
            if hasattr(self.payer_agent_id, 'to_alipay_dict'):
                params['payer_agent_id'] = self.payer_agent_id.to_alipay_dict()
            else:
                params['payer_agent_id'] = self.payer_agent_id
        if self.sub_transfer_purpose:
            if hasattr(self.sub_transfer_purpose, 'to_alipay_dict'):
                params['sub_transfer_purpose'] = self.sub_transfer_purpose.to_alipay_dict()
            else:
                params['sub_transfer_purpose'] = self.sub_transfer_purpose
        if self.transfer_from_amount:
            if hasattr(self.transfer_from_amount, 'to_alipay_dict'):
                params['transfer_from_amount'] = self.transfer_from_amount.to_alipay_dict()
            else:
                params['transfer_from_amount'] = self.transfer_from_amount
        if self.transfer_from_region:
            if hasattr(self.transfer_from_region, 'to_alipay_dict'):
                params['transfer_from_region'] = self.transfer_from_region.to_alipay_dict()
            else:
                params['transfer_from_region'] = self.transfer_from_region
        if self.transfer_purpose:
            if hasattr(self.transfer_purpose, 'to_alipay_dict'):
                params['transfer_purpose'] = self.transfer_purpose.to_alipay_dict()
            else:
                params['transfer_purpose'] = self.transfer_purpose
        if self.transfer_to_amount:
            if hasattr(self.transfer_to_amount, 'to_alipay_dict'):
                params['transfer_to_amount'] = self.transfer_to_amount.to_alipay_dict()
            else:
                params['transfer_to_amount'] = self.transfer_to_amount
        if self.transfer_to_region:
            if hasattr(self.transfer_to_region, 'to_alipay_dict'):
                params['transfer_to_region'] = self.transfer_to_region.to_alipay_dict()
            else:
                params['transfer_to_region'] = self.transfer_to_region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTransferCertifyModel()
        if 'beneficiary' in d:
            o.beneficiary = d['beneficiary']
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
        if 'payer' in d:
            o.payer = d['payer']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'sub_transfer_purpose' in d:
            o.sub_transfer_purpose = d['sub_transfer_purpose']
        if 'transfer_from_amount' in d:
            o.transfer_from_amount = d['transfer_from_amount']
        if 'transfer_from_region' in d:
            o.transfer_from_region = d['transfer_from_region']
        if 'transfer_purpose' in d:
            o.transfer_purpose = d['transfer_purpose']
        if 'transfer_to_amount' in d:
            o.transfer_to_amount = d['transfer_to_amount']
        if 'transfer_to_region' in d:
            o.transfer_to_region = d['transfer_to_region']
        return o



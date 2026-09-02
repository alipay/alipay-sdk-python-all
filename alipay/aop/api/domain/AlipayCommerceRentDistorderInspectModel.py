#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistributionOrderInspectDeductFeeDTO import DistributionOrderInspectDeductFeeDTO
from alipay.aop.api.domain.DistributionOrderInspectProofDTO import DistributionOrderInspectProofDTO


class AlipayCommerceRentDistorderInspectModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._channel_buyer_id = None
        self._channel_order_id = None
        self._deduct_fees = None
        self._distribution_channel = None
        self._inspection_result = None
        self._proof = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def channel_buyer_id(self):
        return self._channel_buyer_id

    @channel_buyer_id.setter
    def channel_buyer_id(self, value):
        self._channel_buyer_id = value
    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def deduct_fees(self):
        return self._deduct_fees

    @deduct_fees.setter
    def deduct_fees(self, value):
        if isinstance(value, list):
            self._deduct_fees = list()
            for i in value:
                if isinstance(i, DistributionOrderInspectDeductFeeDTO):
                    self._deduct_fees.append(i)
                else:
                    self._deduct_fees.append(DistributionOrderInspectDeductFeeDTO.from_alipay_dict(i))
    @property
    def distribution_channel(self):
        return self._distribution_channel

    @distribution_channel.setter
    def distribution_channel(self, value):
        self._distribution_channel = value
    @property
    def inspection_result(self):
        return self._inspection_result

    @inspection_result.setter
    def inspection_result(self, value):
        self._inspection_result = value
    @property
    def proof(self):
        return self._proof

    @proof.setter
    def proof(self, value):
        if isinstance(value, DistributionOrderInspectProofDTO):
            self._proof = value
        else:
            self._proof = DistributionOrderInspectProofDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.channel_buyer_id:
            if hasattr(self.channel_buyer_id, 'to_alipay_dict'):
                params['channel_buyer_id'] = self.channel_buyer_id.to_alipay_dict()
            else:
                params['channel_buyer_id'] = self.channel_buyer_id
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.deduct_fees:
            if isinstance(self.deduct_fees, list):
                for i in range(0, len(self.deduct_fees)):
                    element = self.deduct_fees[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduct_fees[i] = element.to_alipay_dict()
            if hasattr(self.deduct_fees, 'to_alipay_dict'):
                params['deduct_fees'] = self.deduct_fees.to_alipay_dict()
            else:
                params['deduct_fees'] = self.deduct_fees
        if self.distribution_channel:
            if hasattr(self.distribution_channel, 'to_alipay_dict'):
                params['distribution_channel'] = self.distribution_channel.to_alipay_dict()
            else:
                params['distribution_channel'] = self.distribution_channel
        if self.inspection_result:
            if hasattr(self.inspection_result, 'to_alipay_dict'):
                params['inspection_result'] = self.inspection_result.to_alipay_dict()
            else:
                params['inspection_result'] = self.inspection_result
        if self.proof:
            if hasattr(self.proof, 'to_alipay_dict'):
                params['proof'] = self.proof.to_alipay_dict()
            else:
                params['proof'] = self.proof
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentDistorderInspectModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'channel_buyer_id' in d:
            o.channel_buyer_id = d['channel_buyer_id']
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'deduct_fees' in d:
            o.deduct_fees = d['deduct_fees']
        if 'distribution_channel' in d:
            o.distribution_channel = d['distribution_channel']
        if 'inspection_result' in d:
            o.inspection_result = d['inspection_result']
        if 'proof' in d:
            o.proof = d['proof']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVAmountInfoDTO import IndrISVAmountInfoDTO
from alipay.aop.api.domain.IndrISVAmountInfoDTO import IndrISVAmountInfoDTO
from alipay.aop.api.domain.IndrISVResult import IndrISVResult
from alipay.aop.api.domain.IndrISVOrderStatusDTO import IndrISVOrderStatusDTO


class AlipayOverseasOpenIndrpreorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrpreorderQueryResponse, self).__init__()
        self._payment_amount = None
        self._pre_order_id = None
        self._refund_amount = None
        self._result = None
        self._scene_type = None
        self._status = None

    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        if isinstance(value, IndrISVAmountInfoDTO):
            self._payment_amount = value
        else:
            self._payment_amount = IndrISVAmountInfoDTO.from_alipay_dict(value)
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, IndrISVAmountInfoDTO):
            self._refund_amount = value
        else:
            self._refund_amount = IndrISVAmountInfoDTO.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, IndrISVOrderStatusDTO):
            self._status = value
        else:
            self._status = IndrISVOrderStatusDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenIndrpreorderQueryResponse, self).parse_response_content(response_content)
        if 'payment_amount' in response:
            self.payment_amount = response['payment_amount']
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'result' in response:
            self.result = response['result']
        if 'scene_type' in response:
            self.scene_type = response['scene_type']
        if 'status' in response:
            self.status = response['status']

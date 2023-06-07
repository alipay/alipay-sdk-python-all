#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefundPaymentAssetInfo import RefundPaymentAssetInfo


class AlipayFundWalletOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletOrderQueryResponse, self).__init__()
        self._actual_amount = None
        self._execute_time = None
        self._refund_payment_asset_infos = None
        self._total_amount = None
        self._trans_status = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def refund_payment_asset_infos(self):
        return self._refund_payment_asset_infos

    @refund_payment_asset_infos.setter
    def refund_payment_asset_infos(self, value):
        if isinstance(value, list):
            self._refund_payment_asset_infos = list()
            for i in value:
                if isinstance(i, RefundPaymentAssetInfo):
                    self._refund_payment_asset_infos.append(i)
                else:
                    self._refund_payment_asset_infos.append(RefundPaymentAssetInfo.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trans_status(self):
        return self._trans_status

    @trans_status.setter
    def trans_status(self, value):
        self._trans_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletOrderQueryResponse, self).parse_response_content(response_content)
        if 'actual_amount' in response:
            self.actual_amount = response['actual_amount']
        if 'execute_time' in response:
            self.execute_time = response['execute_time']
        if 'refund_payment_asset_infos' in response:
            self.refund_payment_asset_infos = response['refund_payment_asset_infos']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trans_status' in response:
            self.trans_status = response['trans_status']

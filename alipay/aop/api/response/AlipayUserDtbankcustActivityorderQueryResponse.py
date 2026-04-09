#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CombinePrizeResult import CombinePrizeResult


class AlipayUserDtbankcustActivityorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustActivityorderQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_order_id = None
        self._combine_prize_result = None
        self._out_biz_no = None
        self._status = None
        self._voucher_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def combine_prize_result(self):
        return self._combine_prize_result

    @combine_prize_result.setter
    def combine_prize_result(self, value):
        if isinstance(value, CombinePrizeResult):
            self._combine_prize_result = value
        else:
            self._combine_prize_result = CombinePrizeResult.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustActivityorderQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_order_id' in response:
            self.activity_order_id = response['activity_order_id']
        if 'combine_prize_result' in response:
            self.combine_prize_result = response['combine_prize_result']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']

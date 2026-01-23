#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowCloudfundrefundApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowCloudfundrefundApplyResponse, self).__init__()
        self._biz_no = None
        self._cloud_fund_order_no = None
        self._participant_id = None
        self._participant_type = None
        self._refund_apply_msg = None
        self._refund_apply_status = None
        self._refund_order_no = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def cloud_fund_order_no(self):
        return self._cloud_fund_order_no

    @cloud_fund_order_no.setter
    def cloud_fund_order_no(self, value):
        self._cloud_fund_order_no = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value
    @property
    def refund_apply_msg(self):
        return self._refund_apply_msg

    @refund_apply_msg.setter
    def refund_apply_msg(self, value):
        self._refund_apply_msg = value
    @property
    def refund_apply_status(self):
        return self._refund_apply_status

    @refund_apply_status.setter
    def refund_apply_status(self, value):
        self._refund_apply_status = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowCloudfundrefundApplyResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'cloud_fund_order_no' in response:
            self.cloud_fund_order_no = response['cloud_fund_order_no']
        if 'participant_id' in response:
            self.participant_id = response['participant_id']
        if 'participant_type' in response:
            self.participant_type = response['participant_type']
        if 'refund_apply_msg' in response:
            self.refund_apply_msg = response['refund_apply_msg']
        if 'refund_apply_status' in response:
            self.refund_apply_status = response['refund_apply_status']
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']

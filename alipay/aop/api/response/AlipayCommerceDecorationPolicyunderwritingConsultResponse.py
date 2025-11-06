#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubOrderVO import SubOrderVO


class AlipayCommerceDecorationPolicyunderwritingConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationPolicyunderwritingConsultResponse, self).__init__()
        self._message = None
        self._order_no = None
        self._policy_end_date = None
        self._policy_start_date = None
        self._policy_status = None
        self._premium = None
        self._sub_order_no_list = None
        self._total_premium = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def policy_end_date(self):
        return self._policy_end_date

    @policy_end_date.setter
    def policy_end_date(self, value):
        self._policy_end_date = value
    @property
    def policy_start_date(self):
        return self._policy_start_date

    @policy_start_date.setter
    def policy_start_date(self, value):
        self._policy_start_date = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sub_order_no_list(self):
        return self._sub_order_no_list

    @sub_order_no_list.setter
    def sub_order_no_list(self, value):
        if isinstance(value, list):
            self._sub_order_no_list = list()
            for i in value:
                if isinstance(i, SubOrderVO):
                    self._sub_order_no_list.append(i)
                else:
                    self._sub_order_no_list.append(SubOrderVO.from_alipay_dict(i))
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationPolicyunderwritingConsultResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'policy_end_date' in response:
            self.policy_end_date = response['policy_end_date']
        if 'policy_start_date' in response:
            self.policy_start_date = response['policy_start_date']
        if 'policy_status' in response:
            self.policy_status = response['policy_status']
        if 'premium' in response:
            self.premium = response['premium']
        if 'sub_order_no_list' in response:
            self.sub_order_no_list = response['sub_order_no_list']
        if 'total_premium' in response:
            self.total_premium = response['total_premium']

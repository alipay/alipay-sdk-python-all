#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcOrderLineResult import MpcOrderLineResult


class AlipayCloudCloudpromoMallOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallOrderQueryResponse, self).__init__()
        self._create_date = None
        self._logistics_status = None
        self._order_amount = None
        self._order_id = None
        self._order_line_list = None
        self._order_status = None

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_line_list(self):
        return self._order_line_list

    @order_line_list.setter
    def order_line_list(self, value):
        if isinstance(value, list):
            self._order_line_list = list()
            for i in value:
                if isinstance(i, MpcOrderLineResult):
                    self._order_line_list.append(i)
                else:
                    self._order_line_list.append(MpcOrderLineResult.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallOrderQueryResponse, self).parse_response_content(response_content)
        if 'create_date' in response:
            self.create_date = response['create_date']
        if 'logistics_status' in response:
            self.logistics_status = response['logistics_status']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_line_list' in response:
            self.order_line_list = response['order_line_list']
        if 'order_status' in response:
            self.order_status = response['order_status']

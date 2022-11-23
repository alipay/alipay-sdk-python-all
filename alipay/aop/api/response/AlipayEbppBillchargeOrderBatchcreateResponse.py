#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubOrderInfo import SubOrderInfo


class AlipayEbppBillchargeOrderBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillchargeOrderBatchcreateResponse, self).__init__()
        self._open_id = None
        self._order_no = None
        self._out_biz_id = None
        self._status = None
        self._sub_order_list = None
        self._total_pay_amount = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_order_list(self):
        return self._sub_order_list

    @sub_order_list.setter
    def sub_order_list(self, value):
        if isinstance(value, list):
            self._sub_order_list = list()
            for i in value:
                if isinstance(i, SubOrderInfo):
                    self._sub_order_list.append(i)
                else:
                    self._sub_order_list.append(SubOrderInfo.from_alipay_dict(i))
    @property
    def total_pay_amount(self):
        return self._total_pay_amount

    @total_pay_amount.setter
    def total_pay_amount(self, value):
        self._total_pay_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillchargeOrderBatchcreateResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'status' in response:
            self.status = response['status']
        if 'sub_order_list' in response:
            self.sub_order_list = response['sub_order_list']
        if 'total_pay_amount' in response:
            self.total_pay_amount = response['total_pay_amount']
        if 'user_id' in response:
            self.user_id = response['user_id']

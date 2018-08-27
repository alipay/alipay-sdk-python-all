#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderLogisticsInfo import OrderLogisticsInfo
from alipay.aop.api.domain.ServiceOrderInfo import ServiceOrderInfo


class AlipayDaoweiOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDaoweiOrderQueryResponse, self).__init__()
        self._buyer_user_id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_payment = None
        self._gmt_refund = None
        self._logistics_info = None
        self._memo = None
        self._order_no = None
        self._order_status = None
        self._payment_amount = None
        self._real_amount = None
        self._refund_amount = None
        self._service_order_list = None
        self._total_amount = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, OrderLogisticsInfo):
            self._logistics_info = value
        else:
            self._logistics_info = OrderLogisticsInfo.from_alipay_dict(value)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def service_order_list(self):
        return self._service_order_list

    @service_order_list.setter
    def service_order_list(self, value):
        if isinstance(value, list):
            self._service_order_list = list()
            for i in value:
                if isinstance(i, ServiceOrderInfo):
                    self._service_order_list.append(i)
                else:
                    self._service_order_list.append(ServiceOrderInfo.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayDaoweiOrderQueryResponse, self).parse_response_content(response_content)
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'logistics_info' in response:
            self.logistics_info = response['logistics_info']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'payment_amount' in response:
            self.payment_amount = response['payment_amount']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'service_order_list' in response:
            self.service_order_list = response['service_order_list']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']

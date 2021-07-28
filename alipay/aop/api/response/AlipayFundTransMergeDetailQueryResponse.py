#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MergePayOrder import MergePayOrder


class AlipayFundTransMergeDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransMergeDetailQueryResponse, self).__init__()
        self._amount_statistics = None
        self._fail_total_amount = None
        self._fail_total_count = None
        self._item_list = None
        self._merge_order_id = None
        self._order_title = None
        self._payer_logon_id = None
        self._payer_name = None
        self._status = None
        self._success_total_amount = None
        self._success_total_count = None
        self._total_amount = None
        self._total_count = None

    @property
    def amount_statistics(self):
        return self._amount_statistics

    @amount_statistics.setter
    def amount_statistics(self, value):
        self._amount_statistics = value
    @property
    def fail_total_amount(self):
        return self._fail_total_amount

    @fail_total_amount.setter
    def fail_total_amount(self, value):
        self._fail_total_amount = value
    @property
    def fail_total_count(self):
        return self._fail_total_count

    @fail_total_count.setter
    def fail_total_count(self, value):
        self._fail_total_count = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, MergePayOrder):
                    self._item_list.append(i)
                else:
                    self._item_list.append(MergePayOrder.from_alipay_dict(i))
    @property
    def merge_order_id(self):
        return self._merge_order_id

    @merge_order_id.setter
    def merge_order_id(self, value):
        self._merge_order_id = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def payer_logon_id(self):
        return self._payer_logon_id

    @payer_logon_id.setter
    def payer_logon_id(self, value):
        self._payer_logon_id = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def success_total_amount(self):
        return self._success_total_amount

    @success_total_amount.setter
    def success_total_amount(self, value):
        self._success_total_amount = value
    @property
    def success_total_count(self):
        return self._success_total_count

    @success_total_count.setter
    def success_total_count(self, value):
        self._success_total_count = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransMergeDetailQueryResponse, self).parse_response_content(response_content)
        if 'amount_statistics' in response:
            self.amount_statistics = response['amount_statistics']
        if 'fail_total_amount' in response:
            self.fail_total_amount = response['fail_total_amount']
        if 'fail_total_count' in response:
            self.fail_total_count = response['fail_total_count']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'merge_order_id' in response:
            self.merge_order_id = response['merge_order_id']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'payer_logon_id' in response:
            self.payer_logon_id = response['payer_logon_id']
        if 'payer_name' in response:
            self.payer_name = response['payer_name']
        if 'status' in response:
            self.status = response['status']
        if 'success_total_amount' in response:
            self.success_total_amount = response['success_total_amount']
        if 'success_total_count' in response:
            self.success_total_count = response['success_total_count']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_count' in response:
            self.total_count = response['total_count']

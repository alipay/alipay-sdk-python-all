#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryDetailAopResult import QueryDetailAopResult


class AlipayFundTransBatchQuerybatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransBatchQuerybatchResponse, self).__init__()
        self._batch_memo = None
        self._batch_no = None
        self._batch_status = None
        self._batch_type = None
        self._create_date = None
        self._create_user_id = None
        self._detail_list = None
        self._ext_param = None
        self._pay_amount_single = None
        self._pay_amount_total = None
        self._real_items_total = None
        self._show_items_total = None
        self._success_amount_total = None
        self._success_items_total = None
        self._time_out_value = None
        self._token = None

    @property
    def batch_memo(self):
        return self._batch_memo

    @batch_memo.setter
    def batch_memo(self, value):
        self._batch_memo = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def batch_type(self):
        return self._batch_type

    @batch_type.setter
    def batch_type(self, value):
        self._batch_type = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def create_user_id(self):
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, value):
        self._create_user_id = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, QueryDetailAopResult):
            self._detail_list = value
        else:
            self._detail_list = QueryDetailAopResult.from_alipay_dict(value)
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def pay_amount_single(self):
        return self._pay_amount_single

    @pay_amount_single.setter
    def pay_amount_single(self, value):
        self._pay_amount_single = value
    @property
    def pay_amount_total(self):
        return self._pay_amount_total

    @pay_amount_total.setter
    def pay_amount_total(self, value):
        self._pay_amount_total = value
    @property
    def real_items_total(self):
        return self._real_items_total

    @real_items_total.setter
    def real_items_total(self, value):
        self._real_items_total = value
    @property
    def show_items_total(self):
        return self._show_items_total

    @show_items_total.setter
    def show_items_total(self, value):
        self._show_items_total = value
    @property
    def success_amount_total(self):
        return self._success_amount_total

    @success_amount_total.setter
    def success_amount_total(self, value):
        self._success_amount_total = value
    @property
    def success_items_total(self):
        return self._success_items_total

    @success_items_total.setter
    def success_items_total(self, value):
        self._success_items_total = value
    @property
    def time_out_value(self):
        return self._time_out_value

    @time_out_value.setter
    def time_out_value(self, value):
        self._time_out_value = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransBatchQuerybatchResponse, self).parse_response_content(response_content)
        if 'batch_memo' in response:
            self.batch_memo = response['batch_memo']
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'batch_type' in response:
            self.batch_type = response['batch_type']
        if 'create_date' in response:
            self.create_date = response['create_date']
        if 'create_user_id' in response:
            self.create_user_id = response['create_user_id']
        if 'detail_list' in response:
            self.detail_list = response['detail_list']
        if 'ext_param' in response:
            self.ext_param = response['ext_param']
        if 'pay_amount_single' in response:
            self.pay_amount_single = response['pay_amount_single']
        if 'pay_amount_total' in response:
            self.pay_amount_total = response['pay_amount_total']
        if 'real_items_total' in response:
            self.real_items_total = response['real_items_total']
        if 'show_items_total' in response:
            self.show_items_total = response['show_items_total']
        if 'success_amount_total' in response:
            self.success_amount_total = response['success_amount_total']
        if 'success_items_total' in response:
            self.success_items_total = response['success_items_total']
        if 'time_out_value' in response:
            self.time_out_value = response['time_out_value']
        if 'token' in response:
            self.token = response['token']

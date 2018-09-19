#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccDetailModel import AccDetailModel


class AlipayFundBatchDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBatchDetailQueryResponse, self).__init__()
        self._acc_detail_list = None
        self._batch_no = None
        self._batch_status = None
        self._batch_trans_id = None
        self._biz_code = None
        self._biz_scene = None
        self._error_code = None
        self._fail_reason = None
        self._page_num = None
        self._page_size = None
        self._payment_amount = None
        self._payment_currency = None
        self._sign_principal = None
        self._total_item_count = None
        self._total_page_count = None

    @property
    def acc_detail_list(self):
        return self._acc_detail_list

    @acc_detail_list.setter
    def acc_detail_list(self, value):
        if isinstance(value, list):
            self._acc_detail_list = list()
            for i in value:
                if isinstance(i, AccDetailModel):
                    self._acc_detail_list.append(i)
                else:
                    self._acc_detail_list.append(AccDetailModel.from_alipay_dict(i))
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
    def batch_trans_id(self):
        return self._batch_trans_id

    @batch_trans_id.setter
    def batch_trans_id(self, value):
        self._batch_trans_id = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_currency(self):
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self._payment_currency = value
    @property
    def sign_principal(self):
        return self._sign_principal

    @sign_principal.setter
    def sign_principal(self, value):
        self._sign_principal = value
    @property
    def total_item_count(self):
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, value):
        self._total_item_count = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBatchDetailQueryResponse, self).parse_response_content(response_content)
        if 'acc_detail_list' in response:
            self.acc_detail_list = response['acc_detail_list']
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'batch_trans_id' in response:
            self.batch_trans_id = response['batch_trans_id']
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'payment_amount' in response:
            self.payment_amount = response['payment_amount']
        if 'payment_currency' in response:
            self.payment_currency = response['payment_currency']
        if 'sign_principal' in response:
            self.sign_principal = response['sign_principal']
        if 'total_item_count' in response:
            self.total_item_count = response['total_item_count']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']

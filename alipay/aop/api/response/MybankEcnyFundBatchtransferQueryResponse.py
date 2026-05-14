#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcnyBatchTransferInfo import EcnyBatchTransferInfo


class MybankEcnyFundBatchtransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyFundBatchtransferQueryResponse, self).__init__()
        self._batch_transfer_fail_reason = None
        self._gmt_success = None
        self._order_no = None
        self._out_request_from = None
        self._out_request_no = None
        self._status = None
        self._success_amount = None
        self._success_num = None
        self._total_amount = None
        self._total_num = None
        self._transfer_info_list = None

    @property
    def batch_transfer_fail_reason(self):
        return self._batch_transfer_fail_reason

    @batch_transfer_fail_reason.setter
    def batch_transfer_fail_reason(self, value):
        self._batch_transfer_fail_reason = value
    @property
    def gmt_success(self):
        return self._gmt_success

    @gmt_success.setter
    def gmt_success(self, value):
        self._gmt_success = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_request_from(self):
        return self._out_request_from

    @out_request_from.setter
    def out_request_from(self, value):
        self._out_request_from = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def success_amount(self):
        return self._success_amount

    @success_amount.setter
    def success_amount(self, value):
        self._success_amount = value
    @property
    def success_num(self):
        return self._success_num

    @success_num.setter
    def success_num(self, value):
        self._success_num = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def transfer_info_list(self):
        return self._transfer_info_list

    @transfer_info_list.setter
    def transfer_info_list(self, value):
        if isinstance(value, list):
            self._transfer_info_list = list()
            for i in value:
                if isinstance(i, EcnyBatchTransferInfo):
                    self._transfer_info_list.append(i)
                else:
                    self._transfer_info_list.append(EcnyBatchTransferInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankEcnyFundBatchtransferQueryResponse, self).parse_response_content(response_content)
        if 'batch_transfer_fail_reason' in response:
            self.batch_transfer_fail_reason = response['batch_transfer_fail_reason']
        if 'gmt_success' in response:
            self.gmt_success = response['gmt_success']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_request_from' in response:
            self.out_request_from = response['out_request_from']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
        if 'success_amount' in response:
            self.success_amount = response['success_amount']
        if 'success_num' in response:
            self.success_num = response['success_num']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'transfer_info_list' in response:
            self.transfer_info_list = response['transfer_info_list']

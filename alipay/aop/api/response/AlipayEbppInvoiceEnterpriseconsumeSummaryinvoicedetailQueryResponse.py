#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompleteVoucherInfo import CompleteVoucherInfo


class AlipayEbppInvoiceEnterpriseconsumeSummaryinvoicedetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeSummaryinvoicedetailQueryResponse, self).__init__()
        self._account_id = None
        self._apply_date = None
        self._batch_id = None
        self._batch_status = None
        self._complete_voucher_list = None
        self._gmt_biz_end = None
        self._gmt_biz_start = None
        self._status_show_content = None
        self._summary_id = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def complete_voucher_list(self):
        return self._complete_voucher_list

    @complete_voucher_list.setter
    def complete_voucher_list(self, value):
        if isinstance(value, list):
            self._complete_voucher_list = list()
            for i in value:
                if isinstance(i, CompleteVoucherInfo):
                    self._complete_voucher_list.append(i)
                else:
                    self._complete_voucher_list.append(CompleteVoucherInfo.from_alipay_dict(i))
    @property
    def gmt_biz_end(self):
        return self._gmt_biz_end

    @gmt_biz_end.setter
    def gmt_biz_end(self, value):
        self._gmt_biz_end = value
    @property
    def gmt_biz_start(self):
        return self._gmt_biz_start

    @gmt_biz_start.setter
    def gmt_biz_start(self, value):
        self._gmt_biz_start = value
    @property
    def status_show_content(self):
        return self._status_show_content

    @status_show_content.setter
    def status_show_content(self, value):
        self._status_show_content = value
    @property
    def summary_id(self):
        return self._summary_id

    @summary_id.setter
    def summary_id(self, value):
        self._summary_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeSummaryinvoicedetailQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'complete_voucher_list' in response:
            self.complete_voucher_list = response['complete_voucher_list']
        if 'gmt_biz_end' in response:
            self.gmt_biz_end = response['gmt_biz_end']
        if 'gmt_biz_start' in response:
            self.gmt_biz_start = response['gmt_biz_start']
        if 'status_show_content' in response:
            self.status_show_content = response['status_show_content']
        if 'summary_id' in response:
            self.summary_id = response['summary_id']
        if 'user_id' in response:
            self.user_id = response['user_id']

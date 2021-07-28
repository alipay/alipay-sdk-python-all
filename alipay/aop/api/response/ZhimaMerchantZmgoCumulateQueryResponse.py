#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CumulateDataDetail import CumulateDataDetail


class ZhimaMerchantZmgoCumulateQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantZmgoCumulateQueryResponse, self).__init__()
        self._aggr_amount = None
        self._aggr_discount_amount = None
        self._aggr_times = None
        self._agreement_id = None
        self._detail_list = None
        self._fail_reason = None
        self._page_no = None
        self._page_size = None

    @property
    def aggr_amount(self):
        return self._aggr_amount

    @aggr_amount.setter
    def aggr_amount(self, value):
        self._aggr_amount = value
    @property
    def aggr_discount_amount(self):
        return self._aggr_discount_amount

    @aggr_discount_amount.setter
    def aggr_discount_amount(self, value):
        self._aggr_discount_amount = value
    @property
    def aggr_times(self):
        return self._aggr_times

    @aggr_times.setter
    def aggr_times(self, value):
        self._aggr_times = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, CumulateDataDetail):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(CumulateDataDetail.from_alipay_dict(i))
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantZmgoCumulateQueryResponse, self).parse_response_content(response_content)
        if 'aggr_amount' in response:
            self.aggr_amount = response['aggr_amount']
        if 'aggr_discount_amount' in response:
            self.aggr_discount_amount = response['aggr_discount_amount']
        if 'aggr_times' in response:
            self.aggr_times = response['aggr_times']
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'detail_list' in response:
            self.detail_list = response['detail_list']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']

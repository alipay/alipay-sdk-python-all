#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserVoucherInfo import UserVoucherInfo


class AlipayMarketingActivityUserBatchqueryvoucherResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityUserBatchqueryvoucherResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_size = None
        self._user_voucher_infos = None

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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def user_voucher_infos(self):
        return self._user_voucher_infos

    @user_voucher_infos.setter
    def user_voucher_infos(self, value):
        if isinstance(value, list):
            self._user_voucher_infos = list()
            for i in value:
                if isinstance(i, UserVoucherInfo):
                    self._user_voucher_infos.append(i)
                else:
                    self._user_voucher_infos.append(UserVoucherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityUserBatchqueryvoucherResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'user_voucher_infos' in response:
            self.user_voucher_infos = response['user_voucher_infos']

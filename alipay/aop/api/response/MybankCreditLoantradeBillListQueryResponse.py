#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillDetailVo import BillDetailVo
from alipay.aop.api.domain.RefuseVo import RefuseVo


class MybankCreditLoantradeBillListQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeBillListQueryResponse, self).__init__()
        self._bill_detail_list = None
        self._has_next_page = None
        self._page_num = None
        self._page_size = None
        self._refuse_msg = None
        self._success = None

    @property
    def bill_detail_list(self):
        return self._bill_detail_list

    @bill_detail_list.setter
    def bill_detail_list(self, value):
        if isinstance(value, BillDetailVo):
            self._bill_detail_list = value
        else:
            self._bill_detail_list = BillDetailVo.from_alipay_dict(value)
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
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
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, RefuseVo):
            self._refuse_msg = value
        else:
            self._refuse_msg = RefuseVo.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeBillListQueryResponse, self).parse_response_content(response_content)
        if 'bill_detail_list' in response:
            self.bill_detail_list = response['bill_detail_list']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'success' in response:
            self.success = response['success']

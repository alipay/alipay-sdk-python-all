#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupScheduleMsgVO import GroupScheduleMsgVO


class AlipayMerchantGroupSchedulemsgBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupSchedulemsgBatchqueryResponse, self).__init__()
        self._msg_record_list = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def msg_record_list(self):
        return self._msg_record_list

    @msg_record_list.setter
    def msg_record_list(self, value):
        if isinstance(value, list):
            self._msg_record_list = list()
            for i in value:
                if isinstance(i, GroupScheduleMsgVO):
                    self._msg_record_list.append(i)
                else:
                    self._msg_record_list.append(GroupScheduleMsgVO.from_alipay_dict(i))
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupSchedulemsgBatchqueryResponse, self).parse_response_content(response_content)
        if 'msg_record_list' in response:
            self.msg_record_list = response['msg_record_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']

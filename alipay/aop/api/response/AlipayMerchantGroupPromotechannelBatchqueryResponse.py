#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupPromoteChannelVO import GroupPromoteChannelVO


class AlipayMerchantGroupPromotechannelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupPromotechannelBatchqueryResponse, self).__init__()
        self._group_promote_channel_list = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def group_promote_channel_list(self):
        return self._group_promote_channel_list

    @group_promote_channel_list.setter
    def group_promote_channel_list(self, value):
        if isinstance(value, GroupPromoteChannelVO):
            self._group_promote_channel_list = value
        else:
            self._group_promote_channel_list = GroupPromoteChannelVO.from_alipay_dict(value)
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
        response = super(AlipayMerchantGroupPromotechannelBatchqueryResponse, self).parse_response_content(response_content)
        if 'group_promote_channel_list' in response:
            self.group_promote_channel_list = response['group_promote_channel_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']

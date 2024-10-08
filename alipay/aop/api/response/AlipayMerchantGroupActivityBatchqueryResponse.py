#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupActivityRecordVO import GroupActivityRecordVO


class AlipayMerchantGroupActivityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupActivityBatchqueryResponse, self).__init__()
        self._activity_record_list = None
        self._total_count = None

    @property
    def activity_record_list(self):
        return self._activity_record_list

    @activity_record_list.setter
    def activity_record_list(self, value):
        if isinstance(value, list):
            self._activity_record_list = list()
            for i in value:
                if isinstance(i, GroupActivityRecordVO):
                    self._activity_record_list.append(i)
                else:
                    self._activity_record_list.append(GroupActivityRecordVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupActivityBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_record_list' in response:
            self.activity_record_list = response['activity_record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']

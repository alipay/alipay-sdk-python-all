#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupRecord import GroupRecord


class AlipayOpenDataServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDataServiceQueryResponse, self).__init__()
        self._group_records = None
        self._success = None

    @property
    def group_records(self):
        return self._group_records

    @group_records.setter
    def group_records(self, value):
        if isinstance(value, list):
            self._group_records = list()
            for i in value:
                if isinstance(i, GroupRecord):
                    self._group_records.append(i)
                else:
                    self._group_records.append(GroupRecord.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDataServiceQueryResponse, self).parse_response_content(response_content)
        if 'group_records' in response:
            self.group_records = response['group_records']
        if 'success' in response:
            self.success = response['success']

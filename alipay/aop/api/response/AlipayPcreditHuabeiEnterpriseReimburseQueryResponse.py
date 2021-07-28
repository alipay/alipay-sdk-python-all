#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecordDetail import RecordDetail


class AlipayPcreditHuabeiEnterpriseReimburseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiEnterpriseReimburseQueryResponse, self).__init__()
        self._record_detail_list = None

    @property
    def record_detail_list(self):
        return self._record_detail_list

    @record_detail_list.setter
    def record_detail_list(self, value):
        if isinstance(value, list):
            self._record_detail_list = list()
            for i in value:
                if isinstance(i, RecordDetail):
                    self._record_detail_list.append(i)
                else:
                    self._record_detail_list.append(RecordDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiEnterpriseReimburseQueryResponse, self).parse_response_content(response_content)
        if 'record_detail_list' in response:
            self.record_detail_list = response['record_detail_list']

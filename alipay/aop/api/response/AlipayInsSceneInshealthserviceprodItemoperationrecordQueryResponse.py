#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalItemOperationRecordQueryDTO import ExternalItemOperationRecordQueryDTO


class AlipayInsSceneInshealthserviceprodItemoperationrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodItemoperationrecordQueryResponse, self).__init__()
        self._record_list = None
        self._total_count = None

    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, ExternalItemOperationRecordQueryDTO):
                    self._record_list.append(i)
                else:
                    self._record_list.append(ExternalItemOperationRecordQueryDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodItemoperationrecordQueryResponse, self).parse_response_content(response_content)
        if 'record_list' in response:
            self.record_list = response['record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']

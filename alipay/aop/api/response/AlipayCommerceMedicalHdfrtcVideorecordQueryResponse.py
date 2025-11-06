#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecordInfo import RecordInfo


class AlipayCommerceMedicalHdfrtcVideorecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideorecordQueryResponse, self).__init__()
        self._record_watch_notice = None
        self._records_info = None

    @property
    def record_watch_notice(self):
        return self._record_watch_notice

    @record_watch_notice.setter
    def record_watch_notice(self, value):
        self._record_watch_notice = value
    @property
    def records_info(self):
        return self._records_info

    @records_info.setter
    def records_info(self, value):
        if isinstance(value, list):
            self._records_info = list()
            for i in value:
                if isinstance(i, RecordInfo):
                    self._records_info.append(i)
                else:
                    self._records_info.append(RecordInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideorecordQueryResponse, self).parse_response_content(response_content)
        if 'record_watch_notice' in response:
            self.record_watch_notice = response['record_watch_notice']
        if 'records_info' in response:
            self.records_info = response['records_info']

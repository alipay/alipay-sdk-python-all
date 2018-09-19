#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LawsuitRecord import LawsuitRecord


class ZhimaCreditEpLawsuitRecordGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpLawsuitRecordGetResponse, self).__init__()
        self._biz_no = None
        self._lawsuit_record = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def lawsuit_record(self):
        return self._lawsuit_record

    @lawsuit_record.setter
    def lawsuit_record(self, value):
        if isinstance(value, LawsuitRecord):
            self._lawsuit_record = value
        else:
            self._lawsuit_record = LawsuitRecord.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpLawsuitRecordGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'lawsuit_record' in response:
            self.lawsuit_record = response['lawsuit_record']

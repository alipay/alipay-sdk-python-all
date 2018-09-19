#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LawsuitPersonRecord import LawsuitPersonRecord


class ZhimaCreditPeLawsuitRecordGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeLawsuitRecordGetResponse, self).__init__()
        self._biz_no = None
        self._lawsuit_person_record = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def lawsuit_person_record(self):
        return self._lawsuit_person_record

    @lawsuit_person_record.setter
    def lawsuit_person_record(self, value):
        if isinstance(value, LawsuitPersonRecord):
            self._lawsuit_person_record = value
        else:
            self._lawsuit_person_record = LawsuitPersonRecord.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeLawsuitRecordGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'lawsuit_person_record' in response:
            self.lawsuit_person_record = response['lawsuit_person_record']

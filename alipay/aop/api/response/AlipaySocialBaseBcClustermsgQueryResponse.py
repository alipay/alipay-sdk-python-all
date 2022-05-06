#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BcClusterMsgRecord import BcClusterMsgRecord


class AlipaySocialBaseBcClustermsgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcClustermsgQueryResponse, self).__init__()
        self._msg_records = None

    @property
    def msg_records(self):
        return self._msg_records

    @msg_records.setter
    def msg_records(self, value):
        if isinstance(value, list):
            self._msg_records = list()
            for i in value:
                if isinstance(i, BcClusterMsgRecord):
                    self._msg_records.append(i)
                else:
                    self._msg_records.append(BcClusterMsgRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcClustermsgQueryResponse, self).parse_response_content(response_content)
        if 'msg_records' in response:
            self.msg_records = response['msg_records']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AttachmentDetail import AttachmentDetail
from alipay.aop.api.domain.DocInfo import DocInfo


class AlipayEcoSignflowsDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoSignflowsDetailQueryResponse, self).__init__()
        self._attachments = None
        self._docs = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, AttachmentDetail):
            self._attachments = value
        else:
            self._attachments = AttachmentDetail.from_alipay_dict(value)
    @property
    def docs(self):
        return self._docs

    @docs.setter
    def docs(self, value):
        if isinstance(value, DocInfo):
            self._docs = value
        else:
            self._docs = DocInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEcoSignflowsDetailQueryResponse, self).parse_response_content(response_content)
        if 'attachments' in response:
            self.attachments = response['attachments']
        if 'docs' in response:
            self.docs = response['docs']

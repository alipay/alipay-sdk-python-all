#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HitSegmentDetail import HitSegmentDetail


class AlipayCloudCloudpromoKnowledgeRagGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoKnowledgeRagGenerateResponse, self).__init__()
        self._hits = None

    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        if isinstance(value, list):
            self._hits = list()
            for i in value:
                if isinstance(i, HitSegmentDetail):
                    self._hits.append(i)
                else:
                    self._hits.append(HitSegmentDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoKnowledgeRagGenerateResponse, self).parse_response_content(response_content)
        if 'hits' in response:
            self.hits = response['hits']

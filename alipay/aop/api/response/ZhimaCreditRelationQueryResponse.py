#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RelationInfo import RelationInfo


class ZhimaCreditRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditRelationQueryResponse, self).__init__()
        self._biz_no = None
        self._relation_info = None
        self._relation_rank = None
        self._relation_score = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def relation_info(self):
        return self._relation_info

    @relation_info.setter
    def relation_info(self, value):
        if isinstance(value, RelationInfo):
            self._relation_info = value
        else:
            self._relation_info = RelationInfo.from_alipay_dict(value)
    @property
    def relation_rank(self):
        return self._relation_rank

    @relation_rank.setter
    def relation_rank(self, value):
        self._relation_rank = value
    @property
    def relation_score(self):
        return self._relation_score

    @relation_score.setter
    def relation_score(self, value):
        self._relation_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditRelationQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'relation_info' in response:
            self.relation_info = response['relation_info']
        if 'relation_rank' in response:
            self.relation_rank = response['relation_rank']
        if 'relation_score' in response:
            self.relation_score = response['relation_score']

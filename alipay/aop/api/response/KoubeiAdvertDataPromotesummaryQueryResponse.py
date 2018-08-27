#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel


class KoubeiAdvertDataPromotesummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDataPromotesummaryQueryResponse, self).__init__()
        self._kb_platform_promote_data = None
        self._others_promote_data = None
        self._part_promote_data = None
        self._self_promote_data = None
        self._total_promote_data = None

    @property
    def kb_platform_promote_data(self):
        return self._kb_platform_promote_data

    @kb_platform_promote_data.setter
    def kb_platform_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._kb_platform_promote_data = value
        else:
            self._kb_platform_promote_data = PromoteDataModel.from_alipay_dict(value)
    @property
    def others_promote_data(self):
        return self._others_promote_data

    @others_promote_data.setter
    def others_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._others_promote_data = value
        else:
            self._others_promote_data = PromoteDataModel.from_alipay_dict(value)
    @property
    def part_promote_data(self):
        return self._part_promote_data

    @part_promote_data.setter
    def part_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._part_promote_data = value
        else:
            self._part_promote_data = PromoteDataModel.from_alipay_dict(value)
    @property
    def self_promote_data(self):
        return self._self_promote_data

    @self_promote_data.setter
    def self_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._self_promote_data = value
        else:
            self._self_promote_data = PromoteDataModel.from_alipay_dict(value)
    @property
    def total_promote_data(self):
        return self._total_promote_data

    @total_promote_data.setter
    def total_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._total_promote_data = value
        else:
            self._total_promote_data = PromoteDataModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDataPromotesummaryQueryResponse, self).parse_response_content(response_content)
        if 'kb_platform_promote_data' in response:
            self.kb_platform_promote_data = response['kb_platform_promote_data']
        if 'others_promote_data' in response:
            self.others_promote_data = response['others_promote_data']
        if 'part_promote_data' in response:
            self.part_promote_data = response['part_promote_data']
        if 'self_promote_data' in response:
            self.self_promote_data = response['self_promote_data']
        if 'total_promote_data' in response:
            self.total_promote_data = response['total_promote_data']

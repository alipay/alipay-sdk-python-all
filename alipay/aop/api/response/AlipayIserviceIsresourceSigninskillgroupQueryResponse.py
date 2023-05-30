#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiSkillGroupInfo import OpenApiSkillGroupInfo


class AlipayIserviceIsresourceSigninskillgroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceSigninskillgroupQueryResponse, self).__init__()
        self._biz_data = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, list):
            self._biz_data = list()
            for i in value:
                if isinstance(i, OpenApiSkillGroupInfo):
                    self._biz_data.append(i)
                else:
                    self._biz_data.append(OpenApiSkillGroupInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceSigninskillgroupQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']

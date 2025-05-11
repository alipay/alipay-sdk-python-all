#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampusPointDetail import CampusPointDetail


class AlipayCommerceEducateCampusPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusPointQueryResponse, self).__init__()
        self._campus_point_detail_list = None

    @property
    def campus_point_detail_list(self):
        return self._campus_point_detail_list

    @campus_point_detail_list.setter
    def campus_point_detail_list(self, value):
        if isinstance(value, list):
            self._campus_point_detail_list = list()
            for i in value:
                if isinstance(i, CampusPointDetail):
                    self._campus_point_detail_list.append(i)
                else:
                    self._campus_point_detail_list.append(CampusPointDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusPointQueryResponse, self).parse_response_content(response_content)
        if 'campus_point_detail_list' in response:
            self.campus_point_detail_list = response['campus_point_detail_list']

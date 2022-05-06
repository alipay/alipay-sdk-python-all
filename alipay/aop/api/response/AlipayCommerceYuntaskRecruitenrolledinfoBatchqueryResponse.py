#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskRecruitEnrolledInfo import YunTaskRecruitEnrolledInfo


class AlipayCommerceYuntaskRecruitenrolledinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskRecruitenrolledinfoBatchqueryResponse, self).__init__()
        self._enrolled_infos = None

    @property
    def enrolled_infos(self):
        return self._enrolled_infos

    @enrolled_infos.setter
    def enrolled_infos(self, value):
        if isinstance(value, list):
            self._enrolled_infos = list()
            for i in value:
                if isinstance(i, YunTaskRecruitEnrolledInfo):
                    self._enrolled_infos.append(i)
                else:
                    self._enrolled_infos.append(YunTaskRecruitEnrolledInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskRecruitenrolledinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'enrolled_infos' in response:
            self.enrolled_infos = response['enrolled_infos']

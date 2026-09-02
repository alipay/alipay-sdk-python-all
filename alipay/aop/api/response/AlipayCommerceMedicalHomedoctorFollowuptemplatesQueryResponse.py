#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateInfoResponse import TemplateInfoResponse


class AlipayCommerceMedicalHomedoctorFollowuptemplatesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorFollowuptemplatesQueryResponse, self).__init__()
        self._template_list = None

    @property
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, TemplateInfoResponse):
                    self._template_list.append(i)
                else:
                    self._template_list.append(TemplateInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorFollowuptemplatesQueryResponse, self).parse_response_content(response_content)
        if 'template_list' in response:
            self.template_list = response['template_list']

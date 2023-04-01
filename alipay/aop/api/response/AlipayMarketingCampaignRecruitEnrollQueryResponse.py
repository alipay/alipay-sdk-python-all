#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitEnrollBaseInfo import RecruitEnrollBaseInfo
from alipay.aop.api.domain.RecruitEnrollContent import RecruitEnrollContent
from alipay.aop.api.domain.RecruitEnrollMaterial import RecruitEnrollMaterial
from alipay.aop.api.domain.RecruitServingTarget import RecruitServingTarget


class AlipayMarketingCampaignRecruitEnrollQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRecruitEnrollQueryResponse, self).__init__()
        self._enroll_base_info = None
        self._enroll_content = None
        self._enroll_material = None
        self._out_biz_no = None
        self._serving_target = None

    @property
    def enroll_base_info(self):
        return self._enroll_base_info

    @enroll_base_info.setter
    def enroll_base_info(self, value):
        if isinstance(value, RecruitEnrollBaseInfo):
            self._enroll_base_info = value
        else:
            self._enroll_base_info = RecruitEnrollBaseInfo.from_alipay_dict(value)
    @property
    def enroll_content(self):
        return self._enroll_content

    @enroll_content.setter
    def enroll_content(self, value):
        if isinstance(value, RecruitEnrollContent):
            self._enroll_content = value
        else:
            self._enroll_content = RecruitEnrollContent.from_alipay_dict(value)
    @property
    def enroll_material(self):
        return self._enroll_material

    @enroll_material.setter
    def enroll_material(self, value):
        if isinstance(value, RecruitEnrollMaterial):
            self._enroll_material = value
        else:
            self._enroll_material = RecruitEnrollMaterial.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def serving_target(self):
        return self._serving_target

    @serving_target.setter
    def serving_target(self, value):
        if isinstance(value, RecruitServingTarget):
            self._serving_target = value
        else:
            self._serving_target = RecruitServingTarget.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRecruitEnrollQueryResponse, self).parse_response_content(response_content)
        if 'enroll_base_info' in response:
            self.enroll_base_info = response['enroll_base_info']
        if 'enroll_content' in response:
            self.enroll_content = response['enroll_content']
        if 'enroll_material' in response:
            self.enroll_material = response['enroll_material']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'serving_target' in response:
            self.serving_target = response['serving_target']

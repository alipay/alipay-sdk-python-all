#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollBaseInfo import RecruitEnrollBaseInfo
from alipay.aop.api.domain.RecruitEnrollContent import RecruitEnrollContent
from alipay.aop.api.domain.RecruitEnrollMaterial import RecruitEnrollMaterial
from alipay.aop.api.domain.RecruitServingTarget import RecruitServingTarget


class AlipayMarketingCampaignRecruitEnrollCreateModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_base_info:
            if hasattr(self.enroll_base_info, 'to_alipay_dict'):
                params['enroll_base_info'] = self.enroll_base_info.to_alipay_dict()
            else:
                params['enroll_base_info'] = self.enroll_base_info
        if self.enroll_content:
            if hasattr(self.enroll_content, 'to_alipay_dict'):
                params['enroll_content'] = self.enroll_content.to_alipay_dict()
            else:
                params['enroll_content'] = self.enroll_content
        if self.enroll_material:
            if hasattr(self.enroll_material, 'to_alipay_dict'):
                params['enroll_material'] = self.enroll_material.to_alipay_dict()
            else:
                params['enroll_material'] = self.enroll_material
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.serving_target:
            if hasattr(self.serving_target, 'to_alipay_dict'):
                params['serving_target'] = self.serving_target.to_alipay_dict()
            else:
                params['serving_target'] = self.serving_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignRecruitEnrollCreateModel()
        if 'enroll_base_info' in d:
            o.enroll_base_info = d['enroll_base_info']
        if 'enroll_content' in d:
            o.enroll_content = d['enroll_content']
        if 'enroll_material' in d:
            o.enroll_material = d['enroll_material']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'serving_target' in d:
            o.serving_target = d['serving_target']
        return o



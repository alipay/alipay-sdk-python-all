#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTransferInstitutionpaymentQueryModel(object):

    def __init__(self):
        self._biz_scene_type = None
        self._institution_keyword = None
        self._institution_region = None
        self._pass_through_info = None

    @property
    def biz_scene_type(self):
        return self._biz_scene_type

    @biz_scene_type.setter
    def biz_scene_type(self, value):
        self._biz_scene_type = value
    @property
    def institution_keyword(self):
        return self._institution_keyword

    @institution_keyword.setter
    def institution_keyword(self, value):
        self._institution_keyword = value
    @property
    def institution_region(self):
        return self._institution_region

    @institution_region.setter
    def institution_region(self, value):
        self._institution_region = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene_type:
            if hasattr(self.biz_scene_type, 'to_alipay_dict'):
                params['biz_scene_type'] = self.biz_scene_type.to_alipay_dict()
            else:
                params['biz_scene_type'] = self.biz_scene_type
        if self.institution_keyword:
            if hasattr(self.institution_keyword, 'to_alipay_dict'):
                params['institution_keyword'] = self.institution_keyword.to_alipay_dict()
            else:
                params['institution_keyword'] = self.institution_keyword
        if self.institution_region:
            if hasattr(self.institution_region, 'to_alipay_dict'):
                params['institution_region'] = self.institution_region.to_alipay_dict()
            else:
                params['institution_region'] = self.institution_region
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTransferInstitutionpaymentQueryModel()
        if 'biz_scene_type' in d:
            o.biz_scene_type = d['biz_scene_type']
        if 'institution_keyword' in d:
            o.institution_keyword = d['institution_keyword']
        if 'institution_region' in d:
            o.institution_region = d['institution_region']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        return o



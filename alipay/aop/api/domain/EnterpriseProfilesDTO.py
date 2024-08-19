#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseProfilesDTO(object):

    def __init__(self):
        self._create_iot_group = None
        self._credit_applicant_mobile = None
        self._fund_biz_scene = None
        self._group_app_id = None

    @property
    def create_iot_group(self):
        return self._create_iot_group

    @create_iot_group.setter
    def create_iot_group(self, value):
        self._create_iot_group = value
    @property
    def credit_applicant_mobile(self):
        return self._credit_applicant_mobile

    @credit_applicant_mobile.setter
    def credit_applicant_mobile(self, value):
        self._credit_applicant_mobile = value
    @property
    def fund_biz_scene(self):
        return self._fund_biz_scene

    @fund_biz_scene.setter
    def fund_biz_scene(self, value):
        self._fund_biz_scene = value
    @property
    def group_app_id(self):
        return self._group_app_id

    @group_app_id.setter
    def group_app_id(self, value):
        self._group_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_iot_group:
            if hasattr(self.create_iot_group, 'to_alipay_dict'):
                params['create_iot_group'] = self.create_iot_group.to_alipay_dict()
            else:
                params['create_iot_group'] = self.create_iot_group
        if self.credit_applicant_mobile:
            if hasattr(self.credit_applicant_mobile, 'to_alipay_dict'):
                params['credit_applicant_mobile'] = self.credit_applicant_mobile.to_alipay_dict()
            else:
                params['credit_applicant_mobile'] = self.credit_applicant_mobile
        if self.fund_biz_scene:
            if hasattr(self.fund_biz_scene, 'to_alipay_dict'):
                params['fund_biz_scene'] = self.fund_biz_scene.to_alipay_dict()
            else:
                params['fund_biz_scene'] = self.fund_biz_scene
        if self.group_app_id:
            if hasattr(self.group_app_id, 'to_alipay_dict'):
                params['group_app_id'] = self.group_app_id.to_alipay_dict()
            else:
                params['group_app_id'] = self.group_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseProfilesDTO()
        if 'create_iot_group' in d:
            o.create_iot_group = d['create_iot_group']
        if 'credit_applicant_mobile' in d:
            o.credit_applicant_mobile = d['credit_applicant_mobile']
        if 'fund_biz_scene' in d:
            o.fund_biz_scene = d['fund_biz_scene']
        if 'group_app_id' in d:
            o.group_app_id = d['group_app_id']
        return o



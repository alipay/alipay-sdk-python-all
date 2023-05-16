#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsCompany import InsCompany
from alipay.aop.api.domain.InsPartnerOrganization import InsPartnerOrganization


class AlipayInsSceneEmploymentGrouporderCreateModel(object):

    def __init__(self):
        self._effect_start_time = None
        self._merchant = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._partner_organization = None
        self._period = None
        self._recom_flow_no = None
        self._scene_code = None

    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsCompany):
            self._merchant = value
        else:
            self._merchant = InsCompany.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def partner_organization(self):
        return self._partner_organization

    @partner_organization.setter
    def partner_organization(self, value):
        if isinstance(value, InsPartnerOrganization):
            self._partner_organization = value
        else:
            self._partner_organization = InsPartnerOrganization.from_alipay_dict(value)
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def recom_flow_no(self):
        return self._recom_flow_no

    @recom_flow_no.setter
    def recom_flow_no(self, value):
        self._recom_flow_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.partner_organization:
            if hasattr(self.partner_organization, 'to_alipay_dict'):
                params['partner_organization'] = self.partner_organization.to_alipay_dict()
            else:
                params['partner_organization'] = self.partner_organization
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.recom_flow_no:
            if hasattr(self.recom_flow_no, 'to_alipay_dict'):
                params['recom_flow_no'] = self.recom_flow_no.to_alipay_dict()
            else:
                params['recom_flow_no'] = self.recom_flow_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEmploymentGrouporderCreateModel()
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'partner_organization' in d:
            o.partner_organization = d['partner_organization']
        if 'period' in d:
            o.period = d['period']
        if 'recom_flow_no' in d:
            o.recom_flow_no = d['recom_flow_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o



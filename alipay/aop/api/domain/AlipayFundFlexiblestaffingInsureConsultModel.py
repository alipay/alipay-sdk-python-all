#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsureCompany import InsureCompany
from alipay.aop.api.domain.InsurePartnerOrganization import InsurePartnerOrganization


class AlipayFundFlexiblestaffingInsureConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._channel = None
        self._merchant = None
        self._partner_organization = None
        self._product_code = None
        self._scene_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsureCompany):
            self._merchant = value
        else:
            self._merchant = InsureCompany.from_alipay_dict(value)
    @property
    def partner_organization(self):
        return self._partner_organization

    @partner_organization.setter
    def partner_organization(self, value):
        if isinstance(value, InsurePartnerOrganization):
            self._partner_organization = value
        else:
            self._partner_organization = InsurePartnerOrganization.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.partner_organization:
            if hasattr(self.partner_organization, 'to_alipay_dict'):
                params['partner_organization'] = self.partner_organization.to_alipay_dict()
            else:
                params['partner_organization'] = self.partner_organization
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = AlipayFundFlexiblestaffingInsureConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'partner_organization' in d:
            o.partner_organization = d['partner_organization']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o



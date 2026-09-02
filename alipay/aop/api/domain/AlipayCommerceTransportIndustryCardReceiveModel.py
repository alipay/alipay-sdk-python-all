#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIndustryCardReceiveModel(object):

    def __init__(self):
        self._card_template_code = None
        self._industry_scene = None
        self._mobile = None
        self._open_id = None
        self._open_type = None
        self._out_biz_no = None
        self._partner_code = None
        self._user_id = None

    @property
    def card_template_code(self):
        return self._card_template_code

    @card_template_code.setter
    def card_template_code(self, value):
        self._card_template_code = value
    @property
    def industry_scene(self):
        return self._industry_scene

    @industry_scene.setter
    def industry_scene(self, value):
        self._industry_scene = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_code(self):
        return self._partner_code

    @partner_code.setter
    def partner_code(self, value):
        self._partner_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_code:
            if hasattr(self.card_template_code, 'to_alipay_dict'):
                params['card_template_code'] = self.card_template_code.to_alipay_dict()
            else:
                params['card_template_code'] = self.card_template_code
        if self.industry_scene:
            if hasattr(self.industry_scene, 'to_alipay_dict'):
                params['industry_scene'] = self.industry_scene.to_alipay_dict()
            else:
                params['industry_scene'] = self.industry_scene
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_code:
            if hasattr(self.partner_code, 'to_alipay_dict'):
                params['partner_code'] = self.partner_code.to_alipay_dict()
            else:
                params['partner_code'] = self.partner_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIndustryCardReceiveModel()
        if 'card_template_code' in d:
            o.card_template_code = d['card_template_code']
        if 'industry_scene' in d:
            o.industry_scene = d['industry_scene']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_type' in d:
            o.open_type = d['open_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_code' in d:
            o.partner_code = d['partner_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



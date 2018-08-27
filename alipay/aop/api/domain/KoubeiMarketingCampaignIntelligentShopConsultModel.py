#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo


class KoubeiMarketingCampaignIntelligentShopConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._operator_context = None
        self._out_request_no = None
        self._page_index = None
        self._page_size = None
        self._partner_id = None
        self._plan_id = None
        self._promo_id = None
        self._template_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def operator_context(self):
        return self._operator_context

    @operator_context.setter
    def operator_context(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._operator_context = value
        else:
            self._operator_context = PromoOperatorInfo.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.operator_context:
            if hasattr(self.operator_context, 'to_alipay_dict'):
                params['operator_context'] = self.operator_context.to_alipay_dict()
            else:
                params['operator_context'] = self.operator_context
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignIntelligentShopConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'operator_context' in d:
            o.operator_context = d['operator_context']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o



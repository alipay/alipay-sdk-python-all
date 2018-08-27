#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo


class KoubeiMarketingCampaignIntelligentTemplateConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._operator_context = None
        self._out_request_no = None
        self._partner_id = None
        self._promo_id = None
        self._shop_ids = None

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
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)


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
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignIntelligentTemplateConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'operator_context' in d:
            o.operator_context = d['operator_context']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        return o



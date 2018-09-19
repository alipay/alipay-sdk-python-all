#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignOpenDeliveryCreateModel(object):

    def __init__(self):
        self._delivery_content = None
        self._delivery_type = None
        self._partner_id = None
        self._shop_id = None

    @property
    def delivery_content(self):
        return self._delivery_content

    @delivery_content.setter
    def delivery_content(self, value):
        self._delivery_content = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_content:
            if hasattr(self.delivery_content, 'to_alipay_dict'):
                params['delivery_content'] = self.delivery_content.to_alipay_dict()
            else:
                params['delivery_content'] = self.delivery_content
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignOpenDeliveryCreateModel()
        if 'delivery_content' in d:
            o.delivery_content = d['delivery_content']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o



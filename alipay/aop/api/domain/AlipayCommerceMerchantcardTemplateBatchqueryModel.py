#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTemplateBatchqueryModel(object):

    def __init__(self):
        self._card_template_appid = None
        self._card_template_name = None
        self._page_num = None
        self._page_size = None
        self._shop_id = None

    @property
    def card_template_appid(self):
        return self._card_template_appid

    @card_template_appid.setter
    def card_template_appid(self, value):
        self._card_template_appid = value
    @property
    def card_template_name(self):
        return self._card_template_name

    @card_template_name.setter
    def card_template_name(self, value):
        self._card_template_name = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_appid:
            if hasattr(self.card_template_appid, 'to_alipay_dict'):
                params['card_template_appid'] = self.card_template_appid.to_alipay_dict()
            else:
                params['card_template_appid'] = self.card_template_appid
        if self.card_template_name:
            if hasattr(self.card_template_name, 'to_alipay_dict'):
                params['card_template_name'] = self.card_template_name.to_alipay_dict()
            else:
                params['card_template_name'] = self.card_template_name
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayCommerceMerchantcardTemplateBatchqueryModel()
        if 'card_template_appid' in d:
            o.card_template_appid = d['card_template_appid']
        if 'card_template_name' in d:
            o.card_template_name = d['card_template_name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o



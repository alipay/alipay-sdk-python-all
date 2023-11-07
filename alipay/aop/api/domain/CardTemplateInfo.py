#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardTemplateSaleInfo import CardTemplateSaleInfo
from alipay.aop.api.domain.CardTemplateUseInfo import CardTemplateUseInfo


class CardTemplateInfo(object):

    def __init__(self):
        self._card_template_id = None
        self._card_template_name = None
        self._card_template_status = None
        self._category_id = None
        self._image_id_list = None
        self._image_url_list = None
        self._industry_solution_type = None
        self._out_card_id = None
        self._owner = None
        self._sale_info = None
        self._use_info = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_template_name(self):
        return self._card_template_name

    @card_template_name.setter
    def card_template_name(self, value):
        self._card_template_name = value
    @property
    def card_template_status(self):
        return self._card_template_status

    @card_template_status.setter
    def card_template_status(self, value):
        self._card_template_status = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def image_id_list(self):
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, value):
        if isinstance(value, list):
            self._image_id_list = list()
            for i in value:
                self._image_id_list.append(i)
    @property
    def image_url_list(self):
        return self._image_url_list

    @image_url_list.setter
    def image_url_list(self, value):
        if isinstance(value, list):
            self._image_url_list = list()
            for i in value:
                self._image_url_list.append(i)
    @property
    def industry_solution_type(self):
        return self._industry_solution_type

    @industry_solution_type.setter
    def industry_solution_type(self, value):
        self._industry_solution_type = value
    @property
    def out_card_id(self):
        return self._out_card_id

    @out_card_id.setter
    def out_card_id(self, value):
        self._out_card_id = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def sale_info(self):
        return self._sale_info

    @sale_info.setter
    def sale_info(self, value):
        if isinstance(value, CardTemplateSaleInfo):
            self._sale_info = value
        else:
            self._sale_info = CardTemplateSaleInfo.from_alipay_dict(value)
    @property
    def use_info(self):
        return self._use_info

    @use_info.setter
    def use_info(self, value):
        if isinstance(value, CardTemplateUseInfo):
            self._use_info = value
        else:
            self._use_info = CardTemplateUseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_template_name:
            if hasattr(self.card_template_name, 'to_alipay_dict'):
                params['card_template_name'] = self.card_template_name.to_alipay_dict()
            else:
                params['card_template_name'] = self.card_template_name
        if self.card_template_status:
            if hasattr(self.card_template_status, 'to_alipay_dict'):
                params['card_template_status'] = self.card_template_status.to_alipay_dict()
            else:
                params['card_template_status'] = self.card_template_status
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.image_id_list:
            if isinstance(self.image_id_list, list):
                for i in range(0, len(self.image_id_list)):
                    element = self.image_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_id_list, 'to_alipay_dict'):
                params['image_id_list'] = self.image_id_list.to_alipay_dict()
            else:
                params['image_id_list'] = self.image_id_list
        if self.image_url_list:
            if isinstance(self.image_url_list, list):
                for i in range(0, len(self.image_url_list)):
                    element = self.image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.image_url_list, 'to_alipay_dict'):
                params['image_url_list'] = self.image_url_list.to_alipay_dict()
            else:
                params['image_url_list'] = self.image_url_list
        if self.industry_solution_type:
            if hasattr(self.industry_solution_type, 'to_alipay_dict'):
                params['industry_solution_type'] = self.industry_solution_type.to_alipay_dict()
            else:
                params['industry_solution_type'] = self.industry_solution_type
        if self.out_card_id:
            if hasattr(self.out_card_id, 'to_alipay_dict'):
                params['out_card_id'] = self.out_card_id.to_alipay_dict()
            else:
                params['out_card_id'] = self.out_card_id
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.sale_info:
            if hasattr(self.sale_info, 'to_alipay_dict'):
                params['sale_info'] = self.sale_info.to_alipay_dict()
            else:
                params['sale_info'] = self.sale_info
        if self.use_info:
            if hasattr(self.use_info, 'to_alipay_dict'):
                params['use_info'] = self.use_info.to_alipay_dict()
            else:
                params['use_info'] = self.use_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardTemplateInfo()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_template_name' in d:
            o.card_template_name = d['card_template_name']
        if 'card_template_status' in d:
            o.card_template_status = d['card_template_status']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'image_id_list' in d:
            o.image_id_list = d['image_id_list']
        if 'image_url_list' in d:
            o.image_url_list = d['image_url_list']
        if 'industry_solution_type' in d:
            o.industry_solution_type = d['industry_solution_type']
        if 'out_card_id' in d:
            o.out_card_id = d['out_card_id']
        if 'owner' in d:
            o.owner = d['owner']
        if 'sale_info' in d:
            o.sale_info = d['sale_info']
        if 'use_info' in d:
            o.use_info = d['use_info']
        return o



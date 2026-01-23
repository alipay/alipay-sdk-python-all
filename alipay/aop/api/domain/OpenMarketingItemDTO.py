#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenMarketingActionDTO import OpenMarketingActionDTO
from alipay.aop.api.domain.OpenMarketingBrandDTO import OpenMarketingBrandDTO


class OpenMarketingItemDTO(object):

    def __init__(self):
        self._benefit_summary = None
        self._core_selling_point_desc = None
        self._highlight_text_of_benefit_summary = None
        self._item_action_list = None
        self._item_bg_pic = None
        self._item_id = None
        self._item_logo = None
        self._item_name = None
        self._item_type = None
        self._marketing_brand = None

    @property
    def benefit_summary(self):
        return self._benefit_summary

    @benefit_summary.setter
    def benefit_summary(self, value):
        self._benefit_summary = value
    @property
    def core_selling_point_desc(self):
        return self._core_selling_point_desc

    @core_selling_point_desc.setter
    def core_selling_point_desc(self, value):
        self._core_selling_point_desc = value
    @property
    def highlight_text_of_benefit_summary(self):
        return self._highlight_text_of_benefit_summary

    @highlight_text_of_benefit_summary.setter
    def highlight_text_of_benefit_summary(self, value):
        self._highlight_text_of_benefit_summary = value
    @property
    def item_action_list(self):
        return self._item_action_list

    @item_action_list.setter
    def item_action_list(self, value):
        if isinstance(value, list):
            self._item_action_list = list()
            for i in value:
                if isinstance(i, OpenMarketingActionDTO):
                    self._item_action_list.append(i)
                else:
                    self._item_action_list.append(OpenMarketingActionDTO.from_alipay_dict(i))
    @property
    def item_bg_pic(self):
        return self._item_bg_pic

    @item_bg_pic.setter
    def item_bg_pic(self, value):
        self._item_bg_pic = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_logo(self):
        return self._item_logo

    @item_logo.setter
    def item_logo(self, value):
        self._item_logo = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def marketing_brand(self):
        return self._marketing_brand

    @marketing_brand.setter
    def marketing_brand(self, value):
        if isinstance(value, OpenMarketingBrandDTO):
            self._marketing_brand = value
        else:
            self._marketing_brand = OpenMarketingBrandDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_summary:
            if hasattr(self.benefit_summary, 'to_alipay_dict'):
                params['benefit_summary'] = self.benefit_summary.to_alipay_dict()
            else:
                params['benefit_summary'] = self.benefit_summary
        if self.core_selling_point_desc:
            if hasattr(self.core_selling_point_desc, 'to_alipay_dict'):
                params['core_selling_point_desc'] = self.core_selling_point_desc.to_alipay_dict()
            else:
                params['core_selling_point_desc'] = self.core_selling_point_desc
        if self.highlight_text_of_benefit_summary:
            if hasattr(self.highlight_text_of_benefit_summary, 'to_alipay_dict'):
                params['highlight_text_of_benefit_summary'] = self.highlight_text_of_benefit_summary.to_alipay_dict()
            else:
                params['highlight_text_of_benefit_summary'] = self.highlight_text_of_benefit_summary
        if self.item_action_list:
            if isinstance(self.item_action_list, list):
                for i in range(0, len(self.item_action_list)):
                    element = self.item_action_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_action_list[i] = element.to_alipay_dict()
            if hasattr(self.item_action_list, 'to_alipay_dict'):
                params['item_action_list'] = self.item_action_list.to_alipay_dict()
            else:
                params['item_action_list'] = self.item_action_list
        if self.item_bg_pic:
            if hasattr(self.item_bg_pic, 'to_alipay_dict'):
                params['item_bg_pic'] = self.item_bg_pic.to_alipay_dict()
            else:
                params['item_bg_pic'] = self.item_bg_pic
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_logo:
            if hasattr(self.item_logo, 'to_alipay_dict'):
                params['item_logo'] = self.item_logo.to_alipay_dict()
            else:
                params['item_logo'] = self.item_logo
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.marketing_brand:
            if hasattr(self.marketing_brand, 'to_alipay_dict'):
                params['marketing_brand'] = self.marketing_brand.to_alipay_dict()
            else:
                params['marketing_brand'] = self.marketing_brand
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenMarketingItemDTO()
        if 'benefit_summary' in d:
            o.benefit_summary = d['benefit_summary']
        if 'core_selling_point_desc' in d:
            o.core_selling_point_desc = d['core_selling_point_desc']
        if 'highlight_text_of_benefit_summary' in d:
            o.highlight_text_of_benefit_summary = d['highlight_text_of_benefit_summary']
        if 'item_action_list' in d:
            o.item_action_list = d['item_action_list']
        if 'item_bg_pic' in d:
            o.item_bg_pic = d['item_bg_pic']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_logo' in d:
            o.item_logo = d['item_logo']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'marketing_brand' in d:
            o.marketing_brand = d['marketing_brand']
        return o



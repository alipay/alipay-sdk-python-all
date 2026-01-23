#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenMarketingItemDTO import OpenMarketingItemDTO
from alipay.aop.api.domain.OpenMarketingActionDTO import OpenMarketingActionDTO


class OpenMarketingRegionDTO(object):

    def __init__(self):
        self._marketing_item_list = None
        self._region_action_list = None
        self._region_bg_pic = None
        self._region_id = None
        self._region_name = None
        self._region_position = None

    @property
    def marketing_item_list(self):
        return self._marketing_item_list

    @marketing_item_list.setter
    def marketing_item_list(self, value):
        if isinstance(value, list):
            self._marketing_item_list = list()
            for i in value:
                if isinstance(i, OpenMarketingItemDTO):
                    self._marketing_item_list.append(i)
                else:
                    self._marketing_item_list.append(OpenMarketingItemDTO.from_alipay_dict(i))
    @property
    def region_action_list(self):
        return self._region_action_list

    @region_action_list.setter
    def region_action_list(self, value):
        if isinstance(value, list):
            self._region_action_list = list()
            for i in value:
                if isinstance(i, OpenMarketingActionDTO):
                    self._region_action_list.append(i)
                else:
                    self._region_action_list.append(OpenMarketingActionDTO.from_alipay_dict(i))
    @property
    def region_bg_pic(self):
        return self._region_bg_pic

    @region_bg_pic.setter
    def region_bg_pic(self, value):
        self._region_bg_pic = value
    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, value):
        self._region_id = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value
    @property
    def region_position(self):
        return self._region_position

    @region_position.setter
    def region_position(self, value):
        self._region_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.marketing_item_list:
            if isinstance(self.marketing_item_list, list):
                for i in range(0, len(self.marketing_item_list)):
                    element = self.marketing_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.marketing_item_list[i] = element.to_alipay_dict()
            if hasattr(self.marketing_item_list, 'to_alipay_dict'):
                params['marketing_item_list'] = self.marketing_item_list.to_alipay_dict()
            else:
                params['marketing_item_list'] = self.marketing_item_list
        if self.region_action_list:
            if isinstance(self.region_action_list, list):
                for i in range(0, len(self.region_action_list)):
                    element = self.region_action_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_action_list[i] = element.to_alipay_dict()
            if hasattr(self.region_action_list, 'to_alipay_dict'):
                params['region_action_list'] = self.region_action_list.to_alipay_dict()
            else:
                params['region_action_list'] = self.region_action_list
        if self.region_bg_pic:
            if hasattr(self.region_bg_pic, 'to_alipay_dict'):
                params['region_bg_pic'] = self.region_bg_pic.to_alipay_dict()
            else:
                params['region_bg_pic'] = self.region_bg_pic
        if self.region_id:
            if hasattr(self.region_id, 'to_alipay_dict'):
                params['region_id'] = self.region_id.to_alipay_dict()
            else:
                params['region_id'] = self.region_id
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        if self.region_position:
            if hasattr(self.region_position, 'to_alipay_dict'):
                params['region_position'] = self.region_position.to_alipay_dict()
            else:
                params['region_position'] = self.region_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenMarketingRegionDTO()
        if 'marketing_item_list' in d:
            o.marketing_item_list = d['marketing_item_list']
        if 'region_action_list' in d:
            o.region_action_list = d['region_action_list']
        if 'region_bg_pic' in d:
            o.region_bg_pic = d['region_bg_pic']
        if 'region_id' in d:
            o.region_id = d['region_id']
        if 'region_name' in d:
            o.region_name = d['region_name']
        if 'region_position' in d:
            o.region_position = d['region_position']
        return o



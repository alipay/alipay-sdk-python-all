#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemDesignTextInfo import ItemDesignTextInfo


class AlipayDigitalopUcdpApecreativeResultpicCreateModel(object):

    def __init__(self):
        self._creative_item_design_text_list = None
        self._description = None
        self._group_id = None
        self._height = None
        self._project_id = None
        self._style_id_list = None
        self._width = None

    @property
    def creative_item_design_text_list(self):
        return self._creative_item_design_text_list

    @creative_item_design_text_list.setter
    def creative_item_design_text_list(self, value):
        if isinstance(value, list):
            self._creative_item_design_text_list = list()
            for i in value:
                if isinstance(i, ItemDesignTextInfo):
                    self._creative_item_design_text_list.append(i)
                else:
                    self._creative_item_design_text_list.append(ItemDesignTextInfo.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def style_id_list(self):
        return self._style_id_list

    @style_id_list.setter
    def style_id_list(self, value):
        if isinstance(value, list):
            self._style_id_list = list()
            for i in value:
                self._style_id_list.append(i)
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.creative_item_design_text_list:
            if isinstance(self.creative_item_design_text_list, list):
                for i in range(0, len(self.creative_item_design_text_list)):
                    element = self.creative_item_design_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_item_design_text_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_item_design_text_list, 'to_alipay_dict'):
                params['creative_item_design_text_list'] = self.creative_item_design_text_list.to_alipay_dict()
            else:
                params['creative_item_design_text_list'] = self.creative_item_design_text_list
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.style_id_list:
            if isinstance(self.style_id_list, list):
                for i in range(0, len(self.style_id_list)):
                    element = self.style_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.style_id_list[i] = element.to_alipay_dict()
            if hasattr(self.style_id_list, 'to_alipay_dict'):
                params['style_id_list'] = self.style_id_list.to_alipay_dict()
            else:
                params['style_id_list'] = self.style_id_list
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApecreativeResultpicCreateModel()
        if 'creative_item_design_text_list' in d:
            o.creative_item_design_text_list = d['creative_item_design_text_list']
        if 'description' in d:
            o.description = d['description']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'height' in d:
            o.height = d['height']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'style_id_list' in d:
            o.style_id_list = d['style_id_list']
        if 'width' in d:
            o.width = d['width']
        return o



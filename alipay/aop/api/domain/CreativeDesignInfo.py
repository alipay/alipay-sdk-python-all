#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeDesignRelationStyle import CreativeDesignRelationStyle


class CreativeDesignInfo(object):

    def __init__(self):
        self._creative_design_relation_style_list = None
        self._design_id = None
        self._mock_img = None

    @property
    def creative_design_relation_style_list(self):
        return self._creative_design_relation_style_list

    @creative_design_relation_style_list.setter
    def creative_design_relation_style_list(self, value):
        if isinstance(value, list):
            self._creative_design_relation_style_list = list()
            for i in value:
                if isinstance(i, CreativeDesignRelationStyle):
                    self._creative_design_relation_style_list.append(i)
                else:
                    self._creative_design_relation_style_list.append(CreativeDesignRelationStyle.from_alipay_dict(i))
    @property
    def design_id(self):
        return self._design_id

    @design_id.setter
    def design_id(self, value):
        self._design_id = value
    @property
    def mock_img(self):
        return self._mock_img

    @mock_img.setter
    def mock_img(self, value):
        self._mock_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.creative_design_relation_style_list:
            if isinstance(self.creative_design_relation_style_list, list):
                for i in range(0, len(self.creative_design_relation_style_list)):
                    element = self.creative_design_relation_style_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_design_relation_style_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_design_relation_style_list, 'to_alipay_dict'):
                params['creative_design_relation_style_list'] = self.creative_design_relation_style_list.to_alipay_dict()
            else:
                params['creative_design_relation_style_list'] = self.creative_design_relation_style_list
        if self.design_id:
            if hasattr(self.design_id, 'to_alipay_dict'):
                params['design_id'] = self.design_id.to_alipay_dict()
            else:
                params['design_id'] = self.design_id
        if self.mock_img:
            if hasattr(self.mock_img, 'to_alipay_dict'):
                params['mock_img'] = self.mock_img.to_alipay_dict()
            else:
                params['mock_img'] = self.mock_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeDesignInfo()
        if 'creative_design_relation_style_list' in d:
            o.creative_design_relation_style_list = d['creative_design_relation_style_list']
        if 'design_id' in d:
            o.design_id = d['design_id']
        if 'mock_img' in d:
            o.mock_img = d['mock_img']
        return o



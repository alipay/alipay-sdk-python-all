#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingImageDeleteModel(object):

    def __init__(self):
        self._image_index_id_list = None

    @property
    def image_index_id_list(self):
        return self._image_index_id_list

    @image_index_id_list.setter
    def image_index_id_list(self, value):
        if isinstance(value, list):
            self._image_index_id_list = list()
            for i in value:
                self._image_index_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.image_index_id_list:
            if isinstance(self.image_index_id_list, list):
                for i in range(0, len(self.image_index_id_list)):
                    element = self.image_index_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_index_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_index_id_list, 'to_alipay_dict'):
                params['image_index_id_list'] = self.image_index_id_list.to_alipay_dict()
            else:
                params['image_index_id_list'] = self.image_index_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingImageDeleteModel()
        if 'image_index_id_list' in d:
            o.image_index_id_list = d['image_index_id_list']
        return o



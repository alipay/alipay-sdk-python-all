#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionOrderInspectProofDTO(object):

    def __init__(self):
        self._img_ids = None
        self._text = None

    @property
    def img_ids(self):
        return self._img_ids

    @img_ids.setter
    def img_ids(self, value):
        if isinstance(value, list):
            self._img_ids = list()
            for i in value:
                self._img_ids.append(i)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_ids:
            if isinstance(self.img_ids, list):
                for i in range(0, len(self.img_ids)):
                    element = self.img_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_ids[i] = element.to_alipay_dict()
            if hasattr(self.img_ids, 'to_alipay_dict'):
                params['img_ids'] = self.img_ids.to_alipay_dict()
            else:
                params['img_ids'] = self.img_ids
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionOrderInspectProofDTO()
        if 'img_ids' in d:
            o.img_ids = d['img_ids']
        if 'text' in d:
            o.text = d['text']
        return o



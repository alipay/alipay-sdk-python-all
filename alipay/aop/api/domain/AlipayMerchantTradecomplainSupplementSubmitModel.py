#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantTradecomplainSupplementSubmitModel(object):

    def __init__(self):
        self._complain_event_id = None
        self._supplement_content = None
        self._supplement_images = None

    @property
    def complain_event_id(self):
        return self._complain_event_id

    @complain_event_id.setter
    def complain_event_id(self, value):
        self._complain_event_id = value
    @property
    def supplement_content(self):
        return self._supplement_content

    @supplement_content.setter
    def supplement_content(self, value):
        self._supplement_content = value
    @property
    def supplement_images(self):
        return self._supplement_images

    @supplement_images.setter
    def supplement_images(self, value):
        self._supplement_images = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_event_id:
            if hasattr(self.complain_event_id, 'to_alipay_dict'):
                params['complain_event_id'] = self.complain_event_id.to_alipay_dict()
            else:
                params['complain_event_id'] = self.complain_event_id
        if self.supplement_content:
            if hasattr(self.supplement_content, 'to_alipay_dict'):
                params['supplement_content'] = self.supplement_content.to_alipay_dict()
            else:
                params['supplement_content'] = self.supplement_content
        if self.supplement_images:
            if hasattr(self.supplement_images, 'to_alipay_dict'):
                params['supplement_images'] = self.supplement_images.to_alipay_dict()
            else:
                params['supplement_images'] = self.supplement_images
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantTradecomplainSupplementSubmitModel()
        if 'complain_event_id' in d:
            o.complain_event_id = d['complain_event_id']
        if 'supplement_content' in d:
            o.supplement_content = d['supplement_content']
        if 'supplement_images' in d:
            o.supplement_images = d['supplement_images']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDisplayInfoDTO(object):

    def __init__(self):
        self._action_text = None
        self._action_type = None
        self._action_url = None
        self._benefit_detail_images = None
        self._benefit_image = None
        self._brand_logo = None
        self._brand_name = None

    @property
    def action_text(self):
        return self._action_text

    @action_text.setter
    def action_text(self, value):
        self._action_text = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def benefit_detail_images(self):
        return self._benefit_detail_images

    @benefit_detail_images.setter
    def benefit_detail_images(self, value):
        if isinstance(value, list):
            self._benefit_detail_images = list()
            for i in value:
                self._benefit_detail_images.append(i)
    @property
    def benefit_image(self):
        return self._benefit_image

    @benefit_image.setter
    def benefit_image(self, value):
        self._benefit_image = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_text:
            if hasattr(self.action_text, 'to_alipay_dict'):
                params['action_text'] = self.action_text.to_alipay_dict()
            else:
                params['action_text'] = self.action_text
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.benefit_detail_images:
            if isinstance(self.benefit_detail_images, list):
                for i in range(0, len(self.benefit_detail_images)):
                    element = self.benefit_detail_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_detail_images[i] = element.to_alipay_dict()
            if hasattr(self.benefit_detail_images, 'to_alipay_dict'):
                params['benefit_detail_images'] = self.benefit_detail_images.to_alipay_dict()
            else:
                params['benefit_detail_images'] = self.benefit_detail_images
        if self.benefit_image:
            if hasattr(self.benefit_image, 'to_alipay_dict'):
                params['benefit_image'] = self.benefit_image.to_alipay_dict()
            else:
                params['benefit_image'] = self.benefit_image
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDisplayInfoDTO()
        if 'action_text' in d:
            o.action_text = d['action_text']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'benefit_detail_images' in d:
            o.benefit_detail_images = d['benefit_detail_images']
        if 'benefit_image' in d:
            o.benefit_image = d['benefit_image']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        return o



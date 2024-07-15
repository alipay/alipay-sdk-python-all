#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LinkedMallEditableProduct(object):

    def __init__(self):
        self._desc_path = None
        self._images = None
        self._pic_url = None
        self._product_status = None
        self._title = None

    @property
    def desc_path(self):
        return self._desc_path

    @desc_path.setter
    def desc_path(self, value):
        self._desc_path = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc_path:
            if hasattr(self.desc_path, 'to_alipay_dict'):
                params['desc_path'] = self.desc_path.to_alipay_dict()
            else:
                params['desc_path'] = self.desc_path
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.product_status:
            if hasattr(self.product_status, 'to_alipay_dict'):
                params['product_status'] = self.product_status.to_alipay_dict()
            else:
                params['product_status'] = self.product_status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkedMallEditableProduct()
        if 'desc_path' in d:
            o.desc_path = d['desc_path']
        if 'images' in d:
            o.images = d['images']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'product_status' in d:
            o.product_status = d['product_status']
        if 'title' in d:
            o.title = d['title']
        return o



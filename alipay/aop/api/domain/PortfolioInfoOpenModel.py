#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortfolioInfoOpenModel(object):

    def __init__(self):
        self._cover_image_id = None
        self._cover_image_type = None
        self._cover_image_url = None
        self._portfolio_id = None
        self._portfolio_title = None

    @property
    def cover_image_id(self):
        return self._cover_image_id

    @cover_image_id.setter
    def cover_image_id(self, value):
        self._cover_image_id = value
    @property
    def cover_image_type(self):
        return self._cover_image_type

    @cover_image_type.setter
    def cover_image_type(self, value):
        self._cover_image_type = value
    @property
    def cover_image_url(self):
        return self._cover_image_url

    @cover_image_url.setter
    def cover_image_url(self, value):
        self._cover_image_url = value
    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self._portfolio_id = value
    @property
    def portfolio_title(self):
        return self._portfolio_title

    @portfolio_title.setter
    def portfolio_title(self, value):
        self._portfolio_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover_image_id:
            if hasattr(self.cover_image_id, 'to_alipay_dict'):
                params['cover_image_id'] = self.cover_image_id.to_alipay_dict()
            else:
                params['cover_image_id'] = self.cover_image_id
        if self.cover_image_type:
            if hasattr(self.cover_image_type, 'to_alipay_dict'):
                params['cover_image_type'] = self.cover_image_type.to_alipay_dict()
            else:
                params['cover_image_type'] = self.cover_image_type
        if self.cover_image_url:
            if hasattr(self.cover_image_url, 'to_alipay_dict'):
                params['cover_image_url'] = self.cover_image_url.to_alipay_dict()
            else:
                params['cover_image_url'] = self.cover_image_url
        if self.portfolio_id:
            if hasattr(self.portfolio_id, 'to_alipay_dict'):
                params['portfolio_id'] = self.portfolio_id.to_alipay_dict()
            else:
                params['portfolio_id'] = self.portfolio_id
        if self.portfolio_title:
            if hasattr(self.portfolio_title, 'to_alipay_dict'):
                params['portfolio_title'] = self.portfolio_title.to_alipay_dict()
            else:
                params['portfolio_title'] = self.portfolio_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortfolioInfoOpenModel()
        if 'cover_image_id' in d:
            o.cover_image_id = d['cover_image_id']
        if 'cover_image_type' in d:
            o.cover_image_type = d['cover_image_type']
        if 'cover_image_url' in d:
            o.cover_image_url = d['cover_image_url']
        if 'portfolio_id' in d:
            o.portfolio_id = d['portfolio_id']
        if 'portfolio_title' in d:
            o.portfolio_title = d['portfolio_title']
        return o



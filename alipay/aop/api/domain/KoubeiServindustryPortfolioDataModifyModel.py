#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortfolioOperatorInfo import PortfolioOperatorInfo
from alipay.aop.api.domain.PortfolioShop import PortfolioShop


class KoubeiServindustryPortfolioDataModifyModel(object):

    def __init__(self):
        self._cover_media_id = None
        self._cover_media_type = None
        self._portfolio_id = None
        self._portfolio_operator_info = None
        self._portfolio_shops = None
        self._title = None

    @property
    def cover_media_id(self):
        return self._cover_media_id

    @cover_media_id.setter
    def cover_media_id(self, value):
        self._cover_media_id = value
    @property
    def cover_media_type(self):
        return self._cover_media_type

    @cover_media_type.setter
    def cover_media_type(self, value):
        self._cover_media_type = value
    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self._portfolio_id = value
    @property
    def portfolio_operator_info(self):
        return self._portfolio_operator_info

    @portfolio_operator_info.setter
    def portfolio_operator_info(self, value):
        if isinstance(value, PortfolioOperatorInfo):
            self._portfolio_operator_info = value
        else:
            self._portfolio_operator_info = PortfolioOperatorInfo.from_alipay_dict(value)
    @property
    def portfolio_shops(self):
        return self._portfolio_shops

    @portfolio_shops.setter
    def portfolio_shops(self, value):
        if isinstance(value, list):
            self._portfolio_shops = list()
            for i in value:
                if isinstance(i, PortfolioShop):
                    self._portfolio_shops.append(i)
                else:
                    self._portfolio_shops.append(PortfolioShop.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover_media_id:
            if hasattr(self.cover_media_id, 'to_alipay_dict'):
                params['cover_media_id'] = self.cover_media_id.to_alipay_dict()
            else:
                params['cover_media_id'] = self.cover_media_id
        if self.cover_media_type:
            if hasattr(self.cover_media_type, 'to_alipay_dict'):
                params['cover_media_type'] = self.cover_media_type.to_alipay_dict()
            else:
                params['cover_media_type'] = self.cover_media_type
        if self.portfolio_id:
            if hasattr(self.portfolio_id, 'to_alipay_dict'):
                params['portfolio_id'] = self.portfolio_id.to_alipay_dict()
            else:
                params['portfolio_id'] = self.portfolio_id
        if self.portfolio_operator_info:
            if hasattr(self.portfolio_operator_info, 'to_alipay_dict'):
                params['portfolio_operator_info'] = self.portfolio_operator_info.to_alipay_dict()
            else:
                params['portfolio_operator_info'] = self.portfolio_operator_info
        if self.portfolio_shops:
            if isinstance(self.portfolio_shops, list):
                for i in range(0, len(self.portfolio_shops)):
                    element = self.portfolio_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.portfolio_shops[i] = element.to_alipay_dict()
            if hasattr(self.portfolio_shops, 'to_alipay_dict'):
                params['portfolio_shops'] = self.portfolio_shops.to_alipay_dict()
            else:
                params['portfolio_shops'] = self.portfolio_shops
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
        o = KoubeiServindustryPortfolioDataModifyModel()
        if 'cover_media_id' in d:
            o.cover_media_id = d['cover_media_id']
        if 'cover_media_type' in d:
            o.cover_media_type = d['cover_media_type']
        if 'portfolio_id' in d:
            o.portfolio_id = d['portfolio_id']
        if 'portfolio_operator_info' in d:
            o.portfolio_operator_info = d['portfolio_operator_info']
        if 'portfolio_shops' in d:
            o.portfolio_shops = d['portfolio_shops']
        if 'title' in d:
            o.title = d['title']
        return o



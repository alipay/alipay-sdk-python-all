#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetBomItem import AssetBomItem
from alipay.aop.api.domain.AssetFileInfo import AssetFileInfo
from alipay.aop.api.domain.AssetFileInfo import AssetFileInfo


class AssetItemVersion(object):

    def __init__(self):
        self._bom_items = None
        self._design_img = None
        self._effect_img = None
        self._item_version = None
        self._status = None

    @property
    def bom_items(self):
        return self._bom_items

    @bom_items.setter
    def bom_items(self, value):
        if isinstance(value, list):
            self._bom_items = list()
            for i in value:
                if isinstance(i, AssetBomItem):
                    self._bom_items.append(i)
                else:
                    self._bom_items.append(AssetBomItem.from_alipay_dict(i))
    @property
    def design_img(self):
        return self._design_img

    @design_img.setter
    def design_img(self, value):
        if isinstance(value, list):
            self._design_img = list()
            for i in value:
                if isinstance(i, AssetFileInfo):
                    self._design_img.append(i)
                else:
                    self._design_img.append(AssetFileInfo.from_alipay_dict(i))
    @property
    def effect_img(self):
        return self._effect_img

    @effect_img.setter
    def effect_img(self, value):
        if isinstance(value, list):
            self._effect_img = list()
            for i in value:
                if isinstance(i, AssetFileInfo):
                    self._effect_img.append(i)
                else:
                    self._effect_img.append(AssetFileInfo.from_alipay_dict(i))
    @property
    def item_version(self):
        return self._item_version

    @item_version.setter
    def item_version(self, value):
        self._item_version = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bom_items:
            if isinstance(self.bom_items, list):
                for i in range(0, len(self.bom_items)):
                    element = self.bom_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bom_items[i] = element.to_alipay_dict()
            if hasattr(self.bom_items, 'to_alipay_dict'):
                params['bom_items'] = self.bom_items.to_alipay_dict()
            else:
                params['bom_items'] = self.bom_items
        if self.design_img:
            if isinstance(self.design_img, list):
                for i in range(0, len(self.design_img)):
                    element = self.design_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.design_img[i] = element.to_alipay_dict()
            if hasattr(self.design_img, 'to_alipay_dict'):
                params['design_img'] = self.design_img.to_alipay_dict()
            else:
                params['design_img'] = self.design_img
        if self.effect_img:
            if isinstance(self.effect_img, list):
                for i in range(0, len(self.effect_img)):
                    element = self.effect_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effect_img[i] = element.to_alipay_dict()
            if hasattr(self.effect_img, 'to_alipay_dict'):
                params['effect_img'] = self.effect_img.to_alipay_dict()
            else:
                params['effect_img'] = self.effect_img
        if self.item_version:
            if hasattr(self.item_version, 'to_alipay_dict'):
                params['item_version'] = self.item_version.to_alipay_dict()
            else:
                params['item_version'] = self.item_version
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetItemVersion()
        if 'bom_items' in d:
            o.bom_items = d['bom_items']
        if 'design_img' in d:
            o.design_img = d['design_img']
        if 'effect_img' in d:
            o.effect_img = d['effect_img']
        if 'item_version' in d:
            o.item_version = d['item_version']
        if 'status' in d:
            o.status = d['status']
        return o



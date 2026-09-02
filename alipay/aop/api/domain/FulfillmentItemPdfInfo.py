#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemInfoForFulfillmentList import ItemInfoForFulfillmentList


class FulfillmentItemPdfInfo(object):

    def __init__(self):
        self._file_id = None
        self._item_ids = None
        self._item_infos = None
        self._link = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, ItemInfoForFulfillmentList):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(ItemInfoForFulfillmentList.from_alipay_dict(i))
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentItemPdfInfo()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'link' in d:
            o.link = d['link']
        return o



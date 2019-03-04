#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PriceInfo import PriceInfo
from alipay.aop.api.domain.ItemCategoryInfo import ItemCategoryInfo


class AlipayBusinessItemExternalSyncModel(object):

    def __init__(self):
        self._end_date = None
        self._ext_price_info = None
        self._ext_prop = None
        self._external_category_info = None
        self._external_item_id = None
        self._inventory = None
        self._item_type = None
        self._original_price = None
        self._picture_info = None
        self._promotion_type = None
        self._request_id = None
        self._start_date = None
        self._status = None
        self._subject = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ext_price_info(self):
        return self._ext_price_info

    @ext_price_info.setter
    def ext_price_info(self, value):
        if isinstance(value, list):
            self._ext_price_info = list()
            for i in value:
                if isinstance(i, PriceInfo):
                    self._ext_price_info.append(i)
                else:
                    self._ext_price_info.append(PriceInfo.from_alipay_dict(i))
    @property
    def ext_prop(self):
        return self._ext_prop

    @ext_prop.setter
    def ext_prop(self, value):
        self._ext_prop = value
    @property
    def external_category_info(self):
        return self._external_category_info

    @external_category_info.setter
    def external_category_info(self, value):
        if isinstance(value, ItemCategoryInfo):
            self._external_category_info = value
        else:
            self._external_category_info = ItemCategoryInfo.from_alipay_dict(value)
    @property
    def external_item_id(self):
        return self._external_item_id

    @external_item_id.setter
    def external_item_id(self, value):
        self._external_item_id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def picture_info(self):
        return self._picture_info

    @picture_info.setter
    def picture_info(self, value):
        self._picture_info = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ext_price_info:
            if isinstance(self.ext_price_info, list):
                for i in range(0, len(self.ext_price_info)):
                    element = self.ext_price_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_price_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_price_info, 'to_alipay_dict'):
                params['ext_price_info'] = self.ext_price_info.to_alipay_dict()
            else:
                params['ext_price_info'] = self.ext_price_info
        if self.ext_prop:
            if hasattr(self.ext_prop, 'to_alipay_dict'):
                params['ext_prop'] = self.ext_prop.to_alipay_dict()
            else:
                params['ext_prop'] = self.ext_prop
        if self.external_category_info:
            if hasattr(self.external_category_info, 'to_alipay_dict'):
                params['external_category_info'] = self.external_category_info.to_alipay_dict()
            else:
                params['external_category_info'] = self.external_category_info
        if self.external_item_id:
            if hasattr(self.external_item_id, 'to_alipay_dict'):
                params['external_item_id'] = self.external_item_id.to_alipay_dict()
            else:
                params['external_item_id'] = self.external_item_id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.picture_info:
            if hasattr(self.picture_info, 'to_alipay_dict'):
                params['picture_info'] = self.picture_info.to_alipay_dict()
            else:
                params['picture_info'] = self.picture_info
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessItemExternalSyncModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_price_info' in d:
            o.ext_price_info = d['ext_price_info']
        if 'ext_prop' in d:
            o.ext_prop = d['ext_prop']
        if 'external_category_info' in d:
            o.external_category_info = d['external_category_info']
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'picture_info' in d:
            o.picture_info = d['picture_info']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'subject' in d:
            o.subject = d['subject']
        return o



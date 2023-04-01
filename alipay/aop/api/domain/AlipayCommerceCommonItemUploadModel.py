#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair
from alipay.aop.api.domain.ItemDeliveryInfoSyncRequest import ItemDeliveryInfoSyncRequest
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair
from alipay.aop.api.domain.ItemPromoInfoSyncRequest import ItemPromoInfoSyncRequest
from alipay.aop.api.domain.IndustryItemSkuSyncRequest import IndustryItemSkuSyncRequest


class AlipayCommerceCommonItemUploadModel(object):

    def __init__(self):
        self._biz_item_info = None
        self._biz_item_type = None
        self._biz_scene = None
        self._category_id = None
        self._delivery_infos = None
        self._ext_info = None
        self._item_desc = None
        self._item_highlight_list = None
        self._item_id = None
        self._item_image_list = None
        self._item_main_image = None
        self._item_name = None
        self._item_spec_list = None
        self._item_title = None
        self._item_url = None
        self._original_price = None
        self._price = None
        self._price_unit = None
        self._promo_infos = None
        self._sell_status = None
        self._sku_list = None
        self._stock_num = None

    @property
    def biz_item_info(self):
        return self._biz_item_info

    @biz_item_info.setter
    def biz_item_info(self, value):
        if isinstance(value, list):
            self._biz_item_info = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._biz_item_info.append(i)
                else:
                    self._biz_item_info.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def biz_item_type(self):
        return self._biz_item_type

    @biz_item_type.setter
    def biz_item_type(self, value):
        self._biz_item_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def delivery_infos(self):
        return self._delivery_infos

    @delivery_infos.setter
    def delivery_infos(self, value):
        if isinstance(value, ItemDeliveryInfoSyncRequest):
            self._delivery_infos = value
        else:
            self._delivery_infos = ItemDeliveryInfoSyncRequest.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_highlight_list(self):
        return self._item_highlight_list

    @item_highlight_list.setter
    def item_highlight_list(self, value):
        if isinstance(value, list):
            self._item_highlight_list = list()
            for i in value:
                self._item_highlight_list.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_image_list(self):
        return self._item_image_list

    @item_image_list.setter
    def item_image_list(self, value):
        if isinstance(value, list):
            self._item_image_list = list()
            for i in value:
                self._item_image_list.append(i)
    @property
    def item_main_image(self):
        return self._item_main_image

    @item_main_image.setter
    def item_main_image(self, value):
        self._item_main_image = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_spec_list(self):
        return self._item_spec_list

    @item_spec_list.setter
    def item_spec_list(self, value):
        if isinstance(value, list):
            self._item_spec_list = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._item_spec_list.append(i)
                else:
                    self._item_spec_list.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def promo_infos(self):
        return self._promo_infos

    @promo_infos.setter
    def promo_infos(self, value):
        if isinstance(value, ItemPromoInfoSyncRequest):
            self._promo_infos = value
        else:
            self._promo_infos = ItemPromoInfoSyncRequest.from_alipay_dict(value)
    @property
    def sell_status(self):
        return self._sell_status

    @sell_status.setter
    def sell_status(self, value):
        self._sell_status = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, IndustryItemSkuSyncRequest):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(IndustryItemSkuSyncRequest.from_alipay_dict(i))
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_item_info:
            if isinstance(self.biz_item_info, list):
                for i in range(0, len(self.biz_item_info)):
                    element = self.biz_item_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_item_info[i] = element.to_alipay_dict()
            if hasattr(self.biz_item_info, 'to_alipay_dict'):
                params['biz_item_info'] = self.biz_item_info.to_alipay_dict()
            else:
                params['biz_item_info'] = self.biz_item_info
        if self.biz_item_type:
            if hasattr(self.biz_item_type, 'to_alipay_dict'):
                params['biz_item_type'] = self.biz_item_type.to_alipay_dict()
            else:
                params['biz_item_type'] = self.biz_item_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.delivery_infos:
            if hasattr(self.delivery_infos, 'to_alipay_dict'):
                params['delivery_infos'] = self.delivery_infos.to_alipay_dict()
            else:
                params['delivery_infos'] = self.delivery_infos
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_highlight_list:
            if isinstance(self.item_highlight_list, list):
                for i in range(0, len(self.item_highlight_list)):
                    element = self.item_highlight_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_highlight_list[i] = element.to_alipay_dict()
            if hasattr(self.item_highlight_list, 'to_alipay_dict'):
                params['item_highlight_list'] = self.item_highlight_list.to_alipay_dict()
            else:
                params['item_highlight_list'] = self.item_highlight_list
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_image_list:
            if isinstance(self.item_image_list, list):
                for i in range(0, len(self.item_image_list)):
                    element = self.item_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_image_list[i] = element.to_alipay_dict()
            if hasattr(self.item_image_list, 'to_alipay_dict'):
                params['item_image_list'] = self.item_image_list.to_alipay_dict()
            else:
                params['item_image_list'] = self.item_image_list
        if self.item_main_image:
            if hasattr(self.item_main_image, 'to_alipay_dict'):
                params['item_main_image'] = self.item_main_image.to_alipay_dict()
            else:
                params['item_main_image'] = self.item_main_image
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_spec_list:
            if isinstance(self.item_spec_list, list):
                for i in range(0, len(self.item_spec_list)):
                    element = self.item_spec_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_spec_list[i] = element.to_alipay_dict()
            if hasattr(self.item_spec_list, 'to_alipay_dict'):
                params['item_spec_list'] = self.item_spec_list.to_alipay_dict()
            else:
                params['item_spec_list'] = self.item_spec_list
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.promo_infos:
            if hasattr(self.promo_infos, 'to_alipay_dict'):
                params['promo_infos'] = self.promo_infos.to_alipay_dict()
            else:
                params['promo_infos'] = self.promo_infos
        if self.sell_status:
            if hasattr(self.sell_status, 'to_alipay_dict'):
                params['sell_status'] = self.sell_status.to_alipay_dict()
            else:
                params['sell_status'] = self.sell_status
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonItemUploadModel()
        if 'biz_item_info' in d:
            o.biz_item_info = d['biz_item_info']
        if 'biz_item_type' in d:
            o.biz_item_type = d['biz_item_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'delivery_infos' in d:
            o.delivery_infos = d['delivery_infos']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_highlight_list' in d:
            o.item_highlight_list = d['item_highlight_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_image_list' in d:
            o.item_image_list = d['item_image_list']
        if 'item_main_image' in d:
            o.item_main_image = d['item_main_image']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_spec_list' in d:
            o.item_spec_list = d['item_spec_list']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'item_url' in d:
            o.item_url = d['item_url']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'promo_infos' in d:
            o.promo_infos = d['promo_infos']
        if 'sell_status' in d:
            o.sell_status = d['sell_status']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        return o



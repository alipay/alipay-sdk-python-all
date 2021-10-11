#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GolGoodsExtParam import GolGoodsExtParam
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.GoodsSalesVolume import GoodsSalesVolume


class AlipayOverseasTravelGoodsSyncModel(object):

    def __init__(self):
        self._cover = None
        self._external_link_url = None
        self._gol_goods_ext_param = None
        self._goods_category = None
        self._goods_name = None
        self._goods_tags = None
        self._inventory_sync = None
        self._original_price = None
        self._out_goods_id = None
        self._out_shop_id = None
        self._out_shop_ids = None
        self._price = None
        self._recommend = None
        self._sale_end_time = None
        self._sale_start_time = None
        self._sales_volume = None
        self._scenarios = None
        self._status = None

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def external_link_url(self):
        return self._external_link_url

    @external_link_url.setter
    def external_link_url(self, value):
        self._external_link_url = value
    @property
    def gol_goods_ext_param(self):
        return self._gol_goods_ext_param

    @gol_goods_ext_param.setter
    def gol_goods_ext_param(self, value):
        if isinstance(value, GolGoodsExtParam):
            self._gol_goods_ext_param = value
        else:
            self._gol_goods_ext_param = GolGoodsExtParam.from_alipay_dict(value)
    @property
    def goods_category(self):
        return self._goods_category

    @goods_category.setter
    def goods_category(self, value):
        self._goods_category = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_tags(self):
        return self._goods_tags

    @goods_tags.setter
    def goods_tags(self, value):
        if isinstance(value, list):
            self._goods_tags = list()
            for i in value:
                self._goods_tags.append(i)
    @property
    def inventory_sync(self):
        return self._inventory_sync

    @inventory_sync.setter
    def inventory_sync(self, value):
        self._inventory_sync = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        if isinstance(value, Amount):
            self._original_price = value
        else:
            self._original_price = Amount.from_alipay_dict(value)
    @property
    def out_goods_id(self):
        return self._out_goods_id

    @out_goods_id.setter
    def out_goods_id(self, value):
        self._out_goods_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def out_shop_ids(self):
        return self._out_shop_ids

    @out_shop_ids.setter
    def out_shop_ids(self, value):
        if isinstance(value, list):
            self._out_shop_ids = list()
            for i in value:
                self._out_shop_ids.append(i)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, Amount):
            self._price = value
        else:
            self._price = Amount.from_alipay_dict(value)
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def sale_end_time(self):
        return self._sale_end_time

    @sale_end_time.setter
    def sale_end_time(self, value):
        self._sale_end_time = value
    @property
    def sale_start_time(self):
        return self._sale_start_time

    @sale_start_time.setter
    def sale_start_time(self, value):
        self._sale_start_time = value
    @property
    def sales_volume(self):
        return self._sales_volume

    @sales_volume.setter
    def sales_volume(self, value):
        if isinstance(value, GoodsSalesVolume):
            self._sales_volume = value
        else:
            self._sales_volume = GoodsSalesVolume.from_alipay_dict(value)
    @property
    def scenarios(self):
        return self._scenarios

    @scenarios.setter
    def scenarios(self, value):
        if isinstance(value, list):
            self._scenarios = list()
            for i in value:
                self._scenarios.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.external_link_url:
            if hasattr(self.external_link_url, 'to_alipay_dict'):
                params['external_link_url'] = self.external_link_url.to_alipay_dict()
            else:
                params['external_link_url'] = self.external_link_url
        if self.gol_goods_ext_param:
            if hasattr(self.gol_goods_ext_param, 'to_alipay_dict'):
                params['gol_goods_ext_param'] = self.gol_goods_ext_param.to_alipay_dict()
            else:
                params['gol_goods_ext_param'] = self.gol_goods_ext_param
        if self.goods_category:
            if hasattr(self.goods_category, 'to_alipay_dict'):
                params['goods_category'] = self.goods_category.to_alipay_dict()
            else:
                params['goods_category'] = self.goods_category
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_tags:
            if isinstance(self.goods_tags, list):
                for i in range(0, len(self.goods_tags)):
                    element = self.goods_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_tags[i] = element.to_alipay_dict()
            if hasattr(self.goods_tags, 'to_alipay_dict'):
                params['goods_tags'] = self.goods_tags.to_alipay_dict()
            else:
                params['goods_tags'] = self.goods_tags
        if self.inventory_sync:
            if hasattr(self.inventory_sync, 'to_alipay_dict'):
                params['inventory_sync'] = self.inventory_sync.to_alipay_dict()
            else:
                params['inventory_sync'] = self.inventory_sync
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_goods_id:
            if hasattr(self.out_goods_id, 'to_alipay_dict'):
                params['out_goods_id'] = self.out_goods_id.to_alipay_dict()
            else:
                params['out_goods_id'] = self.out_goods_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.out_shop_ids:
            if isinstance(self.out_shop_ids, list):
                for i in range(0, len(self.out_shop_ids)):
                    element = self.out_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_shop_ids, 'to_alipay_dict'):
                params['out_shop_ids'] = self.out_shop_ids.to_alipay_dict()
            else:
                params['out_shop_ids'] = self.out_shop_ids
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.sale_end_time:
            if hasattr(self.sale_end_time, 'to_alipay_dict'):
                params['sale_end_time'] = self.sale_end_time.to_alipay_dict()
            else:
                params['sale_end_time'] = self.sale_end_time
        if self.sale_start_time:
            if hasattr(self.sale_start_time, 'to_alipay_dict'):
                params['sale_start_time'] = self.sale_start_time.to_alipay_dict()
            else:
                params['sale_start_time'] = self.sale_start_time
        if self.sales_volume:
            if hasattr(self.sales_volume, 'to_alipay_dict'):
                params['sales_volume'] = self.sales_volume.to_alipay_dict()
            else:
                params['sales_volume'] = self.sales_volume
        if self.scenarios:
            if isinstance(self.scenarios, list):
                for i in range(0, len(self.scenarios)):
                    element = self.scenarios[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenarios[i] = element.to_alipay_dict()
            if hasattr(self.scenarios, 'to_alipay_dict'):
                params['scenarios'] = self.scenarios.to_alipay_dict()
            else:
                params['scenarios'] = self.scenarios
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
        o = AlipayOverseasTravelGoodsSyncModel()
        if 'cover' in d:
            o.cover = d['cover']
        if 'external_link_url' in d:
            o.external_link_url = d['external_link_url']
        if 'gol_goods_ext_param' in d:
            o.gol_goods_ext_param = d['gol_goods_ext_param']
        if 'goods_category' in d:
            o.goods_category = d['goods_category']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_tags' in d:
            o.goods_tags = d['goods_tags']
        if 'inventory_sync' in d:
            o.inventory_sync = d['inventory_sync']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_goods_id' in d:
            o.out_goods_id = d['out_goods_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'out_shop_ids' in d:
            o.out_shop_ids = d['out_shop_ids']
        if 'price' in d:
            o.price = d['price']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'sale_end_time' in d:
            o.sale_end_time = d['sale_end_time']
        if 'sale_start_time' in d:
            o.sale_start_time = d['sale_start_time']
        if 'sales_volume' in d:
            o.sales_volume = d['sales_volume']
        if 'scenarios' in d:
            o.scenarios = d['scenarios']
        if 'status' in d:
            o.status = d['status']
        return o



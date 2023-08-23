#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO
from alipay.aop.api.domain.PhoneStructVO import PhoneStructVO
from alipay.aop.api.domain.ItemRiskInfo import ItemRiskInfo
from alipay.aop.api.domain.ItemSceneRiskInfo import ItemSceneRiskInfo
from alipay.aop.api.domain.LocalItemSkuQueryVO import LocalItemSkuQueryVO
from alipay.aop.api.domain.TimeRangeStructVO import TimeRangeStructVO


class AlipayOpenAppLocalitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppLocalitemQueryResponse, self).__init__()
        self._attrs = None
        self._category_id = None
        self._create_time = None
        self._customer_service_mobile = None
        self._head_img = None
        self._image_list = None
        self._is_online = None
        self._item_details_page_model = None
        self._item_id = None
        self._item_type = None
        self._merchant_name = None
        self._out_item_id = None
        self._path = None
        self._risk_info = None
        self._scene_risk_info = None
        self._skus = None
        self._sold_time = None
        self._spu_status = None
        self._stock_num = None
        self._title = None
        self._update_time = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, AppItemAttrVO):
                    self._attrs.append(i)
                else:
                    self._attrs.append(AppItemAttrVO.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        if isinstance(value, PhoneStructVO):
            self._customer_service_mobile = value
        else:
            self._customer_service_mobile = PhoneStructVO.from_alipay_dict(value)
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def item_details_page_model(self):
        return self._item_details_page_model

    @item_details_page_model.setter
    def item_details_page_model(self, value):
        self._item_details_page_model = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        if isinstance(value, list):
            self._risk_info = list()
            for i in value:
                if isinstance(i, ItemRiskInfo):
                    self._risk_info.append(i)
                else:
                    self._risk_info.append(ItemRiskInfo.from_alipay_dict(i))
    @property
    def scene_risk_info(self):
        return self._scene_risk_info

    @scene_risk_info.setter
    def scene_risk_info(self, value):
        if isinstance(value, list):
            self._scene_risk_info = list()
            for i in value:
                if isinstance(i, ItemSceneRiskInfo):
                    self._scene_risk_info.append(i)
                else:
                    self._scene_risk_info.append(ItemSceneRiskInfo.from_alipay_dict(i))
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LocalItemSkuQueryVO):
                    self._skus.append(i)
                else:
                    self._skus.append(LocalItemSkuQueryVO.from_alipay_dict(i))
    @property
    def sold_time(self):
        return self._sold_time

    @sold_time.setter
    def sold_time(self, value):
        if isinstance(value, TimeRangeStructVO):
            self._sold_time = value
        else:
            self._sold_time = TimeRangeStructVO.from_alipay_dict(value)
    @property
    def spu_status(self):
        return self._spu_status

    @spu_status.setter
    def spu_status(self, value):
        self._spu_status = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppLocalitemQueryResponse, self).parse_response_content(response_content)
        if 'attrs' in response:
            self.attrs = response['attrs']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'customer_service_mobile' in response:
            self.customer_service_mobile = response['customer_service_mobile']
        if 'head_img' in response:
            self.head_img = response['head_img']
        if 'image_list' in response:
            self.image_list = response['image_list']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'item_details_page_model' in response:
            self.item_details_page_model = response['item_details_page_model']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_type' in response:
            self.item_type = response['item_type']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'path' in response:
            self.path = response['path']
        if 'risk_info' in response:
            self.risk_info = response['risk_info']
        if 'scene_risk_info' in response:
            self.scene_risk_info = response['scene_risk_info']
        if 'skus' in response:
            self.skus = response['skus']
        if 'sold_time' in response:
            self.sold_time = response['sold_time']
        if 'spu_status' in response:
            self.spu_status = response['spu_status']
        if 'stock_num' in response:
            self.stock_num = response['stock_num']
        if 'title' in response:
            self.title = response['title']
        if 'update_time' in response:
            self.update_time = response['update_time']

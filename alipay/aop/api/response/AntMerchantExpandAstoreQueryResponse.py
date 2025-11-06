#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BrandInfoModel import BrandInfoModel
from alipay.aop.api.domain.CategoryInfoModel import CategoryInfoModel
from alipay.aop.api.domain.SettleInfoModel import SettleInfoModel


class AntMerchantExpandAstoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAstoreQueryResponse, self).__init__()
        self._a_store_id = None
        self._a_store_name = None
        self._brand_info = None
        self._category_info = None
        self._out_biz_no = None
        self._settle_infos = None
        self._smid = None

    @property
    def a_store_id(self):
        return self._a_store_id

    @a_store_id.setter
    def a_store_id(self, value):
        self._a_store_id = value
    @property
    def a_store_name(self):
        return self._a_store_name

    @a_store_name.setter
    def a_store_name(self, value):
        self._a_store_name = value
    @property
    def brand_info(self):
        return self._brand_info

    @brand_info.setter
    def brand_info(self, value):
        if isinstance(value, BrandInfoModel):
            self._brand_info = value
        else:
            self._brand_info = BrandInfoModel.from_alipay_dict(value)
    @property
    def category_info(self):
        return self._category_info

    @category_info.setter
    def category_info(self, value):
        if isinstance(value, CategoryInfoModel):
            self._category_info = value
        else:
            self._category_info = CategoryInfoModel.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, SettleInfoModel):
            self._settle_infos = value
        else:
            self._settle_infos = SettleInfoModel.from_alipay_dict(value)
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAstoreQueryResponse, self).parse_response_content(response_content)
        if 'a_store_id' in response:
            self.a_store_id = response['a_store_id']
        if 'a_store_name' in response:
            self.a_store_name = response['a_store_name']
        if 'brand_info' in response:
            self.brand_info = response['brand_info']
        if 'category_info' in response:
            self.category_info = response['category_info']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'settle_infos' in response:
            self.settle_infos = response['settle_infos']
        if 'smid' in response:
            self.smid = response['smid']

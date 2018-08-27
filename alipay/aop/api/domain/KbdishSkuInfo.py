#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishPackagesDetailInfo import KbdishPackagesDetailInfo


class KbdishSkuInfo(object):

    def __init__(self):
        self._box_price = None
        self._dish_id = None
        self._dish_packages_detail_list = None
        self._goods_sku_id = None
        self._member_price = None
        self._out_sku_id = None
        self._sell_price = None
        self._sku_ext_content = None
        self._sku_id = None
        self._sku_sort = None
        self._spec_code_01 = None
        self._spec_code_02 = None
        self._spec_code_03 = None
        self._spec_code_04 = None
        self._spec_code_05 = None
        self._status = None

    @property
    def box_price(self):
        return self._box_price

    @box_price.setter
    def box_price(self, value):
        self._box_price = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_packages_detail_list(self):
        return self._dish_packages_detail_list

    @dish_packages_detail_list.setter
    def dish_packages_detail_list(self, value):
        if isinstance(value, list):
            self._dish_packages_detail_list = list()
            for i in value:
                if isinstance(i, KbdishPackagesDetailInfo):
                    self._dish_packages_detail_list.append(i)
                else:
                    self._dish_packages_detail_list.append(KbdishPackagesDetailInfo.from_alipay_dict(i))
    @property
    def goods_sku_id(self):
        return self._goods_sku_id

    @goods_sku_id.setter
    def goods_sku_id(self, value):
        self._goods_sku_id = value
    @property
    def member_price(self):
        return self._member_price

    @member_price.setter
    def member_price(self, value):
        self._member_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sku_ext_content(self):
        return self._sku_ext_content

    @sku_ext_content.setter
    def sku_ext_content(self, value):
        self._sku_ext_content = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_sort(self):
        return self._sku_sort

    @sku_sort.setter
    def sku_sort(self, value):
        self._sku_sort = value
    @property
    def spec_code_01(self):
        return self._spec_code_01

    @spec_code_01.setter
    def spec_code_01(self, value):
        self._spec_code_01 = value
    @property
    def spec_code_02(self):
        return self._spec_code_02

    @spec_code_02.setter
    def spec_code_02(self, value):
        self._spec_code_02 = value
    @property
    def spec_code_03(self):
        return self._spec_code_03

    @spec_code_03.setter
    def spec_code_03(self, value):
        self._spec_code_03 = value
    @property
    def spec_code_04(self):
        return self._spec_code_04

    @spec_code_04.setter
    def spec_code_04(self, value):
        self._spec_code_04 = value
    @property
    def spec_code_05(self):
        return self._spec_code_05

    @spec_code_05.setter
    def spec_code_05(self, value):
        self._spec_code_05 = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_price:
            if hasattr(self.box_price, 'to_alipay_dict'):
                params['box_price'] = self.box_price.to_alipay_dict()
            else:
                params['box_price'] = self.box_price
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_packages_detail_list:
            if isinstance(self.dish_packages_detail_list, list):
                for i in range(0, len(self.dish_packages_detail_list)):
                    element = self.dish_packages_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_packages_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_packages_detail_list, 'to_alipay_dict'):
                params['dish_packages_detail_list'] = self.dish_packages_detail_list.to_alipay_dict()
            else:
                params['dish_packages_detail_list'] = self.dish_packages_detail_list
        if self.goods_sku_id:
            if hasattr(self.goods_sku_id, 'to_alipay_dict'):
                params['goods_sku_id'] = self.goods_sku_id.to_alipay_dict()
            else:
                params['goods_sku_id'] = self.goods_sku_id
        if self.member_price:
            if hasattr(self.member_price, 'to_alipay_dict'):
                params['member_price'] = self.member_price.to_alipay_dict()
            else:
                params['member_price'] = self.member_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sku_ext_content:
            if hasattr(self.sku_ext_content, 'to_alipay_dict'):
                params['sku_ext_content'] = self.sku_ext_content.to_alipay_dict()
            else:
                params['sku_ext_content'] = self.sku_ext_content
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_sort:
            if hasattr(self.sku_sort, 'to_alipay_dict'):
                params['sku_sort'] = self.sku_sort.to_alipay_dict()
            else:
                params['sku_sort'] = self.sku_sort
        if self.spec_code_01:
            if hasattr(self.spec_code_01, 'to_alipay_dict'):
                params['spec_code_01'] = self.spec_code_01.to_alipay_dict()
            else:
                params['spec_code_01'] = self.spec_code_01
        if self.spec_code_02:
            if hasattr(self.spec_code_02, 'to_alipay_dict'):
                params['spec_code_02'] = self.spec_code_02.to_alipay_dict()
            else:
                params['spec_code_02'] = self.spec_code_02
        if self.spec_code_03:
            if hasattr(self.spec_code_03, 'to_alipay_dict'):
                params['spec_code_03'] = self.spec_code_03.to_alipay_dict()
            else:
                params['spec_code_03'] = self.spec_code_03
        if self.spec_code_04:
            if hasattr(self.spec_code_04, 'to_alipay_dict'):
                params['spec_code_04'] = self.spec_code_04.to_alipay_dict()
            else:
                params['spec_code_04'] = self.spec_code_04
        if self.spec_code_05:
            if hasattr(self.spec_code_05, 'to_alipay_dict'):
                params['spec_code_05'] = self.spec_code_05.to_alipay_dict()
            else:
                params['spec_code_05'] = self.spec_code_05
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
        o = KbdishSkuInfo()
        if 'box_price' in d:
            o.box_price = d['box_price']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_packages_detail_list' in d:
            o.dish_packages_detail_list = d['dish_packages_detail_list']
        if 'goods_sku_id' in d:
            o.goods_sku_id = d['goods_sku_id']
        if 'member_price' in d:
            o.member_price = d['member_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sku_ext_content' in d:
            o.sku_ext_content = d['sku_ext_content']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_sort' in d:
            o.sku_sort = d['sku_sort']
        if 'spec_code_01' in d:
            o.spec_code_01 = d['spec_code_01']
        if 'spec_code_02' in d:
            o.spec_code_02 = d['spec_code_02']
        if 'spec_code_03' in d:
            o.spec_code_03 = d['spec_code_03']
        if 'spec_code_04' in d:
            o.spec_code_04 = d['spec_code_04']
        if 'spec_code_05' in d:
            o.spec_code_05 = d['spec_code_05']
        if 'status' in d:
            o.status = d['status']
        return o



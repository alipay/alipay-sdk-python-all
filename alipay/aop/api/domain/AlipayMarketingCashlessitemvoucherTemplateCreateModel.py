#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCashlessitemvoucherTemplateCreateModel(object):

    def __init__(self):
        self._amount = None
        self._brand_name = None
        self._discount = None
        self._floor_amount = None
        self._goods_ceiling_quantity = None
        self._goods_cover_image_id = None
        self._goods_detail_image_ids = None
        self._goods_id = None
        self._goods_info = None
        self._goods_name = None
        self._goods_origin_price = None
        self._notify_uri = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._rule_conf = None
        self._special_price = None
        self._voucher_available_time = None
        self._voucher_description = None
        self._voucher_quantity = None
        self._voucher_type = None
        self._voucher_valid_period = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def goods_ceiling_quantity(self):
        return self._goods_ceiling_quantity

    @goods_ceiling_quantity.setter
    def goods_ceiling_quantity(self, value):
        self._goods_ceiling_quantity = value
    @property
    def goods_cover_image_id(self):
        return self._goods_cover_image_id

    @goods_cover_image_id.setter
    def goods_cover_image_id(self, value):
        self._goods_cover_image_id = value
    @property
    def goods_detail_image_ids(self):
        return self._goods_detail_image_ids

    @goods_detail_image_ids.setter
    def goods_detail_image_ids(self, value):
        self._goods_detail_image_ids = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        self._goods_info = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_origin_price(self):
        return self._goods_origin_price

    @goods_origin_price.setter
    def goods_origin_price(self, value):
        self._goods_origin_price = value
    @property
    def notify_uri(self):
        return self._notify_uri

    @notify_uri.setter
    def notify_uri(self, value):
        self._notify_uri = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def rule_conf(self):
        return self._rule_conf

    @rule_conf.setter
    def rule_conf(self, value):
        self._rule_conf = value
    @property
    def special_price(self):
        return self._special_price

    @special_price.setter
    def special_price(self, value):
        self._special_price = value
    @property
    def voucher_available_time(self):
        return self._voucher_available_time

    @voucher_available_time.setter
    def voucher_available_time(self, value):
        self._voucher_available_time = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        if isinstance(value, list):
            self._voucher_description = list()
            for i in value:
                self._voucher_description.append(i)
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        self._voucher_valid_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.goods_ceiling_quantity:
            if hasattr(self.goods_ceiling_quantity, 'to_alipay_dict'):
                params['goods_ceiling_quantity'] = self.goods_ceiling_quantity.to_alipay_dict()
            else:
                params['goods_ceiling_quantity'] = self.goods_ceiling_quantity
        if self.goods_cover_image_id:
            if hasattr(self.goods_cover_image_id, 'to_alipay_dict'):
                params['goods_cover_image_id'] = self.goods_cover_image_id.to_alipay_dict()
            else:
                params['goods_cover_image_id'] = self.goods_cover_image_id
        if self.goods_detail_image_ids:
            if hasattr(self.goods_detail_image_ids, 'to_alipay_dict'):
                params['goods_detail_image_ids'] = self.goods_detail_image_ids.to_alipay_dict()
            else:
                params['goods_detail_image_ids'] = self.goods_detail_image_ids
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_origin_price:
            if hasattr(self.goods_origin_price, 'to_alipay_dict'):
                params['goods_origin_price'] = self.goods_origin_price.to_alipay_dict()
            else:
                params['goods_origin_price'] = self.goods_origin_price
        if self.notify_uri:
            if hasattr(self.notify_uri, 'to_alipay_dict'):
                params['notify_uri'] = self.notify_uri.to_alipay_dict()
            else:
                params['notify_uri'] = self.notify_uri
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.rule_conf:
            if hasattr(self.rule_conf, 'to_alipay_dict'):
                params['rule_conf'] = self.rule_conf.to_alipay_dict()
            else:
                params['rule_conf'] = self.rule_conf
        if self.special_price:
            if hasattr(self.special_price, 'to_alipay_dict'):
                params['special_price'] = self.special_price.to_alipay_dict()
            else:
                params['special_price'] = self.special_price
        if self.voucher_available_time:
            if hasattr(self.voucher_available_time, 'to_alipay_dict'):
                params['voucher_available_time'] = self.voucher_available_time.to_alipay_dict()
            else:
                params['voucher_available_time'] = self.voucher_available_time
        if self.voucher_description:
            if isinstance(self.voucher_description, list):
                for i in range(0, len(self.voucher_description)):
                    element = self.voucher_description[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_description[i] = element.to_alipay_dict()
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_valid_period:
            if hasattr(self.voucher_valid_period, 'to_alipay_dict'):
                params['voucher_valid_period'] = self.voucher_valid_period.to_alipay_dict()
            else:
                params['voucher_valid_period'] = self.voucher_valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCashlessitemvoucherTemplateCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'discount' in d:
            o.discount = d['discount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'goods_ceiling_quantity' in d:
            o.goods_ceiling_quantity = d['goods_ceiling_quantity']
        if 'goods_cover_image_id' in d:
            o.goods_cover_image_id = d['goods_cover_image_id']
        if 'goods_detail_image_ids' in d:
            o.goods_detail_image_ids = d['goods_detail_image_ids']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_origin_price' in d:
            o.goods_origin_price = d['goods_origin_price']
        if 'notify_uri' in d:
            o.notify_uri = d['notify_uri']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'rule_conf' in d:
            o.rule_conf = d['rule_conf']
        if 'special_price' in d:
            o.special_price = d['special_price']
        if 'voucher_available_time' in d:
            o.voucher_available_time = d['voucher_available_time']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



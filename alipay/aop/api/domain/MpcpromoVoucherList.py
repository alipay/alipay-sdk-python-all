#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcpromoVoucherList(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name = None
        self._available_city_list = None
        self._available_shop_ids = None
        self._biz_tag = None
        self._brand_logo = None
        self._brand_name = None
        self._customer_service_mobile = None
        self._customer_service_url = None
        self._on_get_coupon_fail = None
        self._on_get_coupon_success = None
        self._on_get_coupon_url = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._sender_merchant_id = None
        self._total_num = None
        self._type = None
        self._voucher_comment = None
        self._voucher_description = None
        self._voucher_detail_images = None
        self._voucher_image = None
        self._voucher_rule = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def available_city_list(self):
        return self._available_city_list

    @available_city_list.setter
    def available_city_list(self, value):
        if isinstance(value, list):
            self._available_city_list = list()
            for i in value:
                self._available_city_list.append(i)
    @property
    def available_shop_ids(self):
        return self._available_shop_ids

    @available_shop_ids.setter
    def available_shop_ids(self, value):
        if isinstance(value, list):
            self._available_shop_ids = list()
            for i in value:
                self._available_shop_ids.append(i)
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        self._customer_service_mobile = value
    @property
    def customer_service_url(self):
        return self._customer_service_url

    @customer_service_url.setter
    def customer_service_url(self, value):
        self._customer_service_url = value
    @property
    def on_get_coupon_fail(self):
        return self._on_get_coupon_fail

    @on_get_coupon_fail.setter
    def on_get_coupon_fail(self, value):
        self._on_get_coupon_fail = value
    @property
    def on_get_coupon_success(self):
        return self._on_get_coupon_success

    @on_get_coupon_success.setter
    def on_get_coupon_success(self, value):
        self._on_get_coupon_success = value
    @property
    def on_get_coupon_url(self):
        return self._on_get_coupon_url

    @on_get_coupon_url.setter
    def on_get_coupon_url(self, value):
        self._on_get_coupon_url = value
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
    def sender_merchant_id(self):
        return self._sender_merchant_id

    @sender_merchant_id.setter
    def sender_merchant_id(self, value):
        self._sender_merchant_id = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher_comment(self):
        return self._voucher_comment

    @voucher_comment.setter
    def voucher_comment(self, value):
        self._voucher_comment = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_detail_images(self):
        return self._voucher_detail_images

    @voucher_detail_images.setter
    def voucher_detail_images(self, value):
        if isinstance(value, list):
            self._voucher_detail_images = list()
            for i in value:
                self._voucher_detail_images.append(i)
    @property
    def voucher_image(self):
        return self._voucher_image

    @voucher_image.setter
    def voucher_image(self, value):
        self._voucher_image = value
    @property
    def voucher_rule(self):
        return self._voucher_rule

    @voucher_rule.setter
    def voucher_rule(self, value):
        self._voucher_rule = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.available_city_list:
            if isinstance(self.available_city_list, list):
                for i in range(0, len(self.available_city_list)):
                    element = self.available_city_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_city_list[i] = element.to_alipay_dict()
            if hasattr(self.available_city_list, 'to_alipay_dict'):
                params['available_city_list'] = self.available_city_list.to_alipay_dict()
            else:
                params['available_city_list'] = self.available_city_list
        if self.available_shop_ids:
            if isinstance(self.available_shop_ids, list):
                for i in range(0, len(self.available_shop_ids)):
                    element = self.available_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_shop_ids, 'to_alipay_dict'):
                params['available_shop_ids'] = self.available_shop_ids.to_alipay_dict()
            else:
                params['available_shop_ids'] = self.available_shop_ids
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.customer_service_mobile:
            if hasattr(self.customer_service_mobile, 'to_alipay_dict'):
                params['customer_service_mobile'] = self.customer_service_mobile.to_alipay_dict()
            else:
                params['customer_service_mobile'] = self.customer_service_mobile
        if self.customer_service_url:
            if hasattr(self.customer_service_url, 'to_alipay_dict'):
                params['customer_service_url'] = self.customer_service_url.to_alipay_dict()
            else:
                params['customer_service_url'] = self.customer_service_url
        if self.on_get_coupon_fail:
            if hasattr(self.on_get_coupon_fail, 'to_alipay_dict'):
                params['on_get_coupon_fail'] = self.on_get_coupon_fail.to_alipay_dict()
            else:
                params['on_get_coupon_fail'] = self.on_get_coupon_fail
        if self.on_get_coupon_success:
            if hasattr(self.on_get_coupon_success, 'to_alipay_dict'):
                params['on_get_coupon_success'] = self.on_get_coupon_success.to_alipay_dict()
            else:
                params['on_get_coupon_success'] = self.on_get_coupon_success
        if self.on_get_coupon_url:
            if hasattr(self.on_get_coupon_url, 'to_alipay_dict'):
                params['on_get_coupon_url'] = self.on_get_coupon_url.to_alipay_dict()
            else:
                params['on_get_coupon_url'] = self.on_get_coupon_url
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
        if self.sender_merchant_id:
            if hasattr(self.sender_merchant_id, 'to_alipay_dict'):
                params['sender_merchant_id'] = self.sender_merchant_id.to_alipay_dict()
            else:
                params['sender_merchant_id'] = self.sender_merchant_id
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.voucher_comment:
            if hasattr(self.voucher_comment, 'to_alipay_dict'):
                params['voucher_comment'] = self.voucher_comment.to_alipay_dict()
            else:
                params['voucher_comment'] = self.voucher_comment
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_detail_images:
            if isinstance(self.voucher_detail_images, list):
                for i in range(0, len(self.voucher_detail_images)):
                    element = self.voucher_detail_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_detail_images[i] = element.to_alipay_dict()
            if hasattr(self.voucher_detail_images, 'to_alipay_dict'):
                params['voucher_detail_images'] = self.voucher_detail_images.to_alipay_dict()
            else:
                params['voucher_detail_images'] = self.voucher_detail_images
        if self.voucher_image:
            if hasattr(self.voucher_image, 'to_alipay_dict'):
                params['voucher_image'] = self.voucher_image.to_alipay_dict()
            else:
                params['voucher_image'] = self.voucher_image
        if self.voucher_rule:
            if hasattr(self.voucher_rule, 'to_alipay_dict'):
                params['voucher_rule'] = self.voucher_rule.to_alipay_dict()
            else:
                params['voucher_rule'] = self.voucher_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcpromoVoucherList()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'available_city_list' in d:
            o.available_city_list = d['available_city_list']
        if 'available_shop_ids' in d:
            o.available_shop_ids = d['available_shop_ids']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        if 'customer_service_url' in d:
            o.customer_service_url = d['customer_service_url']
        if 'on_get_coupon_fail' in d:
            o.on_get_coupon_fail = d['on_get_coupon_fail']
        if 'on_get_coupon_success' in d:
            o.on_get_coupon_success = d['on_get_coupon_success']
        if 'on_get_coupon_url' in d:
            o.on_get_coupon_url = d['on_get_coupon_url']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'sender_merchant_id' in d:
            o.sender_merchant_id = d['sender_merchant_id']
        if 'total_num' in d:
            o.total_num = d['total_num']
        if 'type' in d:
            o.type = d['type']
        if 'voucher_comment' in d:
            o.voucher_comment = d['voucher_comment']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_detail_images' in d:
            o.voucher_detail_images = d['voucher_detail_images']
        if 'voucher_image' in d:
            o.voucher_image = d['voucher_image']
        if 'voucher_rule' in d:
            o.voucher_rule = d['voucher_rule']
        return o



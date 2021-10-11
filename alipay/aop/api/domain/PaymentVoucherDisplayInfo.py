#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherDisplayInfo(object):

    def __init__(self):
        self._brand_name = None
        self._customer_service_mobile = None
        self._voucher_description = None
        self._voucher_detail_images = None
        self._voucher_image = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherDisplayInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_detail_images' in d:
            o.voucher_detail_images = d['voucher_detail_images']
        if 'voucher_image' in d:
            o.voucher_image = d['voucher_image']
        return o



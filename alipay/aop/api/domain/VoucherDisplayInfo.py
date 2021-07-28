#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherDisplayInfo(object):

    def __init__(self):
        self._brand_logo = None
        self._brand_name = None
        self._voucher_comment = None
        self._voucher_description = None
        self._voucher_image = None

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
    def voucher_image(self):
        return self._voucher_image

    @voucher_image.setter
    def voucher_image(self, value):
        self._voucher_image = value


    def to_alipay_dict(self):
        params = dict()
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
        o = VoucherDisplayInfo()
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'voucher_comment' in d:
            o.voucher_comment = d['voucher_comment']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_image' in d:
            o.voucher_image = d['voucher_image']
        return o



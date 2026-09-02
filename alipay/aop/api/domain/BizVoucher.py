#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizVoucher(object):

    def __init__(self):
        self._active_time = None
        self._brand_logo = None
        self._brand_name = None
        self._expire_time = None
        self._issuer_type = None
        self._promo_type = None
        self._rights_desc = None
        self._use_threshold_text = None
        self._voucher_id = None
        self._voucher_link_url = None
        self._voucher_name = None
        self._voucher_status = None
        self._voucher_unit = None
        self._voucher_value = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
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
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def issuer_type(self):
        return self._issuer_type

    @issuer_type.setter
    def issuer_type(self, value):
        self._issuer_type = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def rights_desc(self):
        return self._rights_desc

    @rights_desc.setter
    def rights_desc(self, value):
        self._rights_desc = value
    @property
    def use_threshold_text(self):
        return self._use_threshold_text

    @use_threshold_text.setter
    def use_threshold_text(self, value):
        self._use_threshold_text = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_link_url(self):
        return self._voucher_link_url

    @voucher_link_url.setter
    def voucher_link_url(self, value):
        self._voucher_link_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value
    @property
    def voucher_unit(self):
        return self._voucher_unit

    @voucher_unit.setter
    def voucher_unit(self, value):
        self._voucher_unit = value
    @property
    def voucher_value(self):
        return self._voucher_value

    @voucher_value.setter
    def voucher_value(self, value):
        self._voucher_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
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
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.issuer_type:
            if hasattr(self.issuer_type, 'to_alipay_dict'):
                params['issuer_type'] = self.issuer_type.to_alipay_dict()
            else:
                params['issuer_type'] = self.issuer_type
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.rights_desc:
            if hasattr(self.rights_desc, 'to_alipay_dict'):
                params['rights_desc'] = self.rights_desc.to_alipay_dict()
            else:
                params['rights_desc'] = self.rights_desc
        if self.use_threshold_text:
            if hasattr(self.use_threshold_text, 'to_alipay_dict'):
                params['use_threshold_text'] = self.use_threshold_text.to_alipay_dict()
            else:
                params['use_threshold_text'] = self.use_threshold_text
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_link_url:
            if hasattr(self.voucher_link_url, 'to_alipay_dict'):
                params['voucher_link_url'] = self.voucher_link_url.to_alipay_dict()
            else:
                params['voucher_link_url'] = self.voucher_link_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        if self.voucher_unit:
            if hasattr(self.voucher_unit, 'to_alipay_dict'):
                params['voucher_unit'] = self.voucher_unit.to_alipay_dict()
            else:
                params['voucher_unit'] = self.voucher_unit
        if self.voucher_value:
            if hasattr(self.voucher_value, 'to_alipay_dict'):
                params['voucher_value'] = self.voucher_value.to_alipay_dict()
            else:
                params['voucher_value'] = self.voucher_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizVoucher()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'issuer_type' in d:
            o.issuer_type = d['issuer_type']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'rights_desc' in d:
            o.rights_desc = d['rights_desc']
        if 'use_threshold_text' in d:
            o.use_threshold_text = d['use_threshold_text']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_link_url' in d:
            o.voucher_link_url = d['voucher_link_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_unit' in d:
            o.voucher_unit = d['voucher_unit']
        if 'voucher_value' in d:
            o.voucher_value = d['voucher_value']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceGasInfoGroupcouponQueryModel(object):

    def __init__(self):
        self._create_end_time = None
        self._create_start_time = None
        self._page_num = None
        self._page_size = None
        self._partner_id = None
        self._shop_id = None
        self._user_id = None
        self._voucher_status = None

    @property
    def create_end_time(self):
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, value):
        self._create_end_time = value
    @property
    def create_start_time(self):
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, value):
        self._create_start_time = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_end_time:
            if hasattr(self.create_end_time, 'to_alipay_dict'):
                params['create_end_time'] = self.create_end_time.to_alipay_dict()
            else:
                params['create_end_time'] = self.create_end_time
        if self.create_start_time:
            if hasattr(self.create_start_time, 'to_alipay_dict'):
                params['create_start_time'] = self.create_start_time.to_alipay_dict()
            else:
                params['create_start_time'] = self.create_start_time
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceGasInfoGroupcouponQueryModel()
        if 'create_end_time' in d:
            o.create_end_time = d['create_end_time']
        if 'create_start_time' in d:
            o.create_start_time = d['create_start_time']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


